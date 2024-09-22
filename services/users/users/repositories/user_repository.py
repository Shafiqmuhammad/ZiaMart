from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from users.models.user import User

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user: User):
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_user(self, user_id: int):
        result = await self.session.execute(select(User).filter_by(id=user_id))
        return result.scalars().first()
