"""Holds any application-level constant variables for the auth logic."""


class Areas:
    """
    Enum-style object to hold codes for the various valid authentication areas.
    """

    def __init__(self) -> None:
        self.STAKEHOLDER = 'STAKEHOLDER'
        self.PO = 'PO'
        self.ADMIN = 'ADMIN'


auth_areas = Areas()


role_lookup = {
    'PDB_User': {'access_codes': []},
    'PBD_Stakeholder': {'access_codes': [auth_areas.STAKEHOLDER]},
    'PBD_Product_owner': {'access_codes': [auth_areas.STAKEHOLDER, auth_areas.PO]},
    'PDB_Admin': {
        'access_codes': [auth_areas.STAKEHOLDER, auth_areas.PO, auth_areas.ADMIN]
    },
}
jwt_alg = 'HS256'
