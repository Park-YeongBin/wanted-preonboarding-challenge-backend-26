from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate

def create_user(db: Session, user: UserCreate):
    hashed_password = user.password + "notreallyhashed"  # 실제로는 해싱 필요
    db_user = User(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()
