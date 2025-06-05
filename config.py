import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

    MS_CLIENT_ID = os.getenv("MS_CLIENT_ID")
    MS_CLIENT_SECRET = os.getenv("MS_CLIENT_SECRET")

    GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
    MS_DISCOVERY_URL = "https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration"