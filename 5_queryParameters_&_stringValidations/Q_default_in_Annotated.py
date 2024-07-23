#Khi sử dụng Query bên trong Annotated, không thể sử dụng tham số default cho Query.

#Thay vào đó hãy sử dụng giá trị mặc định thực tế của tham số hàm. Nếu không, nó sẽ không nhất quán.

#Ví dụ: điều này không được phép:
q: Annotated[str, Query(default="rick")] = "morty"
# vì nó không rõ giá trị default rick hay morty
# nên sử dụng:
q: Annotated[str, Query()] = "rick"
# hoặc cũ hơn:
q: str = Query(default="rick")