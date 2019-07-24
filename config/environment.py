import os

db_uri = os.getenv('DATABASE_URI', 'postgres://localhost:5432/write_hand')

secret = os.getenv('SECRET', 'secreto')
