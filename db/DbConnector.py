from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db.BaseModel import Base
from sqlalchemy import URL, select, delete, update

url_object = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="password",  # plain (unescaped) text
    host="localhost",
    database="postgres",
)


def insert_all(data):  # он принимает коллекцию тех моделей, кот-ые надо вставить в бд.
    with Session(engine) as session:  # здесь будет происходить коннект
        session.add_all(data)
        session.commit()


def init_engine():  # здесь мы подключаемся к бд
    engine = create_engine(url_object)
    Base.metadata.create_all(engine)
    return engine


def select_all(table):
    with Session(engine) as session:  # подключаемся к бд
        stmt = select(table)
        return [_ for _ in session.scalars(stmt)]


def delete_all(table):
    with Session(engine) as session:
        stmt = delete(table).where(table.name == "patrick")
        session.execute(stmt)
        session.commit()


def update_table(table):
    with Session(engine) as session:
        stmt = update(table).where(table.name == "sandy").values(fullname="sandy_changed")
        session.execute(stmt)
        session.commit()


engine = init_engine()
