# Có thể nhận được các Header trùng lặp.
# Điều đó có nghĩa là cùng một tiêu đề có nhiều giá trị.
#
# Bạn có thể xác định những trường hợp đó bằng cách sử dụng List trong phần khai báo kiểu.
#
# Bạn sẽ nhận được tất cả các giá trị từ Header trùng lặp dưới dạng List Python.
#
# Ví dụ: để khai báo tiêu đề X-Token có thể xuất hiện nhiều lần, bạn có thể viết:

from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}

# Nếu bạn liên lạc với thao tác đường dẫn đó, hãy gửi hai tiêu đề HTTP như:

X-Token: foo
X-Token: bar
# Câu trả lời sẽ như sau:
{
    "X-Token values": [
        "bar",
        "foo"
    ]
}
