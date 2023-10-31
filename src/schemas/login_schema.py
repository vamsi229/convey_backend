from typing import Optional

from pydantic import BaseModel


class login_model(BaseModel):
    email: str
    password: str


class signup_model(BaseModel):
    userName: str
    email: str
    password: str
    cPassword: str


class get_user_model(BaseModel):
    email: str


class update_user_model(BaseModel):
    userName: Optional[str]
    phoneNumber: Optional[int]


class change_password_model(BaseModel):
    password: str
    newPassword: str
    confirmPassword: str
