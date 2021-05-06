import os
import pytest

from app.sport import GetLeagues, GetSchedule, GetStandings, GetTeams, GetLeagueIds, GetTeamIds, ColourToHtml, Next_Last_Schedule

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_GetLeagues:

def test_GetTeams:

def test_GetLeagueIds:

def test_GetTeamIds:

def test_GetSchedule:

def test_GetStandings:

def test_GetTeams:

def test_ColourToHtml:

def test_Next_Last_Schedule:

def test_GetSchedule():
    # # with valid geography, returns the city name and forecast info:
    # results = get_hourly_forecasts(country_code="US", zip_code="20057", unit="F")
    # assert results["city_name"] == "Washington, DC"
    # assert len(results["hourly_forecasts"]) == 24
    # forecast = results["hourly_forecasts"][0]
    # assert sorted(list(forecast.keys())) == ["conditions", "image_url", "temp", "timestamp"]
    # assert forecast["timestamp"].endswith(":00")
    # assert f"{DEGREE_SIGN}F" in forecast["temp"]
    #
    # # with invalid geography, fails gracefully and returns nothing:
    # invalid_results = get_hourly_forecasts(country_code="US", zip_code="OOPS", unit="F")
    # assert invalid_results == None

def test_GetStandings():
    # assert format_hour("2021-03-29T21:00:00-04:00") == "21:00"
