from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)
base = declarative_base()


class ItemDB(base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String(350))
    type = Column(String(350))
    director = Column(String(350))
    number_of_votes = Column(Integer)
    average_grade = Column(Float)
    sum_grade = Column(Float)
    url = Column(String(400))

    def __init__(self, id, name, type, director, number_of_votes, average_grade, sum_grade, url):
        self.id = id
        self.name = name
        self.type = type
        self.director = director
        self.number_of_votes = number_of_votes
        self.average_grade = average_grade
        self.sum_grade = sum_grade
        self.url = url


def getLasID():
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(ItemDB).all()
    return res[-1].id

if __name__ == '__main__':
    type = "movie"
    print(type)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(ItemDB).filter(ItemDB.type == type)
    for item in res:
        print(item.type)
