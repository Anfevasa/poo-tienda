import mysql.connector

class Conexion:
    _instance = None

    def __new__(cls, host, port, user, password, database):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize(host, port, user, password, database)
        return cls._instance

    def _initialize(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect_db(self):
        if self.connection is None or not self.connection.is_connected():
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
                print("Conexión Exitosa")
            except mysql.connector.Error as err:
                print("La conexión ha fallado", err)

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión Cerrada")

    def execute_query(self, query, params=None):
        if self.connection is None or not self.connection.is_connected():
            print("La conexión no está establecida.")
            return None

        cursor = self.connection.cursor(buffered=True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Consulta exitosa")
            if "select" in query.lower():
                result = cursor.fetchall()
                return result
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta", err)
            return None
        finally:
            cursor.close()
