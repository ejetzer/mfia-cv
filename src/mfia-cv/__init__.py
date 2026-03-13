import sys
from typing import Final, Self, Any
from logging import getLogger, Logger
from zhinst.toolkit import Session
from zhinst.toolkit.session import Devices
from zhinst.toolkit.driver.devices import DeviceType
from zhinst.toolkit.exceptions import ToolkitError, ValidationError
from zhinst.core.errors import *

logging: Final[Logger] = getLogger(__name__)

class Var:
    
    def __init__(self, nom: str, _type: type = type(None), strict: bool = True, default: Any = None):
        self.nom: Final[str] = nom
        self._type: Final[type] = _type
        self.strict: Final[bool] = strict
        self.default: Final[Any] = default
    
    @property
    def value(self):
        cadre = inspect.currentframe().f_back
        if self.nom in cadre.f_locals:
            return cadre.f_locals[self.nom]
        elif self.nom in cadre.f_globals:
            return cadre.f_globals[self.nom]
        elif self.strict:
            msg = f'Aucune variable nommée {self.nom} trouvée'
            raise NameError(msg)
        else:
            return self.default
    
    def __repr__(self):
        return f'<{self.__class__.__module__}.{self.__class__.__name__} object @ {id(self)} == {self.value:r}>'
    
    def __str__(self):
        return str(self.value)
        
    
    

class MessageErreur:
    
    def __init__(self, *msg):
        self.msg: tuple[str|Var] = msg
    
    def __call__(self, *args, **kargs):
        pass
    
    def __str__(self):
        pass
    
    def __lmod__(self, right: str|tuple):
        if isinstance(right, str):
            pass
        elif isinstance(right, tuple):
            pass
        else:
            return NotImplemented
    
    def __format__(self, *args, **kargs):
        pass

class MFIA:
    
    exceptions = {
        None: (True, ''),
        TypeError: (False, ''),
        CoreError: (False, ''),
        ToolkitError: (False, ''),
        ValidationError: (False, ''),
        TimeoutError: (False, ''),
    }
    
    def __init__(
        self,
        host: str = 'localhost',
        dev: str|list[str]|None = None
    ):
        self.
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
    
    @property
    def devid(self):
        return self.__dev
    
    @property
    def host(self):
        return self.__host
    
    @property
    def session(self):
        if session is None:
            msg = '\'session\' n\'est pas initialisé. Il n\'y a pas de session en cours.'
            raise RuntimeError(msg)
        else:
            return self.__session
    
    @property
    def actif(self):
        return self.__session is not None
    
    def __enter__(self) -> Self:
        self.__session: Session = Session(self.host, allow_version_mismatch=True)
        
        for _dev in self.devid:
            self.session.connect_device(_dev)
        
        # Basé sur zhinst.toolkit.session.Session.set_transaction
        self.session.sync()
        self.session._multi_transaction.start()
        for device in self.session.devices.created_devices():
            device.root.transaction.start(self.session._multi_transaction.add)
        self.session.root.transaction.start(self.session._multi_transaction.add)
        
        return self
    
    def __iter__(self):
        self.__step = 0
        self.setup()

        return self
    
    def __next__(self):
        res = self.loop()
        self.__step += 1
        return res
    
    def setup(self):
        pass
    
    def loop(self):
        pass
    
    def __exit__(self, exc_type, exc_value, traceback):
        # Basé sur zhinst.toolkit.session.Session.set_transaction
        self.session._daq_server.set(self.__session._multi_transaction.result())
        for device in self.__session.devices.created_devices():
            device.root.transaction.stop()
        self.session.root.transaction.stop()
        self.session._multi_transaction.stop()

        self.session.sync()
        for _dev in self.devices:
            _dev.session.disconnect_device(_dev.serial)
        
        self.__session = None
        
        status, msg = self.exceptions[exc_type]
        ((status and logging.debug) or logging.error)(msg, self, exc_type, exc_value, traceback)
        return status
