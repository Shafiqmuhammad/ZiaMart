from users import settings
from sqlmodel import SQLModel, create_engine # type: ignore
import psycopg
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession


# Database setup
connection_string = str(settings.DATABASE_URL).replace("postgresql", "postgresql+psycopg")

#  Creating Engine 
engine = create_engine(connection_string, pool_recycle=300, pool_size=10, echo=True)


# Create async session factory
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
#  Function to create tables 
def create_table():
    SQLModel.metadata.create_all(engine)