from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
#giá trị mặc định vẫn là None, vì vậy tham số vẫn là tùy chọn.
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    #xác thực bổ sung cho giá trị này(50 kí tự)
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
# FastAPI bây giờ sẽ:

# Xác thực dữ liệu để đảm bảo độ dài tối đa là 50 ký tự

# Hiển thị lỗi rõ ràng cho khách hàng khi dữ liệu không hợp lệ

# Ghi lại tham số trong hoạt động đường dẫn lược đồ OpenAPI
# (để nó sẽ hiển thị trong automatic docs UI)