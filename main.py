from ctypes.wintypes import tagSIZE
from fastapi import FastAPI, HTTPException, Query, status, Response
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
    img: str
    

"""
print(producto.__dict__) 
All the attributes for Class/instance level
"""
    
    


# @APP.GET
@app.get("/productos", tags=["CRUD"])
async def getDate(Search:str = "", PageSize:int = Query(0), Page:int = Query(0)):
    conn = get_db_connection()
    cursor = conn.cursor()
    offset = (Page-1)*PageSize
    cursor.execute(f"SELECT * FROM productos WHERE title LIKE ? ORDER BY id LIMIT {PageSize} OFFSET {offset}", ['%' + Search + '%'])
    if not Page or not PageSize:
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
    
    respuesta = jsonable_encoder(result)
    return JSONResponse(content = respuesta)




# @APP.POST
@app.post("/productos", tags=["CRUD"])
def createProduct(producto: producto):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO productos(title, price, images) VALUES (?,?,?)',(producto.title, producto.price, producto.img))
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

    updateData = "UPDATE productos SET title=?, price=?, images=? WHERE id=?"
    cursor.execute(updateData, (producto.title, producto.price, producto.img, id))
    conn.commit()
    respuesta = jsonable_encoder(producto)
    return JSONResponse(content = respuesta)


@app.delete("/productos/{id}", tags=["CRUD"])
def deleteProduct(id:int, response:Response):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", [id])
    resultados = cursor.fetchone()

    if not resultados:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="El id no existe")

    cursor.execute("DELETE FROM productos WHERE id = ?", [id])
    conn.commit()
    return HTTPException(status.HTTP_200_OK)
    
    









