import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.schema import Column, ForeignKey, Table

Base = declarative_base()

lists_plants = Table(
    'list_plants',
    Base.metadata,
    Column('list_id', ForeignKey('lists.id'), primary_key=True),
    Column('plant_id', ForeignKey('plants.id'), primary_key=True)
)

class Plant(Base):
    __tablename__ = "plants"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    latin_name = sqlalchemy.Column(sqlalchemy.String(50), unique=True, nullable=False)
    hungarian_name = sqlalchemy.Column(sqlalchemy.String(50), nullable=False)
    pictures = relationship("Picture", back_populates="plant", cascade="all, delete")
    lists = relationship(
        "TestList",
        secondary=lists_plants,
        back_populates='plants'
    )

    def __repr__(self) -> str:
        return "<Plant(latin_name:'%s', hungarian_name:'%s')>" % (self.latin_name, self.hungarian_name)

class Picture(Base):
    __tablename__ = "pictures"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    path = sqlalchemy.Column(sqlalchemy.String, unique=True)
    plant_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('plants.id'))
    plant = relationship(
        "Plant", 
        back_populates="pictures"
    )

    def __repr__(self) -> str:
        return "<Picture(path:'%s', plant_id:'%s')>" % (self.path, self.plant_id)

class TestList(Base):
    __tablename__ = "lists"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(50))
    plants = relationship(
        "Plant",
        secondary=lists_plants,
        back_populates="lists"
    )

    def __repr__(self) -> str:
        return "<TestList(name:'%s')>" % (self.name)
