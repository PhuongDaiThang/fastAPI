from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
#khi bạn muốn tạo một tham số truy vấn bắt buộc, bạn không thể khai báo bất kỳ giá trị mặc định nào
#Ở đây tham số truy vấn needylà tham số truy vấn bắt buộc có kiểu str.