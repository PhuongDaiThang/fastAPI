#Khai báo đường dẫn "parameters" hoặc "variables" với cú pháp tương tự Python:
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}
