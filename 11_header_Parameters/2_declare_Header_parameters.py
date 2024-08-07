from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()

#Giá trị đầu tiên là giá trị mặc định,
#bạn có thể chuyển tất cả các tham số validation hoặc annotation
@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}