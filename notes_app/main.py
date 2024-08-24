from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from notes_app.auth.auth import auth_backend
from notes_app.auth.schemas import UserRead, UserCreate
from notes_app.database import User
from notes_app.auth.manager import get_user_manager


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

@app.get("/notes/{user_id}")
def get_records(user_id: int):
    # query = select(Note).where(Note.user_id == user_id)

    return



@app.get("/")
def main_page():
    return {"Hello": "World"}



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