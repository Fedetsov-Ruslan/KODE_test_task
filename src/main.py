from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from src.auth.auth import auth_backend
from src.auth.schemas import UserRead, UserCreate
from src.auth.models import User
from src.auth.manager import get_user_manager
from src.notes.router import router as router_notes


app = FastAPI(
    title="Заметки"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(current_user: User = Depends(current_user)):
    return f'hello, {current_user.username}'

@app.get("/unprotected-route")
def unprotected_route():
    return f'hello, anonymous'

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
   router_notes,
)