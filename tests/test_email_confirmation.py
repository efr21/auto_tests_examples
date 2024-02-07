from db import DbConnector
from db.BaseModel import User, Address


def test_init_db():
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
        )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
            ],
        )
    patrick = User(name="patrick", fullname="Patrick Star")

    data = [spongebob, sandy, patrick]
    DbConnector.insert_all(data)
    DbConnector.delete_all(User)
    DbConnector.update_table(User)
    result = DbConnector.select_all(User)
    for e in result:
        print(e)
