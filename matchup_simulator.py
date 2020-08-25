import pandas as pd 
import random as rnd
import numpy as np 
import re
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.static import teams
        
# getting dictionary of all teams
teams_dict = teams.get_teams()

# getting the lakers 2020 game log
lakers = [team for team in teams_dict if team["full_name"] == "Los Angeles Lakers"][0]
lakersGameLog = teamgamelog.TeamGameLog(team_id=lakers['id'],season="2019-20", 
                                        season_type_all_star="Regular Season").get_data_frames()[0]

# getting the clippers 2020 game log
clippers = lakers = [team for team in teams_dict if team["full_name"] == "Los Angeles Clippers"][0]
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

awayGamePattern = "[A-Z]+ @ [A-Z]"
homeGamePattern = "[A-Z]+ vs. [A-Z]"

for y in range(0, len(lakersMatchups)):
    if re.search(homeGamePattern, lakersMatchups[y]):
        print("home")
    else:
        print("       AWAY")


# for y in range(0, len(lakers2020Points)):
#     homeGame = re.sub("LAL vs.","", lakersMatchups[y]).strip().
#     awayGame = re.sub("LAL @", "", lakersMatchups[y]).strip()
#     lakerHomeGames.append(homeGame)
#     lakerAwayGames.append(awayGame)
    
    