from . import db_models
import logging
LOGGER = logging.getLogger()

def clear_all_tables(session):
    for plant in session.query(db_models.Plant):
        session.delete(plant)
    for list in session.query(db_models.TestList):
        session.delete(list)
    for picture in session.query(db_models.Picture):
        session.delete(picture)
    session.commit()

def load_example_data(session):
    # create plant objects
    plant1 = db_models.Plant(latin_name="latinname1", hungarian_name="hunname1")
    plant2 = db_models.Plant(latin_name="latinname2", hungarian_name="hunname2")
    plant3 = db_models.Plant(latin_name="latinname3", hungarian_name="hunname3")
    plant4 = db_models.Plant(latin_name="latinname4", hungarian_name="hunname4")
    plant5 = db_models.Plant(latin_name="latinname5", hungarian_name="hunname5")
    plant6 = db_models.Plant(latin_name="latinname6", hungarian_name="hunname6")
    plant7 = db_models.Plant(latin_name="latinname7", hungarian_name="hunname7")
    plant8 = db_models.Plant(latin_name="latinname8", hungarian_name="hunname8")
    # add plants to session
    session.add(plant1)
    session.add(plant2)
    session.add(plant3)
    session.add(plant4)
    session.add(plant5)
    session.add(plant6)
    session.add(plant7)
    session.add(plant8)

    # save plants to db
    session.commit()

    # create picture objects
    pic11 = db_models.Picture(path='/images/plant11', plant_id=1)
    pic12 = db_models.Picture(path='/images/plant12', plant_id=1)
    pic21 = db_models.Picture(path='/images/plant21', plant_id=2)
    pic22 = db_models.Picture(path='/images/plant22', plant_id=2)
    pic31 = db_models.Picture(path='/images/plant31', plant_id=3)
    pic41 = db_models.Picture(path='/images/plant41', plant_id=4)
    pic51 = db_models.Picture(path='/images/plant51', plant_id=5)
    pic52 = db_models.Picture(path='/images/plant52', plant_id=5)

    # add pictures to session
    session.add(pic11)
    session.add(pic12)
    session.add(pic21)
    session.add(pic22)
    session.add(pic31)
    session.add(pic41)
    session.add(pic51)
    session.add(pic52)

    # save pictures to db
    session.commit()

    # create list objects
    kaszab = db_models.TestList(name='kaszab')
    all = db_models.TestList(name='all')

    # add lists to session
    session.add(kaszab)
    session.add(all)
    # save lists to db
    session.commit()

    # add all plant objects to the list named "all"
    for plant in session.query(db_models.Plant):
        plant.lists.append(all)
        session.add(plant)
        session.commit()

    # add some plants to the list "kaszab"
    kaszab.plants.append(plant1)
    kaszab.plants.append(plant2)
    session.add(kaszab)
    session.commit()