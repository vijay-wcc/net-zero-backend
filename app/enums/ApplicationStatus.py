from enum import Enum


class ApplicationStatus(Enum):
    CREATED = "CREATED"
    IN_REVIEW = "IN_REVIEW"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
