# app/testProduct.py

from modelos.Product import Product
from conexionDB.Conexion import Conexion

# Parámetros de conexión
host = 'localhost'
port = 3306
user = 'root'
password = 'root_password'  # Asegúrate de que esta contraseña sea la correcta
database = 'TiendaJPBB'  # Nombre de la base de datos que creaste

def test_product_operations():
    # Crear una instancia de la clase Conexion
    db = Conexion(host, port, user, password, database)
    db.connect_db()

    # Crear un producto
    product = Product(None, None, None, None, None, None, None)
    print("Agregando producto...")
    product.create_product(db)

    # Listar todos los productos
    print("Listando productos...")
    products = product.select_product(db)
    if products:
        print("Productos en la base de datos:")
        for prod in products:
            print(f"ID: {prod.product_id}, Nombre: {prod.product_name}, Descripción: {prod.description}, Categoría ID: {prod.category_id}, Precio: {prod.price}, Cantidad: {prod.quantity}, Marca: {prod.brand}")
    else:
        print("No se encontraron productos.")

    # Actualizar un producto
    print("Actualizando producto...")
    product.update_product(db)

    # Eliminar un producto (si deseas probar esta funcionalidad, asegúrate de proporcionar un ID válido)
    product_id_to_delete = int(input("Ingrese el ID del producto a eliminar: "))
    print(f"Eliminando producto con ID {product_id_to_delete}...")
    product.delete_product(db, product_id_to_delete)

    # Desconectar de la base de datos
    db.disconnect()

if __name__ == "__main__":
    test_product_operations()
