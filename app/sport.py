import os
from dotenv import load_dotenv
import json
import requests
import pandas as pd
from datetime import datetime
from operator import itemgetter
from webcolors import name_to_hex


# from app import APP_ENV

load_dotenv()

API_KEY = os.getenv("API_KEY")
LEAGUE = os.getenv("LEAGUE", default="Serie A")
TEAM = os.getenv("TEAM", default="Inter")
APP_ENV = os.getenv("APP_ENV", default="development")

def SetLeague():
    if APP_ENV == "development":
        league = input("PLEASE INPUT A LEAGUE: ")
        # team = input("PLEASE INPUT A TEAM: ")
    else:
        league = LEAGUE
        # team = TEAM
    return league

def SetTeam():
    if APP_ENV == "development":
        # league = input("PLEASE INPUT A LEAGUE: ")
        team = input("PLEASE INPUT A TEAM: ")
    else:
        # league = LEAGUE
        team = TEAM
    print(team)
    return team

def GetLeagues():
    response = requests.get(f"https://fly.sportsdata.io/v3/soccer/scores/json/Competitions?key={API_KEY}")
    if response.status_code != 200:
        return None
    parsed_response = json.loads(response.text)
    leagues = []
    for i in parsed_response:
        for x in i['Seasons']:
            if x['CurrentSeason'] == True:
                leagues.append(i['Name'])
    return leagues

def GetTeams(SeasonId):
    response = requests.get(f"https://fly.sportsdata.io/v3/soccer/scores/json/SeasonTeams/{SeasonId}?key={API_KEY}")
    if response.status_code != 200:
        return None
    parsed_response = json.loads(response.text)
    teams = [i['Team']['Name'] for i in parsed_response]
    return teams

def GetLeagueIds(league):
    response = requests.get(f"https://fly.sportsdata.io/v3/soccer/scores/json/Competitions?key={API_KEY}")
    if response.status_code != 200:
        return None, None, None, None
    parsed_response = json.loads(response.text)
    tempList = [i['Seasons'] for i in parsed_response if i['Name'] == league][0]
    tempList = [i for i in tempList if i['CurrentSeason'] == True][0]
    SeasonId = tempList['SeasonId']
    print(SeasonId)
    RoundId = [i['RoundId'] for i in tempList['Rounds'] if i['CurrentRound'] == True][0]
    print(RoundId)
    return SeasonId, RoundId

def GetTeamIds(team, SeasonId):
    response = requests.get(f"https://fly.sportsdata.io/v3/soccer/scores/json/SeasonTeams/{SeasonId}?key={API_KEY}")
    if response.status_code != 200:
        return None, None, None, None
    parsed_response = json.loads(response.text)
    TeamList = [i for i in parsed_response if i['Team']['Name'] == team][0]
    TeamId = TeamList['TeamId']
    LogoUrl = TeamList['Team']['WikipediaLogoUrl']
    C1 = TeamList['Team']['ClubColor1']
    if C1 == "White":
        C1 = None
    C2 = TeamList['Team']['ClubColor2']
    if C2 == "White":
        C2 = None
    C4 = TeamList['Team']['ClubColor3']
    if C4 == None:
        C4 = "White"
    cList = [C1,C2,"Black",C4]
    Colours = []
    for i in cList:
        if i != None:
            Colours.append(i.replace(" ", ""))
        else:
            Colours.append(i)
    print(TeamId)
    print(LogoUrl)
    print(Colours)

    return  TeamId, LogoUrl, Colours

def GetStandings(RoundId):
    response = requests.get(f"https://fly.sportsdata.io/v3/soccer/scores/json/Standings/{RoundId}?key={API_KEY}")
    if response.status_code != 200:
        return None
    parsed_response = json.loads(response.text)
    standings = [i for i in parsed_response if i['Scope'] == "Total"]
    standings = sorted(standings, key=itemgetter('Order'))
    return standings

def GetSchedule(RoundId, TeamId):
    response = requests.get(f"https://fly.sportsdata.io/v3/soccer/scores/json/Schedule/{RoundId}?key={API_KEY}")
    if response.status_code != 200:
        return None
    parsed_response = json.loads(response.text)
    schedule = [i for i in parsed_response if i['AwayTeamId'] == TeamId or i['HomeTeamId'] == TeamId]
    # print(schedule)
    return schedule

def ColourToHtml(Colours):
    htmlcolours = []
    for i in Colours:
        if i == None:
            htmlcolours.append("#6D757D")
        else:
            try:
                hex = name_to_hex(i)
                if hex != None:
                    htmlcolours.append(hex)
                else:
                    htmlcolours.append("#6D757D")
            except:
                htmlcolours.append("#6D757D")

    print(htmlcolours)
    return htmlcolours
if __name__ == "__main__":

    print(f"RUNNING THE LIVE SCORES APP IN {APP_ENV.upper()} MODE...")

    leagues = GetLeagues()
    print(leagues)

    league = SetLeague()
    SeasonId, RoundId = GetLeagueIds(league)

    teams = GetTeams(SeasonId)
    print(teams)

    team = SetTeam()

    print("LEAGUE:", league)
    print("TEAM:", team)

    TeamId, LogoUrl, Colours = GetTeamIds(team, SeasonId)

    if not SeasonId or not RoundId or not TeamId:
        print("INVALID PARAMS. PLEASE CHECK YOUR INPUTS AND TRY AGAIN!")
        exit()
    print(SeasonId, RoundId, TeamId, LogoUrl, Colours)

    standings = GetStandings(RoundId)
    for i in standings:
        print(i["Name"],i["Points"])
    schedule = GetSchedule(RoundId, TeamId)
    for i in schedule:
        print(i["DateTime"],"-", i["HomeTeamName"], str(i["HomeTeamScore"])+"-"+str(i["AwayTeamScore"]), i["AwayTeamName"])
    now = datetime.now()
    for i in schedule:
        x = datetime.strptime(i["DateTime"], '%Y-%m-%dT%H:%M:%S')
        if x > now:
            next = i
            break
    print(next["DateTime"], "-", next["HomeTeamName"], str(next["HomeTeamScore"])+"-"+str(next["AwayTeamScore"]), next["AwayTeamName"])

    print(ColourToHtml(Colours))

