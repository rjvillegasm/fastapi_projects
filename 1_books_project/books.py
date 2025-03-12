from fastapi import FastAPI

app= FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
    ]


@app.get("/api-endpoint")
# @app.get: es un decorador, al cual le asignamos un endpoint
async def first_api():
    return {'mesage': 'Hola mundo'}

# método 'async' se refiere a funciones asíncronas
# la app se iniciará en http://127.0.0.1:8000/api-endpoint

# en la terminal muestra el comando uvicorn books:app --reload
# donde uvicorn es un web server utilizado por fastapi
# y books es el nombre de nuestro archivo
# el comadno --reload permite refrescar el server cada vez que realizamos un cambio
# tambien se puede utulizar 'fastapi run main.py'
# run se puede reemplazar por dev

@app.get('/books')
async def real_all_books():
    return BOOKS
 
 
# path parameters:
# son request parameters que son anexados a la URL 
# y sirven como arguento de la función creada

# parametro estático
@app.get("/mybooks/myfav")
async def read_my_fav():
    return {'book_title': '100 años de soledad' }

#parametro dinámico
@app.get("/mybooks/{dynamic_param}")
async def read_my_books(dynamic_param):
    return {'dynamic_param': dynamic_param }


 