from pydantic import BaseModel


class CustomerSupport(BaseModel):
    email: str
    message: str
