from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:   #Lớp Config này được sử dụng để cung cấp cấu hình cho Pydantic.
        orm_mode = True  #Trong lớp Config đặt thuộc tính orm_mode = True.


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True


#Technical Details about ORM mode: dafault: "lazy loading".
#chúng không tìm nạp dữ liệu cho các mối quan hệ từ cơ sở dữ liệu
# trừ khi bạn cố truy cập vào thuộc tính chứa dữ liệu đó.

# Ví dụ: truy cập các mục thuộc tính:
 current_user.items  #sẽ khiến SQLAlchemy đi tới bảng mục và lấy các mục cho người dùng này, nhưng không phải trước đó.

