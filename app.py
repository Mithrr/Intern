from flask import Flask
from config import Config
from auth import configure_oauth
from routes import bp as routes_bp

app = Flask(__name__)
app.config.from_object(Config)

configure_oauth(app)

app.register_blueprint(routes_bp)

if __name__ == "__main__":
    app.run(debug=True)