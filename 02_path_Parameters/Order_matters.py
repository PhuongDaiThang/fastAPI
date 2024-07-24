#Khi tạo các thao tác đường dẫn, bạn có thể gặp các tình huống mà bạn có đường dẫn cố định.

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

#EXAMPLE: Cái đầu tiên sẽ luôn được sử dụng vì đường dẫn khớp trước.
from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]
