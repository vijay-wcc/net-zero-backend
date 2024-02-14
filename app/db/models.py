import uuid
from sqlalchemy import (Column, Integer, String, DateTime, UUID,
                        BigInteger, Enum, Sequence, event)
from sqlalchemy.sql.functions import func
from app.db.base_class import Base
from app.enums.ApplicationStatus import ApplicationStatus
from app.enums.OrganizationClass import OrganizationClass


def format_org_id(_, connection, target):
    target.global_id = connection.scalar(func.nextval('global_id_seq'))
    target.org_id = f"{target.org_class.value}{str(target.global_id).zfill(6)}"


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4)

    global_id_seq = Sequence('global_id_seq')

    # global id with sequence
    global_id = Column(
        Integer,
        global_id_seq,
        server_default=global_id_seq.next_value()
    )

    org_id = Column(String(7), unique=True)

    name = Column(String, index=True)
    uprn = Column(BigInteger, index=True, )

    org_class = Column(Enum(OrganizationClass),
                       default=OrganizationClass.ORGANIZATION_CLASS_O,
                       nullable=False)

    application_status = Column(Enum(ApplicationStatus),
                                default=ApplicationStatus.CREATED,
                                nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now())
    updated_at = Column(DateTime(timezone=True),
                        onupdate=func.now(),
                        server_default=func.now())


event.listen(Organization, 'before_insert', format_org_id)
