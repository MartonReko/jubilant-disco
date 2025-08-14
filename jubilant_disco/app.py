
from fastapi import FastAPI
from sqlmodel import Session, select

from jubilant_disco.db import create_db_and_tables, engine
from jubilant_disco.tables import Person, PersonCreate


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/person/", response_model=Person)
def create_person(person: PersonCreate):
    with Session(engine) as session:
        db_people = Person.model_validate(person)
        session.add(db_people)
        session.commit()
        session.refresh(db_people)
        return db_people


@app.get("/people/", response_model=list[Person])
def read_heroes():
    with Session(engine) as session:
        people = session.exec(select(Person)).all()
        return people
