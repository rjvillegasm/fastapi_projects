from fastapi import FastAPI

app= FastAPI()

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


 