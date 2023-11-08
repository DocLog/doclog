from flask_restful import Api

from .resource import (
    ConditionListResource,
    ConditionResource,
    HealthcareProfessionalListResource,
    HealthcareProfessionalResource,
    LoginResource,
    MedicineListResource,
    MedicineResource,
    OccurrenceListResource,
    OccurrenceResource,
    PatientConditionListResource,
    PatientConditionResource,
    PatientListResource,
    PatientMedicineListResource,
    PatientMedicineResource,
    PatientResource,
    RoleListResource,
    RoleResource,
    UserListResource,
    UserResource,
)


def set_routes(api: Api):
    """
    Set up and register API routes for various resources.

    Args:
        api (Api): An instance of Flask-RESTful Api to register routes with.
    """
    # Condition

    api.add_resource(ConditionResource, "/api/v1/condition/<int:data_id>")
    api.add_resource(ConditionListResource, "/api/v1/condition")

    # Healthcare Professional

    api.add_resource(
        HealthcareProfessionalResource, "/api/v1/healthcare-professional/<int:data_id>"
    )
    api.add_resource(
        HealthcareProfessionalListResource, "/api/v1/healthcare-professional"
    )

    # Medicine

    api.add_resource(MedicineResource, "/api/v1/medicine/<int:data_id>")
    api.add_resource(MedicineListResource, "/api/v1/medicine")

    # Occurrence

    api.add_resource(OccurrenceResource, "/api/v1/occurrence/<int:data_id>")
    api.add_resource(OccurrenceListResource, "/api/v1/occurrence")

    # Patient Condition

    api.add_resource(
        PatientConditionResource, "/api/v1/patient-condition/<int:data_id>"
    )
    api.add_resource(PatientConditionListResource, "/api/v1/patient-condition")

    # Patient Medicine

    api.add_resource(PatientMedicineResource, "/api/v1/patient-medicine/<int:data_id>")
    api.add_resource(PatientMedicineListResource, "/api/v1/patient-medicine")

    # Patient

    api.add_resource(PatientResource, "/api/v1/patient/<int:data_id>")
    api.add_resource(PatientListResource, "/api/v1/patient")

    # User

    api.add_resource(UserResource, "/api/v1/user/<int:data_id>")
    api.add_resource(UserListResource, "/api/v1/user")

    # Role

    api.add_resource(RoleResource, "/api/v1/role/<int:data_id>")
    api.add_resource(RoleListResource, "/api/v1/role")

    # Login

    api.add_resource(LoginResource, "/api/v1/login")
