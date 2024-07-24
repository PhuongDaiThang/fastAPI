from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
#sử dụng Query() làm giá trị mặc định của tham số hàm, đặt tham số max_length thành 50:
async def read_items(q: str | None = Query(default=None, max_length=50)):
    # đặt giá trị mặc định bằng tham số Query(default=None)
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
# phần quan trọng nhất để tạo một tham số tùy chọn là phần: =None hoặc = Query(default=None)
# Phần Union[str, None] cho phép trình soạn thảo của bạn cung cấp hỗ trợ tốt hơn
#Trường hợp tham số max_length áp dụng cho chuỗi:
q: Union[str, None] = Query(default=None, max_length=50)