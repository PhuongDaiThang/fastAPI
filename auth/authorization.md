# Authorization

Authorization là quá trình xác định quyền hạn của người dùng hoặc hệ thống sau khi đã được xác thực. Nó quyết định người dùng có thể làm gì và truy cập vào những tài nguyên nào trong hệ thống. Dưới đây là cái nhìn tổng quan về các khái niệm, phương pháp và cách triển khai authorization:

## 1. Khái Niệm Chính

- **Ủy Quyền:** Đảm bảo người dùng hoặc hệ thống có quyền truy cập vào tài nguyên và thực hiện các hành động cụ thể.
- **Quyền Hạn:** Các quyền truy cập được phân quyền dựa trên vai trò, nhóm, hoặc chính sách.

## 2. Phương Pháp Ủy Quyền

- **Danh Sách Quyền Truy Cập (Access Control Lists - ACLs):** Xác định quyền truy cập cho từng người dùng hoặc nhóm đối với các tài nguyên cụ thể. ACLs liệt kê quyền hạn cụ thể mà một người dùng hoặc nhóm có thể thực hiện.

- **Vai Trò và Quyền (Role-Based Access Control - RBAC):** Phân quyền dựa trên vai trò của người dùng trong hệ thống. Người dùng được gán một hoặc nhiều vai trò, và các vai trò này có quyền truy cập vào các tài nguyên hoặc hành động cụ thể.

- **Danh Sách Quyền Hạn (Permissions):** Phân quyền truy cập bằng cách gán quyền hạn cụ thể cho người dùng hoặc nhóm. Các quyền hạn có thể bao gồm xem, chỉnh sửa, xóa, hoặc quản lý tài nguyên.

- **Chính Sách Dựa Trên Attriute (Attribute-Based Access Control - ABAC):** Quyền truy cập được xác định dựa trên thuộc tính của người dùng, tài nguyên, và môi trường. ABAC cung cấp khả năng kiểm soát tinh vi hơn dựa trên các yếu tố như thời gian, vị trí, và thuộc tính của người dùng.

- **Xác Thực Dựa Trên Chính Sách (Policy-Based Access Control - PBAC):** Quyền truy cập được xác định dựa trên các chính sách quy định. Các chính sách này có thể bao gồm điều kiện và quy tắc chi tiết để quyết định quyền hạn.

## 3. Cách Triển Khai Authorization (Trong FastAPI)

### Cài Đặt Thư Viện

```bash
pip install fastapi uvicorn
```
### Ví dụ về Ủy quyền dựa trên vai trò:
``` python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import List

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Ví dụ về các vai trò người dùng
roles = {
    "admin": ["read", "write", "delete"],
    "user": ["read"]
}

def get_user_roles(token: str):
    # Xác thực và lấy vai trò của người dùng từ token
    if token == "admin_token":
        return ["admin"]
    elif token == "user_token":
        return ["user"]
    else:
        raise HTTPException(status_code=401, detail="Invalid token")

def check_permissions(required_permissions: List[str]):
    def wrapper(token: str = Depends(oauth2_scheme)):
        roles = get_user_roles(token)
        user_permissions = []
        for role in roles:
            user_permissions.extend(roles.get(role, []))
        if not any(p in user_permissions for p in required_permissions):
            raise HTTPException(status_code=403, detail="Insufficient permissions")
    return wrapper

@app.get("/admin/data")
async def get_admin_data(token: str = Depends(oauth2_scheme)):
    check_permissions(["read", "write", "delete"])(token)
    return {"message": "This is admin data"}

@app.get("/user/data")
async def get_user_data(token: str = Depends(oauth2_scheme)):
    check_permissions(["read"])(token)
    return {"message": "This is user data"}
```
### Chạy ứng dụng:
``` bash
uvicorn main:app --reload
```
### Lưu ý:
- Quản Lý Quyền Hạn: Đảm bảo các quy tắc và chính sách phân quyền được thiết lập rõ ràng và dễ quản lý.
- Xác Thực: Phải luôn kết hợp authorization với authentication để đảm bảo tính bảo mật.
- Kiểm Tra: Thực hiện kiểm tra bảo mật và đánh giá thường xuyên để đảm bảo rằng hệ thống phân quyền hoạt động như mong đợi và không có lỗ hổng.