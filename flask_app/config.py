import os

# Stores all configuration values
SECRET_KEY = os.environ.get('SECRET_KEY')
MONGODB_HOST = os.environ.get('MONGODB_HOST')