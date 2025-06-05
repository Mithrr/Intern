from authlib.integrations.flask_client import OAuth
from flask import redirect, url_for, session
from config import Config

oauth = OAuth()

def configure_oauth(app):
    oauth.init_app(app)

    oauth.register(
        name='google',
        client_id=Config.GOOGLE_CLIENT_ID,
        client_secret=Config.GOOGLE_CLIENT_SECRET,
        server_metadata_url=Config.GOOGLE_DISCOVERY_URL,
        client_kwargs={'scope': 'openid email profile'}
    )

    oauth.register(
        name='microsoft',
        client_id=Config.MS_CLIENT_ID,
        client_secret=Config.MS_CLIENT_SECRET,
        server_metadata_url=Config.MS_DISCOVERY_URL,
        client_kwargs={'scope': 'openid email profile'}
    )