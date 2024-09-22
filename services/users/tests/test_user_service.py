import pytest
from app.services.user_service import UserService
from app.models.user import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession

@pytest.mark.asyncio
async def test_create_user(session: AsyncSession):
    user_service = UserService(session)
    user_data = UserCreate(name="John Doe", email="john.doe@example.com")
    created_user = await user_service.create_user(user_data)
    assert created_user.name == "John Doe"
    assert created_user.email == "john.doe@example.com"

@pytest.mark.asyncio
async def test_get_user(session: AsyncSession):
    user_service = UserService(session)
    created_user = await user_service.get_user(1)
    assert created_user is not None
    assert created_user.id == 1
