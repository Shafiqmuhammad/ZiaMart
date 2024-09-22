from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from users.config.settings import settings
from users.routes import user_routes
from services.users.users.consumer.kafka_utils import get_kafka_consumer

app = FastAPI()

DATABASE_URL = f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}/{settings.postgres_db}"

# Create the database engine and session
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

consumer = None

@app.on_event("startup")
async def startup_event():
    global consumer
    consumer = get_kafka_consumer(group_id="user-group", topics=["user-topic"])

@app.on_event("shutdown")
async def shutdown_event():
    if consumer:
        consumer.close()

app.include_router(user_routes.router)
