from .base import *


DEBUG = False

SECURE_SSL_REDIRECT = bool(os.getenv("SECURE_SSL_REDIRECT", "1"))
