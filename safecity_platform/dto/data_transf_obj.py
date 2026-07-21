from pydantic import BaseModel, EmailStr

class ORMBaseModel(BaseModel):
    model_config = {
        "from_attributes": True,
    }

class IncidentRequest(BaseModel):
    title: str
    incident_category: str
    law_breaking_category: str

class IncidentResponse(ORMBaseModel, IncidentRequest):
    id: str
    status: str = "detected"

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(ORMBaseModel):
    access_token: str
    token_type: str

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    role: str = "user"

class RegisterResponse(ORMBaseModel):
    id: str
    email: EmailStr