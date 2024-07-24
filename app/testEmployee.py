# app/testEmployee.py

from modelos.Employee import Employee
from conexionDB.Conexion import Conexion

# Parámetros de conexión
host = 'localhost'
port = 3306
user = 'root'
password = 'root_password'  # Asegúrate de que esta contraseña sea la correcta
database = 'TiendaJPBB'  # Nombre de la base de datos que creaste

def test_employee_operations():
    # Crear una instancia de la clase Conexion
    db = Conexion(host, port, user, password, database)
    db.connect_db()

    # Crear un empleado
    employee = Employee(None, None, None, None, None, None, None)
    print("Agregando empleado...")
    employee.create_employee(db)

    # Listar todos los empleados
    print("Listando empleados...")
    employees = employee.select_employee(db)
    if employees:
        print("Empleados en la base de datos:")
        for emp in employees:
            print(f"ID: {emp.employee_id}, Nombre: {emp.employee_name}, Apellido: {emp.employee_last_name}, Email: {emp.email}, Salario: {emp.salary}, Posición: {emp.position}")
    else:
        print("No se encontraron empleados.")

    # Actualizar un empleado
    print("Actualizando empleado...")
    employee.update_employee(db)

    # Eliminar un empleado (si deseas probar esta funcionalidad, asegúrate de proporcionar un ID válido)
    employee_id_to_delete = int(input("Ingrese el ID del empleado a eliminar: "))
    print(f"Eliminando empleado con ID {employee_id_to_delete}...")
    employee.delete_employee(db, employee_id_to_delete)

    # Desconectar de la base de datos
    db.disconnect()

if __name__ == "__main__":
    test_employee_operations()
