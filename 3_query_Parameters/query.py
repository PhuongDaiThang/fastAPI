#Khai báo các tham số hàm khác, không phải là một phần của tham số đường dẫn thì
# chúng sẽ tự động được hiểu là tham số "truy vấn".là tập hợp các cặp khóa-giá trị theo sau dấu ? trong URL,
# được phân tách bằng ki tu &.

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

#Vi du, trong URL:
#http://127.0.0.1:8000/items/?skip=0&limit=10
