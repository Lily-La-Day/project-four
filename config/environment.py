import os

db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/write_hand')

secret = os.getenv('SECRET', 'secreto')

LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
