from pydantic import BaseSettings

class Settings(BaseSettings):
    postgres_user: str = "postgres"
    postgres_password: str = "password"
    postgres_db: str = "users_db"
    postgres_host: str = "postgres"   # Docker Compose service name
    postgres_port: int = 5432
    kafka_bootstrap_servers: str = "kafka:9092"  # Kafka service

    class Config:
        env_file = ".env"

settings = Settings()
