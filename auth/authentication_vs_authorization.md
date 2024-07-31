# Sự Khác Biệt Giữa Authentication và Authorization

| Authentication                                                  | Authorization                                                  |
|-----------------------------------------------------------------|---------------------------------------------------------------|
| Authentication là bước đầu tiên của Authorization.              | Authorization là bước sau khi Authentication thành công.      |
| Authentication giúp xác định danh tính để cấp quyền đăng nhập vào ứng dụng. | Authorization giúp xác định quyền truy cập vào tài nguyên có trong ứng dụng. |
| Thường yêu cầu cung cấp tên đăng nhập và mật khẩu               | Tùy vào tính bảo mật mà sẽ yêu cầu các yếu tố xác thực khác nhau |
| Xác thực được hiển thị và người dùng có thể thay đổi một phần  | Việc ủy quyền không được hiển thị và không thể thay đổi        |
