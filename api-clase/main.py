from fastapi import FastAPI, Body
from modelos.Category import Category
from conexionDB.Conexion import Conexion

app =FastAPI()

@app.get('/')
def read_root():
    return{
        "message":"Hola mundo"
    }

host = 'localhost'
port = 3306
user = 'root'
password = 'root_password'  # Asegúrate de que esta contraseña sea la correcta
database = 'TiendaJPBB'

db = Conexion(host, port, user, password, database)
db.connect_db()

@app.post('/create_category/', tags=["Category"])
def create_category(category_name: str=Body()):
    new_category = Category(None,None)
    return new_category.create_category(db,category_name)

@app.get('/categories', tags=["Category"])
def get_categories():
    categories = Category(None,None)
    return categories.get_category(db)
