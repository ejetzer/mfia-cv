import sys
from typing import Final
from logging import getLogger, basicConfig, INFO
from zhinst.toolkit import Session
from zhinst.toolkit.exceptions import ToolkitError, ValidationError
from zhinst.core.errors import *

logging: Final[str] = getLogger(__name__)
basicConfig(stream=sys.stderr, level=INFO)

DEVID: Final[str] = 'dev7898'
NOM: Final[str] = f'mf-{DEVID}'
HOSTS: Final[str] = ('localhost', f'{NOM}.local')

for host in HOSTS:
    try:
        session: Session = Session(host, allow_version_mismatch=True)
    except CoreError:
        logging.exception('Problème de connexion à %s', host)
    else:
        logging.info('Connexion réussie à %s', host)
        break

try:
    appareil = session.connect_device(DEVID)

    appareil.system.identify(True)
    print(appareil.status.time())
except ConnectionError:
    logging.exception('Connexion avec %s via %s impossible.', DEVID, HOST)
except TimeoutError:
    logging.exception('Délai de communication avec %s via %s dépassé.', DEVID, HOST)
except CoreError:
    logging.exception('Problème interne du module zhinst')
else:
    
finally:
    session.disconnect_device(DEVID)
