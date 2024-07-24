#Create a middleware:Phần mềm trung gian (chỉ là một hàm) sẽ tạo SQLAlchemy SessionLocal mới cho mỗi yêu cầu,
#thêm nó vào yêu cầu rồi đóng nó sau khi yêu cầu kết thúc.
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

#request.state:
#request.state là một thuộc tính của mỗi đối tượng Request.
#Nó được sử dụng để lưu trữ các đối tượng tùy ý đính kèm vào chính yêu cầu,
#chẳng hạn như phiên cơ sở dữ liệu trong trường hợp này.
#Đối với chúng ta trong trường hợp này,
#nó giúp đảm bảo một phiên cơ sở dữ liệu duy nhất được sử dụng trong suốt yêu cầu
#và sau đó được đóng lại (trong middleware).

#Dependencies with yield or middleware:
# Thêm middleware ở đây tương tự như những gì một dependency với yield thực hiện, nhưng có một số điểm khác biệt:
#
# Nó yêu cầu nhiều mã hơn và phức tạp hơn một chút.
# Middleware phải là một hàm async.
# Nếu có mã trong đó phải "chờ" mạng, nó có thể "chặn" ứng dụng của bạn và làm giảm hiệu suất một chút.
# Mặc dù có thể không quá vấn đề với cách SQLAlchemy hoạt động.
# Nhưng nếu bạn thêm nhiều mã vào middleware có nhiều thao tác I/O chờ đợi, nó có thể trở thành vấn đề.
# Middleware được chạy cho mọi yêu cầu.
# Do đó, một kết nối sẽ được tạo ra cho mọi yêu cầu.
# Ngay cả khi hoạt động đường dẫn (path operation) xử lý yêu cầu đó không cần DB.