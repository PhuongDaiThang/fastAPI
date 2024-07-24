from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()

#Giá trị đầu tiên là giá trị mặc định,
#bạn có thể chuyển tất cả các tham số validation hoặc annotation
@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}