# Header có thêm một chút chức năng ngoài những gì Path,Query và Cookie cung cấp.
#
# Hầu hết các Header tiêu chuẩn được phân tách bằng ký tự "gạch nối", còn được gọi là "ký hiệu dấu trừ" (-).
#
# Nhưng một biến như tác nhân người dùng không hợp lệ trong Python.
#
# Vì vậy, theo mặc định, Header sẽ chuyển đổi các ký tự tên tham số từ dấu gạch dưới (_) sang dấu gạch nối (-) để
# trích xuất và ghi lại các tiêu đề.
# 
# Ngoài ra, tiêu đề HTTP không phân biệt chữ hoa chữ thường,
# vì vậy, bạn có thể khai báo chúng theo kiểu Python tiêu chuẩn (còn được gọi là "snake_case").
#
# Vì vậy, bạn có thể sử dụng user_agent như bình thường trong mã Python,
# thay vì cần viết hoa các chữ cái đầu tiên là User_Agent hoặc một cái gì đó tương tự.
#
# Nếu vì lý do nào đó bạn cần tắt tính năng tự động chuyển đổi dấu gạch dưới thành dấu gạch nối,
# hãy đặt tham số Convert_underscores của Header thành False:



from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
):
    return {"strange_header": strange_header}