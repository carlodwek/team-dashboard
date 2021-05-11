import os
import pytest

from app.sport import GetLeagues, GetSchedule, GetStandings, GetTeams, GetLeagueIds, GetTeamIds, ColourToHtml, Next_Last_Schedule

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")

def test_GetLeagues:

    leagues = GetLeagues()
    assert "Serie A" in leagues

def test_GetLeagueIds:
    
    seasonID, roundID = GetLeagueIds(league="Serie A")
    assert seasonID == 128
    assert roundID == 645

def test_GetTeams:
    teams = GetTeams(seasonID = 128)
    assert "AS Roma" in teams

def test_GetTeamIds:

    teamID, logourl, colors = GetTeamIds(team = "AS Roma", SeasonId = 128)
    assert teamID == 550
    assert logourl == "https://upload.wikimedia.org/wikipedia/en/f/f7/AS_Roma_logo_%282017%29.svg"
    assert colors == ['Maroon', 'Orange', 'Black', 'White']

def test_GetSchedule:
    
    schedule = GetSchedule(roundID = 645, teamID = 550)
    assert schedule[0]["HomeTeamName"]=="AS Roma" or schedule[0]["AwayTeamName"]=="AS Roma"


def test_GetStandings:

    standings = GetStandings(roundID=645)
    listTeams = []
    for x in standings:
        listTeams.append(x['Name'])
    assert "AS Roma" in listTeams
     

def test_ColourToHtml:

    listColors = ['None', 'Black', 'Broken']
    color = ColourToHtml(listColors)
    assert color = ["#6D757D", "#000000", "#6D757D"] 

def test_Next_Last_Schedule:

    next, last = Next_Last_Schedule(schedule)
    assert next[0]["HomeTeamName"]=="AS Roma" or next[0]["AwayTeamName"]=="AS Roma"
    assert last[0]["HomeTeamName"]=="AS Roma" or last[0]["AwayTeamName"]=="AS Roma"

    




