def get_missing_authorization_header_response() -> dict[str, str]:
    return {"msg": "Missing Authorization Header"}


def get_access_denied_response() -> dict[str, str]:
    return {"message": "Higher access level required."}
