# app/testCustomer.py

from modelos.Customer import Customer
from conexionDB.Conexion import Conexion

# Parámetros de conexión
host = 'localhost'
port = 3306
user = 'root'
password = 'root_password'  # Asegúrate de que esta contraseña sea la correcta
database = 'TiendaJPBB'  # Nombre de la base de datos que creaste

def test_customer_operations():
    # Crear una instancia de la clase Conexion
    db = Conexion(host, port, user, password, database)
    db.connect_db()

    # Crear un cliente
    customer = Customer(None, None, None, None, None, None, None)
    print("Agregando cliente...")
    customer.create_customer(db)

    # Listar todos los clientes
    print("Listando clientes...")
    customers = customer.select_customer(db)
    if customers:
        print("Clientes en la base de datos:")
        for cust in customers:
            print(f"ID: {cust.customer_id}, Nombre: {cust.customer_name}, Apellido: {cust.customer_last_name}, Email: {cust.email}, Tipo: {cust.customer_type}, Puntos: {cust.points}")
    else:
        print("No se encontraron clientes.")

    # Actualizar un cliente
    print("Actualizando cliente...")
    customer.update_customer(db)

    # Eliminar un cliente (si deseas probar esta funcionalidad, asegúrate de proporcionar un ID válido)
    customer_id_to_delete = int(input("Ingrese el ID del cliente a eliminar: "))
    print(f"Eliminando cliente con ID {customer_id_to_delete}...")
    customer.delete_customer(db, customer_id_to_delete)

    # Desconectar de la base de datos
    db.disconnect()

if __name__ == "__main__":
    test_customer_operations()
