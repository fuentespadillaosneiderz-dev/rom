class Config:
    USER = 'root'
    PASSWORD = ''  # Déjalo en blanco si tu MySQL no utiliza contraseña
    HOST = 'localhost'
    DATABASE = 'inventario'

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False