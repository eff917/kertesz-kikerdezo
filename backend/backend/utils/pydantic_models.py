from typing import List, Optional

from pydantic import BaseModel

class PictureBase(BaseModel):
    path: str

class PictureCreate(PictureBase):
    pass

class Picture(PictureBase):
    id: int
    plant_id: int
    pass

class TestListBase(BaseModel):
    name: str
    pass

class TestListCreate(TestListBase):
    pass

class TestList(TestListBase):
    id: int
    plants: List["Plant"]
    pass

class PlantBase(BaseModel):
    latin_name: str
    hungarian_name: str

class PlantCreate(PlantBase):
    pass

class Plant(PlantBase):
    id: int
    pictures: Optional[List[Picture]] = None
    lists: Optional[List[TestList]] = None

    class Config:
        orm_mode: True