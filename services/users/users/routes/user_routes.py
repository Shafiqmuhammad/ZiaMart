from fastapi import APIRouter, Depends
from users.services.user_service import UserService
from users.models.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/users", response_model=UserResponse)
async def create_user(user_data: UserCreate, service: UserService = Depends()):
    return await service.create_user(user_data)

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, service: UserService = Depends()):
    return await service.get_user(user_id)
