#1_Body with examples:
#Ở đây, chuyển các examples chứa một ví dụ về dữ liệu được mong đợi trong Body():
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ],
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results

# 2_Body with multiple examples:

# Khi bạn thực hiện việc này, examples sẽ là một phần của Lược đồ JSON nội bộ cho dữ liệu body đó.
#
# Tuy nhiên, tại thời điểm này, Swagger UI, công cụ chịu trách nhiệm hiển thị giao diện người dùng tài liệu,
# không hỗ trợ hiển thị nhiều ví dụ cho dữ liệu trong Lược đồ JSON.

from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
                {
                    "name": "Bar",
                    "price": "35.4",
                },
                {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            ],
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results
# 3_OpenAPI-specific examples
# Trước khi Lược đồ JSON hỗ trợ examples,
# OpenAPI đã hỗ trợ cho một trường khác cũng được gọi là examples.
#
# examples dành riêng cho OpenAPI này nằm trong phần khác trong đặc tả OpenAPI.
# Nó đi vào chi tiết cho từng thao tác đường dẫn, không phải bên trong mỗi Lược đồ JSON.
#
# Và Swagger UI đã hỗ trợ examples field cụ thể này trong một thời gian.
# Vì vậy, bạn có thể sử dụng nó để hiển thị examples khác nhau trong giao diện người dùng tài liệu.
#
# Hình dạng của field examples dành riêng cho OpenAPI này là một lệnh có nhiều ví dụ (thay vì một danh sách),
# mỗi ví dụ có thông tin bổ sung cũng sẽ được thêm vào OpenAPI.
#
# Điều này không đi vào bên trong mỗi Lược đồ JSON có trong OpenAPI,
# điều này đi ra bên ngoài, trực tiếp trong thao tác đường dẫn.


#4_using_the openapi_examples Parameter:
# Bạn có thể khai báo examples dành riêng cho OpenAPI trong FastAPI bằng tham số openapi_examples cho:
# Path()
# Query()
# Header()
# Cookie()
# Body()
# Form()
# File()

# Các khóa của dict này xác định từng ví dụ và mỗi giá trị là một dict khác.
#
# Mỗi ví dụ cụ thể trong examples có thể chứa:
# summary: Mô tả ngắn gọn cho ví dụ.
# description: Một mô tả dài có thể chứa văn bản Markdown.
# value: Đây là ví dụ thực tế được hiển thị, ví dụ: a dict.
# externalValue:  thay thế cho giá trị, một URL trỏ đến ví dụ. Mặc dù điều này có thể không được hỗ trợ bởi nhiều công cụ như value.

#Minh họa cách sử dụng:
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results
