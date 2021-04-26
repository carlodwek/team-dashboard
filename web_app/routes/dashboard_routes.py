from flask import Blueprint, request, render_template
from app.sport import GetIds, GetSchedule, GetStandings

dashboard_routes = Blueprint("dashboard_routes", __name__)

@dashboard_routes.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    print("DASHBOARD...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    league = request_data.get("league") or "Serie A"
    team = request_data.get("team") or "Inter"

    SeasonId, RoundId, TeamId, LogoUrl = GetIds(league=league, team=team)
    standings = GetStandings(RoundId=RoundId)
    schedule = GetSchedule(RoundId=RoundId, TeamId=TeamId)

    return render_template("dashboard.html", league=league, team=team, LogoUrl=LogoUrl, standings=standings, schedule=schedule)
