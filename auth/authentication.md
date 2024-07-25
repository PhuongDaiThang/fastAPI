# Authentication

Authentication là quá trình xác minh danh tính của người dùng hoặc hệ thống để đảm bảo rằng họ là ai mà họ tuyên bố. Dưới đây là cái nhìn tổng quan về các khái niệm, phương pháp và cách triển khai authentication:

## 1. Khái Niệm Chính

- **Xác Thực:** Đảm bảo người dùng hoặc hệ thống là chính xác và có quyền truy cập vào tài nguyên.
- **Danh Tính:** Thông tin xác thực (như tên người dùng, mật khẩu, mã OTP) được kiểm tra để xác nhận danh tính.

## 2. Phương Pháp Xác Thực

- **Tên Người Dùng và Mật Khẩu:** Đây là phương pháp phổ biến nhất, nơi người dùng cung cấp tên người dùng và mật khẩu. Hệ thống kiểm tra thông tin này để xác minh danh tính.

- **Mã OTP (One-Time Password):** Một mã tạm thời được gửi đến người dùng qua email, tin nhắn SMS, hoặc ứng dụng xác thực. Mã này chỉ có hiệu lực trong một khoảng thời gian ngắn.

- **Xác Thực Sinh Trắc Học:** Sử dụng các đặc điểm sinh trắc học như dấu vân tay, nhận diện khuôn mặt, hoặc quét mống mắt để xác thực.

- **Xác Thực Hai Yếu Tố (2FA):** Yêu cầu người dùng cung cấp hai hình thức xác thực khác nhau (ví dụ: mật khẩu và mã OTP) để tăng cường bảo mật.

- **Xác Thực Bằng Token:** Sử dụng các token (như JWT - JSON Web Token) để xác thực người dùng. Token thường được cấp phát sau khi người dùng đăng nhập và được gửi trong các yêu cầu tiếp theo để xác thực.

- **Xác Thực Dựa Trên OAuth:** Sử dụng OAuth để cấp quyền truy cập vào tài nguyên mà không cần chia sẻ mật khẩu. Thường thấy trong các ứng dụng web và di động.

## 3. Cách Triển Khai Authentication (Trong FastAPI)

### Cài Đặt Thư Viện

```bash
pip install fastapi uvicorn python-multipart
```
### Ví Dụ Về Xác Thực Sử Dụng OAuth2:
```` python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Union

app = FastAPI()

# Định nghĩa đối tượng bảo mật OAuth2 với tokenUrl
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Định nghĩa lớp User với các thuộc tính username và email
class User(BaseModel):
    username: str
    email: Union[str, None] = None

# Định nghĩa lớp UserInDB kế thừa từ User, thêm thuộc tính hashed_password
class UserInDB(User):
    hashed_password: str

# Hàm giả mã hóa mật khẩu
def fake_hash_password(password: str):
    return "fakehashed" + password

# Hàm kiểm tra người dùng hiện tại từ token
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Xác thực token ở đây (ví dụ: kiểm tra xem nó có hợp lệ không)
    if token != "fake_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": "fakeuser"}

# Định nghĩa route để lấy token
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = {"username": form_data.username}
    return {"access_token": "fake_token", "token_type": "bearer"}

# Định nghĩa route để đọc thông tin người dùng hiện tại
@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
```
### Chạy Ứng Dụng:
```` bash
uvicorn main:app --reload
````
### Lưu ý:
- Bảo Mật: Đảm bảo các phương pháp xác thực được bảo mật và dữ liệu nhạy cảm (như mật khẩu) được mã hóa đúng cách.
- Xác Thực Đối Tượng: Cân nhắc sử dụng xác thực mạnh mẽ hơn cho các hệ thống có yêu cầu bảo mật cao.
- Thử Nghiệm: Thực hiện kiểm tra bảo mật và audit thường xuyên để đảm bảo rằng hệ thống xác thực hoạt động như mong đợi và không có lỗ hổng.