from conexionDB.Conexion import Conexion

class Category:
    category_id = None
    category_name = None

    def __init__(self, category_id, category_name):
        self._category_id = category_id
        self._category_name = category_name

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        self._category_id = category_id

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        self._category_name = category_name

    @staticmethod
    def from_row(row):
        return Category(row[0], row[1])



    def create_category(self, db):
        self._category_id = int(input("id"))
        self._category_name = input("Nombre categoria")
        query = "INSERT INTO category(category_id , category_name)VALUES(%s,%s) "
        params = (self._category_id , self._category_name)
        db.execute_query(query, params)

    def select_category(self, db):
        query = "SELECT * FROM category"
        result = db.execute_query(query)
        if result:
            categories = []
            for row in result:
                category = Category.from_row(row)
                categories.append(category)
                print(row[0], row[1])
            return categories
        else:
            print("Categorias no encontradas")
            return []


    def delete_category(self, db , category_id):
        query = "DELETE FROM category WHERE category_id = %s"
        db.execute_query(query, (category_id,))

    def update_category(self, db):
        # Solicita el ID de la categoría a actualizar
        category_id = int(input("Ingrese el ID de la categoría que desea actualizar: "))
        # Solicita los nuevos valores
        new_category_name = input("Ingrese el nuevo nombre de la categoría: ")

        # Consulta para actualizar la categoría
        query = "UPDATE category SET category_name = %s WHERE category_id = %s"
        params = (new_category_name, category_id)
        
        # Ejecuta la consulta
        db.execute_query(query, params)
        print(f"Categoría con ID {category_id} actualizada a {new_category_name}.")

