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

@app.get('/get_categories', tags=["Category"])
def get_categories(): 
    return Category(None,None).get_category(db)

@app.delete('/delete_category', tags=["Category"])
def delete_category(category_id: int=Body()):
    return Category(None,None).delete_category(db,category_id)

@app.put('/update_category', tags = ["Category"])
def update_category(category_id:int=Body(),category_name:str=Body()):
    return Category(None,None).update_category(db,category_id,category_name)  
