

from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
__version__ = "1.3.1"

class MQTTException(Exception):
    pass
