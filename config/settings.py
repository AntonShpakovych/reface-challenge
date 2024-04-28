import os
from dotenv import load_dotenv


load_dotenv()


DEBUG = os.getenv("DJANGO_DEBUG_MODE") == "True"

if DEBUG:
    from .local import *
else:
    # from .production import *
    pass
