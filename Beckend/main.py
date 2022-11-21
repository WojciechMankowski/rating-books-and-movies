from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Database import base, ItemDB, getLasID
from Item import Item
from TypeItem import TypeItem

app = FastAPI()
engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)


@app.get("/")
def getItems():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(ItemDB).all()
@app.get("/type/{type}")
def getItemForType(type: str):
    print(type)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(ItemDB).filter(ItemDB.type == type)

@app.post("/add")
def addItem(item: Item):
    Session = sessionmaker(bind=engine)
    session = Session()
    if item.type == TypeItem.BOOK:
        type = TypeItem.BOOK.value
    elif item.type == TypeItem.MOVIE:
        type = TypeItem.MOVIE.value
    else:
        type = ""
    id = getLasID() + 1
    itemDB = ItemDB(id=id, name=item.nameItem, type=type,
                    director=item.director, number_of_votes=item.number_of_votes,
                    average_grade=item.average_grade, sum_grade=
                    item.sum_grade, url=item.url
                    )
    session.add(itemDB)
    session.commit()
    return {'code': 200}
