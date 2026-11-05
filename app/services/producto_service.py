from app.models import db
from app.models.producto import Producto

class ProductoService:
    @staticmethod
    def get_all():
        productos = Producto.query.all()
        return [producto.to_dict() for producto in productos]
    
    @staticmethod
    def create(data):
        # ... (el código que ya tienes para crear)
        pass