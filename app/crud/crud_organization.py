from typing import Type, Optional

from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.db.models import Organization
from app.schemas.organization import OrganizationCreate, OrganizationUpdate


def create_organization(db: Session,
                        organization_in: OrganizationCreate) -> Organization:
    db_organization = Organization(**organization_in.dict())
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    db_organization.org_id = db.execute(
        text("SELECT org_id FROM organizations WHERE id = :value"),
        {"value": db_organization.id}).scalar_one()
    return db_organization


def get_organizations(db: Session,
                      skip: int = 0, limit: int = 100) \
        -> list[Type[Organization]]:
    return db.query(Organization).offset(skip).limit(limit).all()


def get_organization(db: Session, org_id: str) -> Optional[Type[Organization]]:
    return (db.query(Organization)
            .filter(Organization.org_id == org_id).first())


def update_organization(db: Session, org_id: str,
                        organization_in: OrganizationUpdate) \
        -> Optional[Type[Organization]]:
    db_organization = (db.query(Organization)
                       .filter(Organization.org_id == org_id).first())
    if db_organization is None:
        return None
    for var, value in vars(organization_in).items():
        setattr(db_organization, var, value) if value else None
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization


def delete_organization(db: Session, org_id: str)\
        -> Optional[Type[Organization]]:
    db_organization = (db.query(Organization)
                       .filter(Organization.org_id == org_id).first())
    if db_organization is None:
        return None
    db.delete(db_organization)
    db.commit()
    return db_organization
