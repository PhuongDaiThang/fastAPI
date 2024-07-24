##Sắp xếp các thông số theo nhu cầu của bạn:
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
# nếu sử dụng Annotated, bạn sẽ không gặp phải vấn đề này,
# điều đó không thành vấn đề vì bạn không sử dụng các giá trị default của tham số hàm cho Query() hoặc Path().

from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

## Order the parameters as you need, tricks:
# Nếu bạn muốn:
# khai báo tham số truy vấn q không có Query cũng như bất kỳ giá trị default nào
# khai báo tham số đường dẫn item_id bằng Path
# đặt chúng theo một thứ tự khác
# không sử dụng Annotated

# ...Python có một cú pháp đặc biệt cho việc đó.
#
# Truyền *, làm tham số đầu tiên của hàm.
#
# Python sẽ không làm gì với * đó, nhưng nó sẽ biết rằng tất cả các tham số sau đây phải được gọi là từ khóa, còn đuọc gọi là kwargs

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

##Better with Annotated:

# Hãy nhớ rằng nếu bạn sử dụng Annotated,
# vì bạn không sử dụng các giá trị default của tham số hàm,
# nên bạn sẽ không gặp phải vấn đề này và có thể bạn sẽ không cần sử dụng *.
from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results




