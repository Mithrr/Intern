from flask import Blueprint, redirect, session, url_for, render_template
from auth import oauth

bp = Blueprint('routes', __name__)

@bp.route("/")
def index():
    return render_template("login.html")

@bp.route("/login/<provider>")
def login(provider):
    redirect_uri = url_for("routes.authorize", provider=provider, _external=True)
    return oauth.create_client(provider).authorize_redirect(redirect_uri)

@bp.route("/authorize/<provider>")
def authorize(provider):
    token = oauth.create_client(provider).authorize_access_token()
    user = oauth.create_client(provider).parse_id_token(token)
    session["user"] = dict(user)
    return redirect(url_for("routes.profile"))

@bp.route("/profile")
def profile():
    if "user" not in session:
        return redirect(url_for("routes.index"))
    return render_template("profile.html", user=session["user"])

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("routes.index"))