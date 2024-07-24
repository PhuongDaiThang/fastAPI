##Number validations: greater than or equal:
# Với Query và Path, bạn có thể khai báo các ràng buộc về số.
# Ở đây, với ge=1, item_id sẽ cần phải là số nguyên "lớn hơn hoặc bằng" 1.

from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

##Number validations: greater than and less than or equal
# Tương tự cũng áp dụng cho:
#
# gt: lớn hơn
# le: nhỏ hơn hoặc bằng
from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

##Number validations: floats, greater than and less than;
# Xác thực số cũng hoạt động với các giá trị float.
#
# Đây là lúc điều quan trọng là có thể khai báo gt chứ không chỉ ge.
# Với nó, bạn có thể yêu cầu, chẳng hạn, giá trị phải lớn hơn 0, ngay cả khi nó nhỏ hơn 1.
#
# Vì vậy, 0,5 sẽ là một giá trị hợp lệ. Nhưng 0,0 hoặc 0 thì không.

from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results