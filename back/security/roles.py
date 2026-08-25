"""Any utility functions relating to the role based access control (RBAC) logic."""

from typing import List, Optional

from constants.auth_constants import role_lookup
from mocks.fake_pcf_api import role_to_org_id


class RoleValidateResult:
    """Represents the result of a role list check."""

    def __init__(self, invalid_roles: Optional[List[str]] = []) -> None:
        self.success = len(invalid_roles) > 0 if invalid_roles else True
        self.invalid_roles = invalid_roles


def validate_role_list(roles: List[str]):
    """Checks a given list of roles against the central role list to ensure each is valid."""
    fail_list: List[str] = []
    for role in roles:
        if role not in role_lookup:
            fail_list.append(role)
    return RoleValidateResult(fail_list)


def get_org_ids_for_user(roles: List[str]):
    """Maps a users roles to the PCF Organisations they have access to."""
    org_ids = []
    for role in roles:
        if role in role_to_org_id:
            org_ids.append(role_to_org_id[role])
    return org_ids
