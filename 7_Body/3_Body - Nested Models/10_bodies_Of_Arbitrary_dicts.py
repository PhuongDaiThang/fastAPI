# Bạn cũng có thể khai báo phần thân dưới dạng
# một lệnh với các khóa thuộc một số loại và các giá trị thuộc một số loại khác.

from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights