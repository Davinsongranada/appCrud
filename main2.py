from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import get_db_connection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
conn = get_db_connection()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class productBase(BaseModel):
    id: int
    name: str
    img: str

@app.get("/products")
async def get_users():
    bus = input("Busque algo: ")
    print(bus)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE title LIKE ?", ('%' + bus + '%'))
    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]

    result = []
    for row in rows:
        result.append({column_names[i]: row[i] for i in range(len(row))})
    print(result)



