import os

class Config:
    USER = 'root'
    PASSWORD = ''  # Déjalo en blanco si tu MySQL no utiliza contraseña
    HOST = 'localhost'
    DATABASE = 'inventario'

    # URL para desarrollo local
    LOCAL_DB = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}'

    # os.getenv busca primero la variable en Render. Si no la encuentra, usa LOCAL_DB
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', LOCAL_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False