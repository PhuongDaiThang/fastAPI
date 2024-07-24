# Để loại trừ tham số truy vấn khỏi lược đồ OpenAPI được tạo (và do đó, khỏi hệ thống tài liệu tự động),
# hãy đặt tham số include_in_schema của Query thành False:

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}