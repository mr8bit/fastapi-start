from fastapi import Request
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from src.app.users.models import UserDB, user_db, User, UserCreate, UserUpdate
from src.config.settings import SECRET_KEY
from fastapi import APIRouter


def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")


def on_after_forgot_password(user: UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")


jwt_authentication = JWTAuthentication(
    secret=SECRET_KEY, lifetime_seconds=3600, tokenUrl="/auth/jwt/login"
)

fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

fastapi_auth = APIRouter()

fastapi_auth.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt"
)
fastapi_auth.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth"
)
fastapi_auth.include_router(
    fastapi_users.get_reset_password_router(
        SECRET_KEY, after_forgot_password=on_after_forgot_password
    ),
    prefix="/auth",
)

fastapi_auth.include_router(fastapi_users.get_users_router(), prefix="/users")
