from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"Account must be greater than or equal to 0: {value}")
        return value


user = User(name="Jack", email="jack@gmail.com", account_id=3)
print(user)
