from flask import Blueprint, render_template
from app.services.producto_service import ProductoService

producto_bp = Blueprint('producto_bp', __name__)

@producto_bp.route('/products', methods=['GET'])
def listar_productos():
    # Obtenemos los productos desde la base de datos
    productos = ProductoService.get_all()
    # Renderizamos la plantilla HTML y le pasamos la lista de productos
    return render_template('productos.html', productos=productos)