from Conexion import Conexion

# Parámetros de conexión
host = 'localhost'
port = 3306
user = 'root'
password = 'root_password'
database = 'TiendaJPBB'

# Crear una instancia de la clase Conexion
conexion = Conexion(host, port, user, password, database)

# Conectar a la base de datos
conexion.connect_db()

# Ejecutar una consulta de prueba
query = "SELECT * FROM customer"
result = conexion.execute_query(query)

# Imprimir los resultados de la consulta
if result is not None:
    for row in result:
        print(row)

# Desconectar de la base de datos
conexion.disconnect()
