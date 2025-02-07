from ctypes.wintypes import tagSIZE
import sqlite3
from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel
from db import get_db_connection
from fastapi.middleware.cors import CORSMiddleware
from http import HTTPStatus
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder



origins = ["*"]

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class producto(BaseModel):
    title: str
    price: float
    id: int

"""
print(producto.__dict__) 
All the attributes for Class/instance level
"""
    
    


# @APP.GET
@app.get("/productos", tags=["CRUD"])
async def getDate(search:str = "", page:int = Query(0), size:int = Query(0)):
    conn = get_db_connection()
    cursor = conn.cursor()
    offset = (page-1)*size
    cursor.execute(f"SELECT * FROM productos WHERE title LIKE ? ORDER BY id LIMIT {size} OFFSET {offset}", ['%' + search + '%'])
    if not page or not size:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, detail="LLene los datos"
        )
    elif offset - 0:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST
        )
    else:
        status.HTTP_200_OK
        
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]

    result = []
    for row in rows:
        result.append({column_names[i]: row[i] for i in range(len(row))})
    return result


# @APP.GET
@app.get("/productos/{id}", tags=["CRUD"])
async def getId(id:int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM productos WHERE id = ?", [id])
    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]

    result = []
    for row in rows:
        result.append({column_names[i]: row[i] for i in range(len(row))})

    if result:
        result
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = 'No se encontró el producto' )   




# @APP.POST
@app.post("/productos", tags=["CRUD"])
def createProduct(producto: producto):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO productos(title, price) VALUES (?,?)',(producto.title, producto.price))
    conn.commit()
    respuesta = jsonable_encoder(producto)
    return JSONResponse(content = respuesta)
    


# @APP.PUT
@app.put("/productos/{id}", tags=["CRUD"])
def editProduct(producto: producto, id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", [id])
    result = cursor.fetchone()

    if result is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="No se ha encontrado")

    updateData = "UPDATE productos SET title=?, price=? WHERE id=?"
    cursor.execute(updateData, (producto.title, producto.price, id))
    conn.commit()
    respuesta = jsonable_encoder(producto)
    return JSONResponse(content = respuesta)


@app.delete("/productos/{id}", tags=["CRUD"])
def deleteProduct(id:int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM productos WHERE id = ?", [id])
        cursor.fetchone()
        conn.commit()
        HTTPException(status.HTTP_200_OK, detail= "OK!")
    except:
        HTTPException(status.HTTP_404_NOT_FOUND, detail = "No hay producto con ese id")
    
    









