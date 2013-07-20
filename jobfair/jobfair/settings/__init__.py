import os

if 'PROD' in os.environ:
    from .production import *
else:
    from .local import *

