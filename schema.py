from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str

class TaskCreate(TaskBase):
    owner_id: int

class Task(TaskBase):
    id: int
    auth_token: str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    tasks: list[Task] = []

    class Config:
        orm_mode = True
