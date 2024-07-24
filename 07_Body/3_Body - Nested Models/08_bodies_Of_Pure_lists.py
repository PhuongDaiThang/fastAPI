# Nếu giá trị cấp cao nhất của phần body JSON mà bạn mong đợi là một mảng JSON (danh sách Python),
# thì bạn có thể khai báo loại này trong tham số của hàm, giống như trong các models Pydantic:
images: List[Image]
images: list[Image] #Bản 3.9+
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images