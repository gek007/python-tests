"""SQLAlchemy example: one table — create DB, seed, write, read.

Run as a module (``python -m`` adds the working directory to ``sys.path``):

- From repo root: ``uv run --directory DB -m my_simple_db``
- From ``DB/``: ``uv run -m my_simple_db``

``uv run -m my_simple_db`` from the repo root alone will fail: ``my_simple_db``
lives under ``DB/``, so Python does not see it unless cwd is ``DB`` (or you use
``--directory DB``).
"""

from pathlib import Path

from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

DB_PATH = Path(__file__).resolve().parent / "app.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    sku: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)


def seed_products(session) -> None:
    if session.scalar(select(Product).limit(1)) is not None:
        return
    session.add_all(
        [
            Product(name="Notebook", sku="NB-001"),
            Product(name="Pen", sku="PN-002"),
            Product(name="Stapler", sku="ST-003"),
        ]
    )
    session.commit()


def write_product(session, name: str, sku: str) -> Product:
    product = Product(name=name, sku=sku)
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def read_products(session) -> list[Product]:
    return list(session.scalars(select(Product).order_by(Product.id)))


def main() -> None:
    # The engine in SQLAlchemy is the starting point for any SQL database application.
    # It manages the database connection pool and acts as the interface to the actual database.
    engine = create_engine(DATABASE_URL, echo=False)
    # At this point, the database file (if it didn't exist) has *not* yet been created.
    # The database file gets created when the first actual connection or operation is made,
    # such as by calling Base.metadata.create_all(engine) below.

    # We use Base.metadata.create_all(engine) to create the tables in the database (if they do not already exist)
    # based on the models (like Product) defined with SQLAlchemy's Declarative system.
    Base.metadata.create_all(engine)

    # A session in SQLAlchemy handles conversations with the database. It's where we do all the CRUD (create, read,
    # update, delete) operations. We use sessionmaker to generate a Session class bound to our engine. Then,
    # we instantiate a session when we need to interact with the database.
    Session = sessionmaker(bind=engine)

    with Session() as session:
        seed_products(session)

    with Session() as session:
        if session.scalar(select(Product).where(Product.sku == "HL-004")) is None:
            write_product(session, name="Highlighter", sku="HL-004")

    with Session() as session:
        for row in read_products(session):
            print(f"{row.id}\t{row.sku}\t{row.name}")

    print(f"Database: {DB_PATH}")


if __name__ == "__main__":
    main()
