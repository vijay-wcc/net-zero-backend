from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.crud_organization import (create_organization, get_organizations,
                                        update_organization, delete_organization,
                                        get_organization)

from app.schemas.organization import OrganizationCreate, Organization, OrganizationUpdate

router = APIRouter()


@router.post("/organizations/", response_model=Organization, status_code=status.HTTP_201_CREATED)
def create_an_organization(organization_in: OrganizationCreate, db: Session = Depends(get_db)):
    organization = create_organization(db=db, organization_in=organization_in)
    return organization


@router.get("/organizations/", response_model=List[Organization])
def read_organizations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    organizations = get_organizations(db=db, skip=skip, limit=limit)
    return organizations


@router.get("/organizations/{org_id}", response_model=Organization)
def read_organization(org_id: str, db: Session = Depends(get_db)):
    organization = get_organization(db, org_id)
    if organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organization


@router.put("/organizations/{org_id}", response_model=Organization)
def update_item(org_id: str, organization: OrganizationUpdate, db: Session = Depends(get_db)):
    updated_organization = update_organization(db, org_id, organization)
    if updated_organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return updated_organization


@router.delete("/organizations/{org_id}")
def delete_item(org_id: str, db: Session = Depends(get_db)):
    deleted_organization = delete_organization(db, org_id)
    if deleted_organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return {"detail": f"Deleted organization {org_id}"}
