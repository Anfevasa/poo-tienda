# modelos/Product.py

from conexionDB.Conexion import Conexion

class Product:
    product_id = None
    product_name = None
    description = None
    category_id = None
    price = None
    quantity = None
    brand = None

    def __init__(self, product_id, product_name, description, category_id, price, quantity, brand):
        self._product_id = product_id
        self._product_name = product_name
        self._description = description
        self._category_id = category_id
        self._price = price
        self._quantity = quantity
        self._brand = brand

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        self._product_name = product_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        self._category_id = category_id

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
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    conexion = Conexion(host='localhost', port=3306, user='root', password="root_password", database='TiendaJPBB')

    @staticmethod
    def from_row(row):
        return Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    def create_product(self, db):
        self._product_id = int(input("ID del producto: "))
        self._product_name = input("Nombre del producto: ")
        self._description = input("Descripción del producto: ")
        self._category_id = int(input("ID de la categoría: "))
        self._price = float(input("Precio del producto: "))
        self._quantity = int(input("Cantidad del producto: "))
        self._brand = input("Marca del producto: ")

        query = "INSERT INTO product (product_id, product_name, description, category_id, price, quantity, brand) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (self._product_id, self._product_name, self._description, self._category_id, self._price, self._quantity, self._brand)
        db.execute_query(query, params)

    def select_product(self, db):
        query = "SELECT * FROM product"
        result = db.execute_query(query)
        if result:
            products = []
            for row in result:
                product = Product.from_row(row)
                products.append(product)
                print(f"ID: {row[0]}, Nombre: {row[1]}, Descripción: {row[2]}, Categoría ID: {row[3]}, Precio: {row[4]}, Cantidad: {row[5]}, Marca: {row[6]}")
            return products
        else:
            print("Productos no encontrados")
            return []

    def delete_product(self, db, product_id):
        query = "DELETE FROM product WHERE product_id = %s"
        db.execute_query(query, (product_id,))

    def update_product(self, db):
        # Solicita el ID del producto a actualizar
        product_id = int(input("Ingrese el ID del producto que desea actualizar: "))
        # Solicita los nuevos valores
        new_product_name = input("Ingrese el nuevo nombre del producto: ")
        new_description = input("Ingrese la nueva descripción del producto: ")
        new_category_id = int(input("Ingrese el nuevo ID de la categoría: "))
        new_price = float(input("Ingrese el nuevo precio del producto: "))
        new_quantity = int(input("Ingrese la nueva cantidad del producto: "))
        new_brand = input("Ingrese la nueva marca del producto: ")

        # Consulta para actualizar el producto
        query = "UPDATE product SET product_name = %s, description = %s, category_id = %s, price = %s, quantity = %s, brand = %s WHERE product_id = %s"
        params = (new_product_name, new_description, new_category_id, new_price, new_quantity, new_brand, product_id)
        
        # Ejecuta la consulta
        db.execute_query(query, params)
        print(f"Producto con ID {product_id} actualizado.")
