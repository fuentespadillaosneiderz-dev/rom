from flask import Flask, redirect
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
    
    # Redirige la página principal directo a la tabla de productos
    def index():
        return redirect('/products')
        
    app.add_url_rule('/', 'index', index)
    
    with app.app_context():
        db.create_all()
        
        # Insertar productos de prueba automáticamente si la tabla está vacía
        if Producto.query.count() == 0:
            p1 = Producto(nombre="Teclado Mecánico", descripcion="Teclado RGB switch blue", precio=120000.0, stock=5)
            p2 = Producto(nombre="Mouse Gamer", descripcion="Mouse óptico 7200 DPI", precio=65000.0, stock=10)
            p3 = Producto(nombre="Laptop Gamer", descripcion="Laptop 16GB RAM RTX 4060", precio=3500000.0, stock=3)
            p4 = Producto(nombre="Audífonos Bluetooth", descripcion="Audífonos inalámbricos con cancelación de ruido", precio=180000.0, stock=7)
            
            db.session.add(p1)
            db.session.add(p2)
            db.session.add(p3)
            db.session.add(p4)
            db.session.commit()
            
    return app