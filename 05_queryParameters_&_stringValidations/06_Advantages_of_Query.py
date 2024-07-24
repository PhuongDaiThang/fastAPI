# Nên sử dụng Annotated thay vì giá trị mặc định trong tham số hàm
#
# Giá trị default của tham số hàm là giá trị mặc định thực tế, trực quan hơn với Python.
#
# Có thể gọi hàm tương tự ở những nơi khác mà không cần FastAPI và nó sẽ hoạt động như mong đợi.
# Nếu có một tham số bắt buộc (không có giá trị mặc định), trình soạn thảo sẽ cho  biết có lỗi,
# Python cũng sẽ báo lỗi nếu chạy nó mà không truyền tham số bắt buộc.
#
# Khi không sử dụng Annotated và thay vào đó sử dụng kiểu giá trị default (cũ),
# nếu gọi hàm đó mà không có FastAPI ở nơi khác,
# cần chuyển các đối số cho hàm để nó hoạt động chính xác,
# nếu không các giá trị sẽ khác với những gì mong đợi
#
#
# Vì Annotated có thể có nhiều chú thích siêu dữ liệu
# nên có thể sử dụng chức năng tương tự với các công cụ khác, như Typer.