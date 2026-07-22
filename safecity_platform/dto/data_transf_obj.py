from pydantic import BaseModel, EmailStr

from safecity_platform.models.categories import LawBreakingCategory, IncidentCategory


class ORMBaseModel(BaseModel):
    model_config = {
        "from_attributes": True,
    }

class IncidentRequest(BaseModel):
    title: str
    incident_category: IncidentCategory = IncidentCategory.STH_ELSE
    law_breaking_category: LawBreakingCategory = LawBreakingCategory.STH_ELSE

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