# modelos/Sales.py

from conexionDB.Conexion import Conexion

class Sales:
    sale_id = None
    sale_date = None
    customer_id = None
    product_id = None
    price = None
    quantity = None
    total = None
    employee_id = None

    def __init__(self, sale_id, sale_date, customer_id, product_id, price, quantity, total, employee_id):
        self._sale_id = sale_id
        self._sale_date = sale_date
        self._customer_id = customer_id
        self._product_id = product_id
        self._price = price
        self._quantity = quantity
        self._total = total
        self._employee_id = employee_id

    @property
    def sale_id(self):
        return self._sale_id

    @sale_id.setter
    def sale_id(self, sale_id):
        self._sale_id = sale_id

    @property
    def sale_date(self):
        return self._sale_date

    @sale_date.setter
    def sale_date(self, sale_date):
        self._sale_date = sale_date

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id = customer_id

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    conexion = Conexion(host='localhost', port=3306, user='root', password="root_password", database='TiendaJPBB')

    @staticmethod
    def from_row(row):
        return Sales(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

    def create_sale(self, db):
        self._sale_date = input("Fecha de la venta (YYYY-MM-DD HH:MM:SS): ")
        self._customer_id = int(input("ID del cliente: "))
        self._product_id = int(input("ID del producto: "))
        self._price = float(input("Precio del producto: "))
        self._quantity = int(input("Cantidad del producto: "))
        self._total = self._price * self._quantity
        self._employee_id = int(input("ID del empleado: "))

        query = "INSERT INTO sales (sale_date, customer_id, product_id, price, quantity, total, employee_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (self._sale_date, self._customer_id, self._product_id, self._price, self._quantity, self._total, self._employee_id)
        db.execute_query(query, params)

    def select_sales(self, db):
        query = "SELECT * FROM sales"
        result = db.execute_query(query)
        if result:
            sales = []
            for row in result:
                sale = Sales.from_row(row)
                sales.append(sale)
                print(f"ID: {row[0]}, Fecha: {row[1]}, Cliente ID: {row[2]}, Producto ID: {row[3]}, Precio: {row[4]}, Cantidad: {row[5]}, Total: {row[6]}, Empleado ID: {row[7]}")
            return sales
        else:
            print("Ventas no encontradas")
            return []

    def delete_sale(self, db, sale_id):
        query = "DELETE FROM sales WHERE sale_id = %s"
        db.execute_query(query, (sale_id,))

    def update_sale(self, db):
        # Solicita el ID de la venta a actualizar
        sale_id = int(input("Ingrese el ID de la venta que desea actualizar: "))
        # Solicita los nuevos valores
        new_sale_date = input("Ingrese la nueva fecha de la venta (YYYY-MM-DD HH:MM:SS): ")
        new_customer_id = int(input("Ingrese el nuevo ID del cliente: "))
        new_product_id = int(input("Ingrese el nuevo ID del producto: "))
        new_price = float(input("Ingrese el nuevo precio del producto: "))
        new_quantity = int(input("Ingrese la nueva cantidad del producto: "))
        new_total = new_price * new_quantity
        new_employee_id = int(input("Ingrese el nuevo ID del empleado: "))

        # Consulta para actualizar la venta
        query = "UPDATE sales SET sale_date = %s, customer_id = %s, product_id = %s, price = %s, quantity = %s, total = %s, employee_id = %s WHERE sale_id = %s"
        params = (new_sale_date, new_customer_id, new_product_id, new_price, new_quantity, new_total, new_employee_id, sale_id)
        
        # Ejecuta la consulta
        db.execute_query(query, params)
        print(f"Venta con ID {sale_id} actualizada.")
