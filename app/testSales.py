# app/testSales.py

from modelos.Sales import Sales
from conexionDB.Conexion import Conexion

# Parámetros de conexión
host = 'localhost'
port = 3306
user = 'root'
password = 'root_password'  # Asegúrate de que esta contraseña sea la correcta
database = 'TiendaJPBB'  # Nombre de la base de datos que creaste

def test_sales_operations():
    # Crear una instancia de la clase Conexion
    db = Conexion(host, port, user, password, database)
    db.connect_db()

    # Crear una venta
    sale = Sales(None, None, None, None, None, None, None, None)
    print("Agregando venta...")
    sale.create_sale(db)

    # Listar todas las ventas
    print("Listando ventas...")
    sales = sale.select_sales(db)
    if sales:
        print("Ventas en la base de datos:")
        for s in sales:
            print(f"ID: {s.sale_id}, Fecha: {s.sale_date}, Cliente ID: {s.customer_id}, Producto ID: {s.product_id}, Precio: {s.price}, Cantidad: {s.quantity}, Total: {s.total}, Empleado ID: {s.employee_id}")
    else:
        print("No se encontraron ventas.")

    # Actualizar una venta
    print("Actualizando venta...")
    sale.update_sale(db)

    # Eliminar una venta (si deseas probar esta funcionalidad, asegúrate de proporcionar un ID válido)
    sale_id_to_delete = int(input("Ingrese el ID de la venta a eliminar: "))
    print(f"Eliminando venta con ID {sale_id_to_delete}...")
    sale.delete_sale(db, sale_id_to_delete)

    # Desconectar de la base de datos
    db.disconnect()

if __name__ == "__main__":
    test_sales_operations()
