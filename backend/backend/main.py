from os import path, stat
from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from typing import List
from pathlib import Path

import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker, joinedload
from utils import db_models
from utils import load_data

from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]


DATABASE_URL = "sqlite:///./data.sqlite"
engine = sqlalchemy.create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    future=True,
    echo=True
)
Session = sessionmaker(engine)
session = Session()
db_models.Base.metadata.create_all(engine)

main_app = FastAPI()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    load_data.clear_all_tables(session
    )
    load_data.load_example_data(session)
    



@app.on_event("shutdown")
async def shutdown():
    engine.dispose()

@app.get("/")
async def root():
    return "Hello World!"

### Manage plants ###
@app.get("/plants/{plant_id}")
async def get_plant(plant_id):
    if plant_id == "all":
        plant = session.query(db_models.Plant).options(joinedload(db_models.Plant.pictures)).all()
    else:
        plant = session.query(db_models.Plant).options(joinedload(db_models.Plant.pictures)).filter(db_models.Plant.id == plant_id).first()
    return plant

# Add new plant
@app.post("/plants")
async def add_plant(latinName: str  = Form(...), hungarianName: str  = Form(...), files: List[UploadFile] = File(...)):
    new_plant = session.query(db_models.Plant).filter(db_models.Plant.latin_name == latinName).first()
    if new_plant is not None:
        raise HTTPException(status_code=409, detail=f"{latinName} already exists!")
    new_plant = db_models.Plant(latin_name = latinName, hungarian_name = hungarianName)
    session.add(new_plant)
    session.commit()
    for file in files:
        if file.filename != '':
            contents = await file.read()
            Path("static/images").mkdir(parents=True, exist_ok=True)
            with open(f"/static/images/{file.filename}", "wb") as target:
                target.write(contents)
            new_picture = db_models.Picture(path = f"/static/images/{file.filename}", plant_id = new_plant.id)
            session.add(new_picture)
            session.commit()

    return RedirectResponse(f'/plants/{new_plant.id}')

@app.patch("/plants/{plant_id}", response_class=db_models.Plant)
async def update_plant(plant_id):
    # TODO modify plant with updated data
    plant_to_update = session.query(db_models.Plant).options(joinedload(db_models.Plant.pictures)).options(joinedload(db_models.Plant.lists)).filter(db_models.Plant.id == plant_id).first()
    if plant_to_update is None:
        raise HTTPException(status_code=404, detail="Plant not found!")
    pass

# Delete plant
@app.delete("/plants/{plant_id}")
async def delete_plant(plant_id):
    # TODO delete pictures
    plant_to_delete = session.query(db_models.Plant).options(joinedload(db_models.Plant.pictures)).options(joinedload(db_models.Plant.lists)).filter(db_models.Plant.id == plant_id).first()
    if plant_to_delete is not None:
        # TODO delete picture files
        session.delete(plant_to_delete)
        session.commit()
        return f"Plant {plant_id} deleted successfully."
    else:
        raise HTTPException(status_code=404, detail=f"The plant with id {plant_id} doesn't exist!")

### Manage lists ###
@app.get("/lists/{list_id}")
async def get_list(list_id):
    if list_id == "all":
        list = session.query(db_models.TestList).options(joinedload(db_models.TestList.plants)).all()
    else:
        list = session.query(db_models.TestList).options(joinedload(db_models.TestList.plants)).filter(db_models.TestList.id == list_id).first()
    return list

### Create new list
@app.post("/lists")
async def add_list(name: str  = Form(...), plants: str  = Form(...)):
    new_list = session.query(db_models.TestList).filter(db_models.TestList.name == name).first()
    if new_list is not None:
        raise HTTPException(status_code=409, detail=f"{name} already exists!")
    if plants is not None:
        plantlist = session.query(db_models.Plant).filter(db_models.Plant.id.in_(plants.split(','))).all()
        new_list = db_models.TestList(name=name, plants=plantlist)
    else:
        new_list = db_models.TestList(name=name)
    session.add(new_list)
    session.commit()

### Modify existing list
@app.patch("/lists/{list_id}")
async def update_list(list_id, list):
    list_to_update = session.query(db_models.TestList).filter(db_models.TestList.id == list_id).first()
    if list_to_update is not None:
        update_data = list.dict()
        if "name" in update_data.keys():
            list_to_update.name = update_data["name"]
        if "plants" in update_data.keys():
            list_to_update.plants = update_data["plants"]
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"TestList with id {list_id} not found!")

### Delete list
@app.delete("/lists/{list_id}")
async def delete_list(list_id):
    list_to_delete = session.query(db_models.TestList).filter(db_models.TestList.id == list_id).first()
    if list_to_delete is not None:
        session.delete(list_to_delete)
        session.commit()
        return f"TestList {list_id} deleted successfully."
    else:
        raise HTTPException(status_code=404, detail=f"TestList with id {list_id} doesn't exist!")
    
main_app.mount("/api", app)
main_app.mount("/static", StaticFiles(directory="static", check_dir=False), name="static")