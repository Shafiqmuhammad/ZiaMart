from sqlalchemy.ext.asyncio import AsyncSession
from users.repositories.user_repository import UserRepository
from users.protobuf.user_pb2 import User, UserCreatedEvent
from users.events.user_events import UserEvents

class UserService:
    def __init__(self, session: AsyncSession):
        self.repo = UserRepository(session)
        self.events = UserEvents()

    async def create_user(self, user_data):
        new_user = User(name=user_data.name, email=user_data.email)
        user = await self.repo.create_user(new_user)
        user_event = User(id=user.id, name=user.name, email=user.email)
        self.events.produce_user_created_event(user_event)
        return user

    async def get_user(self, user_id: int):
        return await self.repo.get_user(user_id)
