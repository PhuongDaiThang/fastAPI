# Khi xác định rõ ràng một tham số truy vấn bằng Query,
# bạn cũng có thể khai báo tham số đó để nhận danh sách các giá trị hoặc nói cách khác là nhận nhiều giá trị.

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items

# URL:
http://localhost:8000/items/?q=foo&q=bar
#bạn sẽ nhận được nhiều giá trị của tham số Query q (foo và bar) trong
#danh sách Python bên trong hàm thao tác đường dẫn của bạn, trong tham số hàm q.

# Phản hồi URL đó là:
# {
#   "q": [
#     "foo",
#     "bar"
#   ]
# }

# with defaults:
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items

# Đường dẫn: http://localhost:8000/items/

# default của q sẽ là ["foo", "bar"], phản hồi sẽ là:
# {
#   "q": [
#     "foo",
#     "bar"
#   ]
# }