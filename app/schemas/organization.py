from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from app.enums.OrganizationClass import OrganizationClass
from app.enums.ApplicationStatus import ApplicationStatus


class OrganizationBase(BaseModel):
    name: str
    uprn: int
    org_class: OrganizationClass = OrganizationClass.O


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationInDBBase(OrganizationBase):
    id: UUID
    org_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Organization(OrganizationInDBBase):
    pass


class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    uprn: Optional[int] = None
    application_status: Optional[ApplicationStatus] = None
