import sys
from typing import Final
from logging import getLogger, basicConfig, INFO
from zhinst.toolkit import Session
from zhinst.toolkit.exceptions import ToolkitError, ValidationError
from zhinst.core.errors import *

from . import MFIA

logging: Final[str] = getLogger(__name__)
basicConfig(stream=sys.stderr, level=INFO)

DEVID: Final[str] = 'dev7898'
NOM: Final[str] = f'mf-{DEVID}'
HOSTS: Final[str] = f'{NOM}.local'

with MFIA(HOST, DEVID) as mfia:
    for status in mfia:
        logging.info('status = %r', status)
