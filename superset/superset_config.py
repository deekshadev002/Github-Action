import os
from flask_appbuilder.security.manager import AUTH_OAUTH

AUTH_TYPE = AUTH_OAUTH
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public"

OAUTH_PROVIDERS = [
    {
        "name": "keycloak",
        "token_key": "access_token",
        "icon": "fa-address-card",
        "remote_app": {
            "client_id": os.getenv("KEYCLOAK_CLIENT_ID"),
            "client_secret": os.getenv("KEYCLOAK_CLIENT_SECRET"),
            "api_base_url": os.getenv("KEYCLOAK_BASE_URL") + "/realms/" + os.getenv("KEYCLOAK_REALM") + "/protocol/openid-connect",
            "access_token_url": os.getenv("KEYCLOAK_BASE_URL") + "/realms/" + os.getenv("KEYCLOAK_REALM") + "/protocol/openid-connect/token",
            "authorize_url": os.getenv("KEYCLOAK_BASE_URL") + "/realms/" + os.getenv("KEYCLOAK_REALM") + "/protocol/openid-connect/auth",
            "client_kwargs": {"scope": "openid profile email"},
        },
    }
]

