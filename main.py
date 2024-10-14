from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/inicio")
def read_root():
    return {"Hi there,": "you're seen this NOW!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# parametros de ruta
@app.get("/parametros/{nombre}")
def get_parametros(nombre):
    return {
        "Nombre" : nombre
    }

@app.get("/secretplace/{nombre}")
def get_secretuser(nombre):
    return {
        "Wuola, que hay?," : nombre
    }

@app.get("/incremento/{num}")
def get_incremento(num:int and float):
    num = num + 1
    return {
        "Resultado" : num
    }


# Suma de dos números usando parámetros de query ---/suma?num1=5.5&num2=4.2---
@app.get("/suma")
def sumar(num1: float, num2: float):
    resultado = num1 + num2
    return {
        "Suma": resultado
    }
