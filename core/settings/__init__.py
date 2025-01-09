import os

from dotenv import load_dotenv

# loading env
load_dotenv()

environment = os.getenv('DJANGO_ENV', 'dev')

if environment == 'production':
    from .production import *
else:
    from .dev import *
