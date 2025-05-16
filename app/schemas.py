from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserPublic(BaseModel):
    id: int
    user: str
    email: EmailStr


class UserSchema(BaseModel):
    user: str
    email: EmailStr
    password: str


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
