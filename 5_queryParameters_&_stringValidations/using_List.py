from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items

# Trong trường hợp này, FastAPI sẽ không kiểm tra nội dung của list.
#
# Ví dụ: List[int] sẽ kiểm tra (và ghi lại) xem nội dung của List có phải là số nguyên hay không.
# Nhưng chỉ riêng List thì không.