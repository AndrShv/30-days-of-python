from pydantic import BaseModel, Field, EmailStr, field_validator

class UserCreateDTO(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=18)  # ge = greater than or equal

    # Аналог кастомной аннотации валидации в Java
    @field_validator("username")
    @classmethod
    def validate_no_spaces(cls, value: str) -> str:
        if " " in value:
            raise ValueError("Username cannot contain spaces")
        return value

# Pydantic автоматически валидирует входящие типы и конвертирует их:
user = UserCreateDTO(username="andrey_dev", email="test@example.com", age="20") # age станет int 20!