# Đầu tiên, import Path từ fastapi và import Annotated:
from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# FastAPI đã thêm hỗ trợ cho Annotated (và bắt đầu đề xuất nó) trong phiên bản 0.95.0.
#
# Nếu bạn có phiên bản cũ hơn, bạn sẽ gặp lỗi khi cố gắng sử dụng Annotated.
#
# Đảm bảo bạn Nâng cấp phiên bản FastAPI lên ít nhất 0.95.1 trước khi sử dụng Annotated.