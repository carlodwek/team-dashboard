from flask import Blueprint, request, render_template
from app.sport import GetSchedule, GetStandings, GetTeams, GetLeagueIds, GetTeamIds

dashboard_routes = Blueprint("dashboard_routes", __name__)

@dashboard_routes.route("/team", methods=["GET", "POST"])
def team():
    print("TEAM...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    league = request_data.get("League") or "Serie A"

    SeasonId, RoundId = GetLeagueIds(league=league)
    teams = GetTeams(SeasonId)

    return render_template("team.html", league=league, teams=teams)

@dashboard_routes.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    print("DASHBOARD...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    league = request_data.get("League") or "Serie A"
    team = request_data.get("Team") or "Inter"

    SeasonId, RoundId = GetLeagueIds(league=league)
    TeamId, LogoUrl = GetTeamIds(team=team, SeasonId=SeasonId)
    standings = GetStandings(RoundId=RoundId)
    schedule = GetSchedule(RoundId=RoundId, TeamId=TeamId)

    return render_template("dashboard.html", league=league, team=team, LogoUrl=LogoUrl, standings=standings, schedule=schedule)

@dashboard_routes.route("/dashboard/schedule")
def dashboard_schedule():
    print("DASHBOARD SCHEDULE...", dict(request.args))

    league = request.args.get("League") or "Serie A"
    team = request.args.get("Team") or "Inter"

    SeasonId, RoundId = GetLeagueIds(league=league)
    TeamId, LogoUrl = GetTeamIds(team=team, SeasonId=SeasonId)
    standings = GetStandings(RoundId=RoundId)
    schedule = GetSchedule(RoundId=RoundId, TeamId=TeamId)

    return render_template("dashboard_schedule.html", league=league, team=team, LogoUrl=LogoUrl, standings=standings, schedule=schedule)

@dashboard_routes.route("/dashboard/standings")
def dashboard_standings():
    print("DASHBOARD STANDINGS...", dict(request.args))

    league = request.args.get("League") or "Serie A"
    team = request.args.get("Team") or "Inter"

    SeasonId, RoundId = GetLeagueIds(league=league)
    TeamId, LogoUrl = GetTeamIds(team=team, SeasonId=SeasonId)
    standings = GetStandings(RoundId=RoundId)
    schedule = GetSchedule(RoundId=RoundId, TeamId=TeamId)

    return render_template("dashboard_standings.html", league=league, team=team, LogoUrl=LogoUrl, standings=standings, schedule=schedule)
