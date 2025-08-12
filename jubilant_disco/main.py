from fastapi import FastAPI
from sqlmodel import Session, SQLModel, create_engine, select
from jubilant_disco.tables import *

def main() -> None:

    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

    def create_db_and_tables():
        SQLModel.metadata.create_all(engine)

    app = FastAPI()

    @app.on_event("startup")
    def on_startup():
        create_db_and_tables()

""" 
    @app.post("/person/", response_model=BaseTable)
    def create_person(person: PersonCreate):
        with Session(engine) as session:
            db_people = Person.model_validate(person)
            session.add(db_people)
            session.commit()
            session.refresh(db_people)
            return db_people

    @app.get("/people/", response_model=list[BaseTable])
    def read_heroes():
        with Session(engine) as session:
            people = session.exec(select(Person)).all()
            return people
 """

if __name__ == "__main__":
    main()
