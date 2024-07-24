# Để tạo phần mềm trung gian, bạn sử dụng trình decorator @app.middleware("http") ở đầu hàm.
#
# Chức năng phần mềm trung gian nhận được:
#
# Yêu cầu.
#
# Hàm call_next sẽ nhận yêu cầu dưới dạng tham số.
# Hàm này sẽ chuyển yêu cầu tới thao tác đường dẫn tương ứng.
# Sau đó, nó trả về phản hồi được tạo bởi thao tác đường dẫn tương ứng.
# Sau đó, bạn có thể sửa đổi thêm phản hồi trước khi trả lại
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

#Trước và sau Response:

# Bạn có thể thêm mã để chạy cùng với yêu cầu trước khi bất kỳ thao tác đường dẫn nào nhận được nó.
#
# Và cả sau khi phản hồi được tạo, trước khi trả lại.
#
# Ví dụ: bạn có thể thêm tiêu đề tùy chỉnh X-Process-Time chứa thời gian tính bằng giây
# để xử lý yêu cầu và tạo phản hồi:


import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


