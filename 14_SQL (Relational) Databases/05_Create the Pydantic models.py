#Create initial Pydantic models / schemas:
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


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

#SQLAlchemy style and Pydantic style:

# Lưu ý rằng các mô hình SQLAlchemy định nghĩa các thuộc tính bằng cách sử dụng dấu =
# và truyền kiểu dữ liệu làm tham số cho Column, như sau:
name = Column(String)
# Trong khi đó, các mô hình Pydantic khai báo kiểu dữ liệu bằng dấu :, sử dụng cú pháp chú thích kiểu mới:
name: str
# ghi nhớ điều này để bạn không bị nhầm lẫn khi sử dụng dấu = và dấu : với chúng