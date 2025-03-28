from fastapi import FastAPI, HTTPException, status
from starlette import status
from typing import List

from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    return db.get_sheep(id)

@app.get("/sheep", response_model=List[Sheep])
def get_all_sheep():
    return db.get_all_sheep()

@app.post("/sheep", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")

    db.data[sheep.id] = sheep
    return sheep

@app.put("/sheep/{sheep_id}")
def update_sheep(sheep_id: int, updated_data: dict):
    updated_sheep = db.update_sheep(sheep_id, updated_data)
    if not updated_sheep:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return updated_sheep

@app.delete("/sheep/{sheep_id}")
def delete_sheep(sheep_id: int):
    deleted = db.delete_sheep(sheep_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return {"message": "Sheep deleted successfully"}