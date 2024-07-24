# Bây giờ hãy tạo các mô hình (lược đồ)
# Pydantic sẽ được sử dụng khi đọc dữ liệu, khi trả về dữ liệu từ API.
#
# Ví dụ: trước khi tạo một mục, chúng tôi không biết ID được gán cho nó là gì,
# nhưng khi đọc nó (khi trả về từ API), chúng tôi sẽ biết ID của nó.
#
# Tương tự như vậy, khi đọc một người dùng, bây giờ chúng ta có thể khai báo
# rằng các mục sẽ chứa các mục thuộc về người dùng này.
#
# Không chỉ ID của các mục đó mà còn tất cả dữ liệu mà chúng tôi đã
# xác định trong mô hình Pydantic để đọc các mục: Item.

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