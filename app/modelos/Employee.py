# modelos/Employee.py

from conexionDB.Conexion import Conexion

class Employee:
    employee_id = None
    employee_name = None
    employee_last_name = None
    email = None
    employee_password = None
    salary = None
    position = None

    def __init__(self, employee_id, employee_name, employee_last_name, email, employee_password, salary, position):
        self._employee_id = employee_id
        self._employee_name = employee_name
        self._employee_last_name = employee_last_name
        self._email = email
        self._employee_password = employee_password
        self._salary = salary
        self._position = position

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def employee_name(self):
        return self._employee_name

    @employee_name.setter
    def employee_name(self, employee_name):
        self._employee_name = employee_name

    @property
    def employee_last_name(self):
        return self._employee_last_name

    @employee_last_name.setter
    def employee_last_name(self, employee_last_name):
        self._employee_last_name = employee_last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def employee_password(self):
        return self._employee_password

    @employee_password.setter
    def employee_password(self, employee_password):
        self._employee_password = employee_password

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    conexion = Conexion(host='localhost', port=3306, user='root', password="root_password", database='TiendaJPBB')

    @staticmethod
    def from_row(row):
        return Employee(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    def create_employee(self, db):
        self._employee_id = int(input("ID del empleado: "))
        self._employee_name = input("Nombre del empleado: ")
        self._employee_last_name = input("Apellido del empleado: ")
        self._email = input("Correo electrónico del empleado: ")
        self._employee_password = input("Contraseña del empleado: ")
        self._salary = float(input("Salario del empleado: "))
        self._position = input("Posición del empleado: ")

        query = "INSERT INTO employee (employee_id, employee_name, employee_last_name, email, employee_password, salary, position) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (self._employee_id, self._employee_name, self._employee_last_name, self._email, self._employee_password, self._salary, self._position)
        db.execute_query(query, params)

    def select_employee(self, db):
        query = "SELECT * FROM employee"
        result = db.execute_query(query)
        if result:
            employees = []
            for row in result:
                employee = Employee.from_row(row)
                employees.append(employee)
                print(f"ID: {row[0]}, Nombre: {row[1]}, Apellido: {row[2]}, Email: {row[3]}, Salario: {row[5]}, Posición: {row[6]}")
            return employees
        else:
            print("Empleados no encontrados")
            return []

    def delete_employee(self, db, employee_id):
        query = "DELETE FROM employee WHERE employee_id = %s"
        db.execute_query(query, (employee_id,))

    def update_employee(self, db):
        # Solicita el ID del empleado a actualizar
        employee_id = int(input("Ingrese el ID del empleado que desea actualizar: "))
        # Solicita los nuevos valores
        new_employee_name = input("Ingrese el nuevo nombre del empleado: ")
        new_employee_last_name = input("Ingrese el nuevo apellido del empleado: ")
        new_email = input("Ingrese el nuevo correo electrónico del empleado: ")
        new_employee_password = input("Ingrese la nueva contraseña del empleado: ")
        new_salary = float(input("Ingrese el nuevo salario del empleado: "))
        new_position = input("Ingrese la nueva posición del empleado: ")

        # Consulta para actualizar el empleado
        query = "UPDATE employee SET employee_name = %s, employee_last_name = %s, email = %s, employee_password = %s, salary = %s, position = %s WHERE employee_id = %s"
        params = (new_employee_name, new_employee_last_name, new_email, new_employee_password, new_salary, new_position, employee_id)
        
        # Ejecuta la consulta
        db.execute_query(query, params)
        print(f"Empleado con ID {employee_id} actualizado.")
