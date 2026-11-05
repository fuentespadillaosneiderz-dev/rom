from flask import Flask
from app.common.config import Config
from app.models import db
from app.common.error import error_bp
from app.controllers.producto_controller import producto_bp

# <--- Importa tus modelos aquí para que SQLAlchemy los reconozca
from app.models.producto import Producto
from app.models.categoria import Categoria

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    db.init_app(app)
    
    app.register_blueprint(error_bp)
    app.register_blueprint(producto_bp)
    
    with app.app_context():
        db.create_all()
        
    return app