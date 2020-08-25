import pandas as pd 
import random as rnd
import numpy as np 
import re
import requests
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.static import teams

headers = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

# getting dictionary of all teams
teams_dict = teams.get_teams()

# getting the lakers 2020 game log
lakers = [team for team in teams_dict if team["full_name"] == "Los Angeles Lakers"][0]
lakersGameLog = teamgamelog.TeamGameLog(team_id=lakers['id'],season="2019-20", 
                                        season_type_all_star="Regular Season").get_data_frames()[0]

# getting the clippers 2020 game log
clippers = [team for team in teams_dict if team["full_name"] == "Los Angeles Clippers"][0]
clippersGameLog = teamgamelog.TeamGameLog(team_id=clippers['id'],season="2019-20", 
                                        season_type_all_star="Regular Season").get_data_frames()[0]

# extracting the data for points scored for each team
lakers2020Points = [pts for pts in lakersGameLog['PTS']]
totalLakersPoints = 0

clippers2020Points = [pts for pts in clippersGameLog['PTS']]
totalClippersPoints = 0

# calculating total points scored in the season for the team
for x in range(0, len(lakers2020Points)):
    totalLakersPoints += lakers2020Points[x]
    # print(f"Laker Cumulative Total: {totalLakersPoints}")
    
for i in range(0, len(clippers2020Points)):
    totalClippersPoints += clippers2020Points[i]
    # print(f"Clipper Cumulative Total: {totalClippersPoints}")

# printing out an average for each team
print(f"Clippers Average: {totalClippersPoints / len(clippers2020Points)}")
print(f"Lakers Average: {totalLakersPoints / len(lakers2020Points)}")

# displaying the points distribution in the form of a histogram
lakersGameLog['PTS'].hist()
clippersGameLog['PTS'].hist()

# finding laker opponent teams
lakersMatchups = lakersGameLog['MATCHUP']
lakerHomeGames = []
lakerAwayGames = []

# wrote regex for home and away game matchups as per the (lakersGameLog)
# https://regex101.com/r/XGMXed/1

awayGamePattern = "[A-Z]+ @ +[A-Z]"
homeGamePattern = "[A-Z]+ vs. +[A-Z]"
pattern = "(?P<team1>[A-Z]{3}) (?:@|vs\.) (?P<team2>[A-Z]{3})"
reg = re.compile(pattern)

# checks if the matchup is home or away and adds respective games to separate lists
for game in lakersMatchups:
    reg_match = reg.match(game)
    print(reg_match.group('team1'), reg_match.group('team2'))
  
        
for p in range(0, len(lakerHomeGames)):
    team_details = [team for team in teams_dict if team["abbreviation"] == lakerHomeGames[p]][0]
    
    teamGameLog = teamgamelog.TeamGameLog(team_id=team_details["id"], season="2019-20", 
                                          season_type_all_star="Regular Season", headers=headers).get_data_frames()[0]
    
    teamMatchups = teamGameLog['MATCHUP']
    
    
    
    