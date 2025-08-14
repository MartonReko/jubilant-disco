from sqlmodel import SQLModel, Session, create_engine, select
from jubilant_disco.tables import (
    Actor,
    Good,
    PersonCreate,
    RecipeItem,
    Recipe,
    Occupation,
    Person,
    Workplace,
    Product,
)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


with Session(engine) as session:
    goods: dict[str, Good] = {
        "wheat": Good(name="wheat"),
        "bread": Good(name="bread"),
    }
    session.add_all(goods)
    session.commit()
    session.refresh(goods)

    recipes: dict[str, Recipe] = {"bread": Recipe(name="bread")}
    session.add_all(goods)
    session.commit()
    session.refresh(recipes)

    bread_recipe: list[RecipeItem] = [
        RecipeItem(
            good=goods["wheat"],
            recipe=recipes["bread"],
        ),
        RecipeItem(
            good=goods["bread"], recipe=recipes["bread"], type=RecipeItem.Type.OUTPUT
        ),
    ]
    session.add_all(bread_recipe)
    session.commit()
    session.refresh(bread_recipe)

    workplaces: dict[str, Workplace] = {
        "bread factory": Workplace(name="bread factory", recipe=recipes["bread"])
    }
    session.add_all(workplaces)
    session.commit()
    session.refresh(workplaces)

    people: list[Person] = [
        Person() for i in range(0, 10)
    ]
    session.add_all(people)
    session.commit()
    session.refresh(people)
    
    occupations: list[Occupation] = [
        Occupation(person=p, workplace=workplaces["bread factory"]) for p in people
    ]
