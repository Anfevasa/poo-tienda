# app/main.py

from modelos.Category import Category
from modelos.Employee import Employee
from modelos.Customer import Customer
from modelos.Product import Product
from modelos.Sales import Sales
from conexionDB.Conexion import Conexion

# Parámetros de conexión
host = 'localhost'
port = 3306
user = 'root'
password = 'root_password'  # Asegúrate de que esta contraseña sea la correcta
database = 'TiendaJPBB'  # Nombre de la base de datos que creaste

def display_menu():
    print("\n*** Menú Principal ***")
    print("1. Categorías")
    print("2. Empleados")
    print("3. Clientes")
    print("4. Productos")
    print("5. Ventas")
    print("6. Salir")

def handle_category_operations(db):
    print("\n*** Opciones de Categoría ***")
    print("1. Crear categoría")
    print("2. Ver categorías")
    print("3. Eliminar categoría")
    print("4. Actualizar categoría")
    choice = input("Elija una opción: ")

    if choice == '1':
        category = Category(None, None)
        category.create_category(db)
    elif choice == '2':
        Category(None, None).select_category(db)
    elif choice == '3':
        category_id = int(input("Ingrese el ID de la categoría a eliminar: "))
        Category(None, None).delete_category(db, category_id)
    elif choice == '4':
        category_id = int(input("Ingrese el ID de la categoría a actualizar: "))
        category = Category(category_id, None)
        category.update_category(db)
    else:
        print("Opción inválida")

def handle_employee_operations(db):
    print("\n*** Opciones de Empleado ***")
    print("1. Crear empleado")
    print("2. Ver empleados")
    print("3. Eliminar empleado")
    print("4. Actualizar empleado")
    choice = input("Elija una opción: ")

    if choice == '1':
        employee = Employee(None, None, None, None, None, None,None)
        employee.create_employee(db)
    elif choice == '2':
        Employee(None, None, None, None, None, None, None).select_employee(db)
    elif choice == '3':
        employee_id = int(input("Ingrese el ID del empleado a eliminar: "))
        Employee(None, None, None, None, None, None, None).delete_employee(db, employee_id)
    elif choice == '4':
        employee_id = int(input("Ingrese el ID del empleado a actualizar: "))
        employee = Employee(employee_id, None, None, None, None, None, None)
        employee.update_employee(db)
    else:
        print("Opción inválida")

def handle_customer_operations(db):
    print("\n*** Opciones de Cliente ***")
    print("1. Crear cliente")
    print("2. Ver clientes")
    print("3. Eliminar cliente")
    print("4. Actualizar cliente")
    choice = input("Elija una opción: ")

    if choice == '1':
        customer = Customer(None, None, None, None, None, None)
        customer.create_customer(db)
    elif choice == '2':
        Customer(None, None, None, None, None, None).select_customer(db)
    elif choice == '3':
        customer_id = int(input("Ingrese el ID del cliente a eliminar: "))
        Customer(None, None, None, None, None, None).delete_customer(db, customer_id)
    elif choice == '4':
        customer_id = int(input("Ingrese el ID del cliente a actualizar: "))
        customer = Customer(customer_id, None, None, None, None, None)
        customer.update_customer(db)
    else:
        print("Opción inválida")

def handle_product_operations(db):
    print("\n*** Opciones de Producto ***")
    print("1. Crear producto")
    print("2. Ver productos")
    print("3. Eliminar producto")
    print("4. Actualizar producto")
    choice = input("Elija una opción: ")

    if choice == '1':
        product = Product(None, None, None, None, None, None, None)
        product.create_product(db)
    elif choice == '2':
        Product(None, None, None, None, None, None, None).select_product(db)
    elif choice == '3':
        product_id = int(input("Ingrese el ID del producto a eliminar: "))
        Product(None, None, None, None, None, None, None).delete_product(db, product_id)
    elif choice == '4':
        product_id = int(input("Ingrese el ID del producto a actualizar: "))
        product = Product(product_id, None, None, None, None, None, None)
        product.update_product(db)
    else:
        print("Opción inválida")

def handle_sales_operations(db):
    print("\n*** Opciones de Venta ***")
    print("1. Crear venta")
    print("2. Ver ventas")
    print("3. Eliminar venta")
    print("4. Actualizar venta")
    choice = input("Elija una opción: ")

    if choice == '1':
        sale = Sales(None, None, None, None, None, None, None, None)
        sale.create_sale(db)
    elif choice == '2':
        Sales(None, None, None, None, None, None, None, None).select_sales(db)
    elif choice == '3':
        sale_id = int(input("Ingrese el ID de la venta a eliminar: "))
        Sales(None, None, None, None, None, None, None, None).delete_sale(db, sale_id)
    elif choice == '4':
        sale = Sales(None, None, None, None, None, None, None, None)
        sale.update_sale(db)
    else:
        print("Opción inválida")

def main():
    db = Conexion(host, port, user, password, database)
    db.connect_db()

    while True:
        display_menu()
        choice = input("Elija una opción: ")

        if choice == '1':
            handle_category_operations(db)
        elif choice == '2':
            handle_employee_operations(db)
        elif choice == '3':
            handle_customer_operations(db)
        elif choice == '4':
            handle_product_operations(db)
        elif choice == '5':
            handle_sales_operations(db)
        elif choice == '6':
            db.disconnect()
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
