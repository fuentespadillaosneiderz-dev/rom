from flask import Flask
from flask_cors import CORS
from app.common.config import Config
from app.models import db
from app.common.error import error_bp
from app.controllers.producto_controller import producto_bp

# Importa tus modelos para que SQLAlchemy los reconozca
from app.models.producto import Producto
from app.models.categoria import Categoria

def create_app():
    app = Flask(__name__)
    
    # Habilitar CORS para permitir peticiones desde React
    CORS(app)
    
    app.config.from_object(Config)
    db.init_app(app)
    
    app.register_blueprint(error_bp)
    app.register_blueprint(producto_bp)
    
    # Ruta raíz usando add_url_rule (ideal para Factory Pattern)
    def index():
        return "¡Bienvenido a mi API de Inventario con Flask y Aiven!"
        
    app.add_url_rule('/', 'index', index)
    
    with app.app_context():
        db.create_all()
        
    return app