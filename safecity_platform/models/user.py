from pydantic import EmailStr


class User:
    id: str
    email: EmailStr
    password: str
    role: str

    def __str__(self):
        return (f"User ID: {self.id}, "
                f"Email: {self.email}, "
                f"Role: {self.role}")