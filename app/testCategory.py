# modelos/testCategory.py

from modelos.Category import Category
from conexionDB.Conexion import Conexion

# Parámetros de conexión
host = 'localhost'
port = 3306
user = 'root'
password = 'root_password'  # Asegúrate de que esta contraseña sea la correcta
database = 'TiendaJPBB'  # Nombre de la base de datos que creaste

def test_category_operations():
    # Crear una instancia de la clase Conexion
    db = Conexion(host, port, user, password, database)
    db.connect_db()

    # Crear una categoría
    category = Category(None, None)
    print("Agregando categoría...")
    category.create_category(db)

    # Listar todas las categorías
    print("Listando categorías...")
    categories = category.select_category(db)
    if categories:
        print("Categorías en la base de datos:")
        for cat in categories:
            print(f"ID: {cat.category_id}, Nombre: {cat.category_name}")
    else:
        print("No se encontraron categorías.")

    # Actualizar una categoría
    print("Actualizando categoría...")
    category.update_category(db)

    # Eliminar una categoría (si deseas probar esta funcionalidad, asegúrate de proporcionar un ID válido)
    category_id_to_delete = int(input("Ingrese el ID de la categoría a eliminar: "))
    print(f"Eliminando categoría con ID {category_id_to_delete}...")
    category.delete_category(db, category_id_to_delete)

    # Desconectar de la base de datos
    db.disconnect()

if __name__ == "__main__":
    test_category_operations()
