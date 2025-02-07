from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import get_db_connection
from fastapi.middleware.cors import CORSMiddleware

busqueda = input("Busque uno de estos productos, colchon, iPhone 13 y Mac mini M4 Pro: ")

