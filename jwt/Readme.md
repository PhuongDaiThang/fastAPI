# JSON Web Token (JWT)

## Giới thiệu

JSON Web Token (JWT) là một tiêu chuẩn mở (RFC 7519) định nghĩa một cách nhỏ gọn và độc lập để truyền thông tin một cách an toàn dưới dạng đối tượng JSON giữa các bên. Thông tin này có thể được xác thực và tin cậy nhờ vào chữ ký số.

- **Nhỏ gọn**: JWT có kích thước nhỏ gọn, có thể dễ dàng được truyền qua URL, tham số POST hoặc trong HTTP header.
- **Tự chứa**: JWT chứa tất cả thông tin cần thiết về người dùng hoặc dữ liệu khác, loại bỏ nhu cầu phải truy vấn cơ sở dữ liệu nhiều lần.
### Một số ví dụ về JWT Token:
````bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjEzODY4OTkxMzEsImlzcyI6ImppcmE6MTU0ODk1OTUiLCJxc2giOiI4MDYzZmY0Y2ExZTQxZGY3YmM5MGM4YWI2ZDBmNjIwN2Q0OTFjZjZkYWQ3YzY2ZWE3OTdiNDYxNGI3MTkyMmU5IiwiaWF0IjoxMzg2ODk4OTUxfQ.uKqU9dTB6gKwG6jQCuXYAiMNdfNRw98Hw_IWuA5MaMo
````
Cấu trúc được hiểu đơn giản như sau: 
````
<base64-encoded header>.<base64-encoded payload>.<base64-encoded signature>
````
## Cài đặt

### Yêu cầu hệ thống

- Python 3.6+
- Thư viện `pyjwt`
- Thư viện `fastapi`
- Thư viện `fastapi-jwt-auth`

### Cài đặt thư viện

```bash
pip install pyjwt fastapi fastapi-jwt-auth
```
## Cách sử dụng
### Cấu trúc của JWT: header.payload.signature
JWT bao gồm ba phần chính:

- Header: Header bao gồm hai phần chính: loại token ( cho biết đây là một Token JWT) và thuật toán mã hóa được sử dụng (HMAC SHA256 (HS256) hoặc RSA).

- Payload: Là phần thứ 2 của token, chứa các claims, thường gặp: 
- - Registered claims: cung cấp thông tin hữu ích và tương thích. Ví dụ: iss (người phát hành), exp (thời gian hết hạn), sub (đối tượng), aud (khán giả), v.v.
- - Public claims: Được định nghĩa tùy ý. Nhưng nên đăng kí trong IANA JSON Web Token Registry hoặc sử dụng URI để tránh xung đột tên.
- - Private claims: Các claims tùy chỉnh được tạo ra để chia sẻ thông tin giữa các bên đã thỏa thuận sử dụng chúng, không thuộc loại registered hoặc public claims.
- -Ví dụ về Payload: 
````
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
````
- Signature là phần cuối cùng của JWT, được tạo ra để xác thực rằng token không bị thay đổi và (trong trường hợp token được ký bằng khóa riêng) xác nhận danh tính của người gửi.
- - Để tạo chữ ký:

- - - Kết hợp header và payload đã được mã hóa bằng Base64Url, cách nhau bằng dấu chấm.
- - - Sử dụng thuật toán và khóa bí mật để ký chuỗi kết hợp này.
- - Ví dụ với thuật toán HMAC SHA256:

````
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret
)
````
## Triển khai JWT trong FastAPI
```` python
from fastapi import FastAPI, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel

app = FastAPI()

# Cấu hình JWT, bao gồm khóa bí mật
class Settings(BaseModel):
    authjwt_secret_key: str = "secret"

# Hàm để nạp cấu hình cho AuthJWT
@AuthJWT.load_config
def get_config():
    return Settings()

# Mô hình dữ liệu cho người dùng khi đăng nhập
class User(BaseModel):
    username: str
    password: str

# Mô hình dữ liệu cho thông tin người dùng sau khi đăng nhập
class UserOut(BaseModel):
    username: str

# Endpoint để đăng nhập và nhận token
@app.post('/login')
def login(user: User, Authorize: AuthJWT = Depends()):
    # Kiểm tra thông tin đăng nhập
    if user.username != "test" hoặc user.password != "test":
        raise HTTPException(status_code=401, detail="Tên người dùng hoặc mật khẩu không hợp lệ")

    # Tạo token truy cập và trả về
    access_token = Authorize.create_access_token(subject=user.username)
    return {"access_token": access_token}

# Endpoint để truy cập vào tài nguyên bảo vệ
@app.get('/protected')
def protected(Authorize: AuthJWT = Depends()):
    try:
        # Kiểm tra token
        Authorize.jwt_required()
    except AuthJWTException as err:
        raise HTTPException(status_code=401, detail="Token không hợp lệ")

    # Lấy thông tin người dùng từ token và trả về
    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}

# Chạy ứng dụng FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
````
### Lưu ý:
- Bảo mật khóa bí mật: Khóa bí mật dùng để ký JWT phải được bảo mật. Không nên lưu trữ khóa bí mật trong mã nguồn công khai.
- Thời hạn JWT: Nên thiết lập thời hạn cho JWT để giảm thiểu rủi ro từ việc JWT bị lộ.
