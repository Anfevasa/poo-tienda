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


    def create_category(self, db, category_name):
        query = "INSERT INTO category( category_name)VALUES(%s) "
        params = (category_name,)
        return db.execute_query(query, params)

    @staticmethod
    def get_category(db):
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

    @staticmethod
    def delete_category( db , category_id):
        query = "DELETE FROM category WHERE category_id = %s"
        db.execute_query(query, (category_id,))

    @staticmethod
    def update_category(db, category_id,category_name):
        # Consulta para actualizar la categoría
        query = "UPDATE category SET category_name = %s WHERE category_id = %s"
        params = (category_name, category_id)
        
        # Ejecuta la consulta
        db.execute_query(query, params)
        print(f"Categoría con ID {category_id} actualizada a {category_name}.")

