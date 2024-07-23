# Khi không cần khai báo thêm xác thực hoặc metadata,
# có thể yêu cầu tham số query q chỉ bằng cách không khai báo giá trị mặc định, như:
#
# q: str
#
# thay vì:
#
# q: Union[str, None] = None
# 
# Nhưng hiện tại, đang khai báo nó bằng Query, ví dụ như:
#
# Annotated
# q: Annotated[Union[str, None], Query(min_length=3)] = None
#
# non-Annotated
# q: Union[str, None] = Query(default=None, min_length=3)
#
# Vì vậy, khi cần khai báo một giá trị theo yêu cầu trong khi sử dụng Query,
# có thể không khai báo giá trị mặc định:


from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results