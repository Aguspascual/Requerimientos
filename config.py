import os

class Seguridad:
    SECRET_KEY = '1234_567_89'

class Config (Seguridad):
    # Heredo de la clase Seguridad
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:admin@localhost/requerimientos')
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:wLeDuriQHbkUnhSRnOCxvGeSzhBqdsuX@gondola.proxy.rlwy.net:12820/railway'
    



    SQLALCHEMY_TRACK_MODIFICATIONS = False

