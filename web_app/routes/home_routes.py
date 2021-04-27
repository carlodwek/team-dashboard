from flask import Blueprint, request, render_template
from app.sport import GetLeagues

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    leagues = GetLeagues()
    return render_template("home.html", leagues=leagues)

@home_routes.route("/about")
def about():
    print("ABOUT...")
    return render_template("about.html")
