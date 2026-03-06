import sys
from typing import Final, Self
from logging import getLogger, Logger, basicConfig, INFO
from zhinst.toolkit import Session
from zhinst.toolkit.session import Devices
from zhinst.toolkit.driver.devices import DeviceType
from zhinst.toolkit.exceptions import ToolkitError, ValidationError
from zhinst.core.errors import *

logging: Final[Logger] = getLogger(__name__)

class MFIA:
    
    def __init__(
        self,
        host: str = 'localhost',
        dev: str|list[str]|None = None
    ):
        self.__host: Final[str] = host
        
        self.__dev: list[str] = []
        if isinstance(dev, str):
            self.__dev = [dev]
        elif isinstance(dev, list):
            self.__dev = dev
        elif dev is not None:
            msg: str = 'parameter `dev` should be of type list[str]|str|None'
            raise TypeError(msg)
        
        self.__session: Session|None = None
    
    def __enter__(self) -> Self:
        self.__session: Session = Session(self.host, allow_version_mismatch=True)
        
        for _dev in self.__dev:
            self.__session.connect_device(_dev)
        
        # Basé sur zhinst.toolkit.session.Session.set_transaction
        self.__session.sync()
        self.__session._multi_transaction.start()
        for device in self.__session.devices.created_devices():
            device.root.transaction.start(self.__session._multi_transaction.add)
        self.__session.root.transaction.start(self.__session._multi_transaction.add)
        
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        # Basé sur zhinst.toolkit.session.Session.set_transaction
        self.__session._daq_server.set(self.__session._multi_transaction.result())
        for device in self.__session.devices.created_devices():
            device.root.transaction.stop()
        self.__session.root.transaction.stop()
        self.__session._multi_transaction.stop()

        self.__session.sync()
        for _dev in self.devices:
            _dev.session.disconnect_device(_dev.serial)
        
        self.__session = None
        
        if exc_type is None:
            logging.debug('%r has disconnected from %s at %s.', self, self.devid, self.host)
            return True
        else:
            return False