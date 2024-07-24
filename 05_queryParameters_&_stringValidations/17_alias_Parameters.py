# Hãy tưởng tượng rằng bạn muốn tham số là item-query:
#
# Giống như trong:
#
# http://127.0.0.1:8000/items/?item-query=foobaritems
#
# Nhưng item-query không phải là tên biến Python hợp lệ.
#
# Gần nhất sẽ là item_query.
#
# Nhưng bạn vẫn cần nó chính xác là item-query...
# 
# Sau đó, bạn có thể khai báo một alias và alias đó sẽ được sử dụng để tìm giá trị tham số:

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results