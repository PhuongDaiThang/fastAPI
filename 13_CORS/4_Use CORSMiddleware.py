# Bạn có thể định cấu hình nó trong ứng dụng FastAPI của mình bằng CORSMiddleware.
#
# Nhập CORSMiddleware.
#
# Tạo danh sách allowed origins  (dưới dạng chuỗi).
#
# Thêm nó dưới dạng "middleware" vào ứng dụng FastAPI của bạn.
#
# Bạn cũng có thể chỉ định xem backend có cho phép:
#
# Thông tin xác thực (Authorization headers, Cookie, v.v.).
#
# Các phương thức HTTP cụ thể (POST, PUT) hoặc tất cả các phương thức này có ký tự đại diện "*".
#
# Các headers HTTP cụ thể hoặc tất cả chúng có ký tự đại diện "*".
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}

#allow_origins - Danh sách các nguồn gốc được phép thực hiện các yêu cầu cross-origin
#allow_origin_regex - Một chuỗi biểu thức chính quy để khớp với các nguồn gốc được phép thực hiện các yêu cầu cross-origin.
#allow_methods - Danh sách các phương thức HTTP được phép cho các yêu cầu cross-origin
#allow_headers: -Danh sách các tiêu đề yêu cầu HTTP cần được hỗ trợ cho các yêu cầu cross-origin
#allow_credentials - Cho biết rằng cookie phải được hỗ trợ cho các yêu cầu cross-origin
#Exposure_headers - Cho biết mọi tiêu đề phản hồi mà trình duyệt có thể truy cập được.
#max_age - Đặt thời gian tối đa tính bằng giây để trình duyệt lưu vào bộ đệm phản hồi CORS. Mặc định là 600


#CORS preflight requests:
# Đây là bất kỳ yêu cầu OPTIONS nào có tiêu đề Origin và Access-Control-Request-Method.
#
# Trong trường hợp này, phần mềm trung gian sẽ chặn yêu cầu đến và
# phản hồi bằng các tiêu đề CORS thích hợp và phản hồi 200 hoặc 400 cho mục đích cung cấp thông tin.

#Simple requests:
# Bất kỳ yêu cầu nào có tiêu đề Origin. Trong trường hợp này, phần mềm trung gian sẽ chuyển yêu cầu như bình thường
# nhưng sẽ bao gồm các tiêu đề CORS thích hợp trong phản hồi.