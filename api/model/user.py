from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, String

from .base_model import BaseModel


class UserModel(BaseModel):
    """
    Model representing users.

    This class defines the database model for users, mainly used for authentication
    and access-limitation purposes.

    Attributes:
        id: The primary key of the model, representing its unique identifier.
        name: The user name. Should be an unique identifier and does not represent
        the name of the actual user.
        email: The e-mail address associated with this account.
        password: user password, used to authenticate user.
        role_id: user role, defines access permissions.
        patient_id: The unique identifier of the patient file associated with this
        user account.
        healthcare_professional_id: The unique identifier of the healthcare
        professional file associated with this user account.
    """

    __tablename__ = "User"

    name = Column(String(32), nullable=False, unique=True)
    email = Column(String(32), nullable=False, unique=True)
    password = Column(LargeBinary(60), nullable=False)
    role_id = Column(Integer, ForeignKey("Role.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("Patient.id"))
    healthcare_professional_id = Column(
        Integer, ForeignKey("HealthcareProfessional.id")
    )
