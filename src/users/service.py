from beanie import PydanticObjectId

from auth.service import get_password, verify_password
from users.models import User
from users.schemas import UserAuth


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=get_password(user.password)
        )
        await user_in.save()
        return user_in

    @staticmethod
    async def authenticate(email: str, password: str) -> User | None:
        user = await UserService.get_user_by_email(email)
        if not user:
            return None
        if not verify_password(password=password, hashed_pass=user.hashed_password):
            return None
        return user

    @staticmethod
    async def get_user_by_email(email: str) -> User | None:
        user = await User.find_one(User.email == email)
        return user

    @staticmethod
    async def get_user_by_id(id: PydanticObjectId) -> User | None:
        user = await User.find_one(User.id == id)
        return user
