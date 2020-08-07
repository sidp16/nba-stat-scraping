import pandas as pd
import numpy as np
import requests
from matplotlib import pyplot as plt
from sklearn import linear_model
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail
from nba_api.stats import endpoints

class NBAPlayer:
    def __init__(self, fullname, season=0):
        self.fullname = fullname
        self.season = season

    def details(self):
        try:
            players_dict = players.get_players()
            player_details = [player for player in players_dict if player['full_name'].lower() == self.fullname.strip().lower()][0]
            
            return player_details
        except:
            return "N/A"

    def seasonLog(self):
        try:
            if int(self.season) < 1900:
                    return "Year not in range!"
            
            playerDetails = self.details()
         
            findGames = playergamelog.PlayerGameLog(player_id=playerDetails['id'], season=self.season.strip())
            gamelog = findGames.get_data_frames()[0]

            return gamelog
        except:
            return "N/A"
        
    def careerlog(self):
        try:
            playerDetails = self.details()
            
            findGames = playergamelog.PlayerGameLog(player_id=playerDetails['id'], season=SeasonAll.all)
            careerlog = findGames.get_data_frames()[0]
            
            return careerlog
        except:
            return "N/A"

data = endpoints.leagueleaders.LeagueLeaders()
leaders = data.league_leaders.get_data_frame()

x, y = leaders.FGA/leaders.GP, leaders.PTS/leaders.GP

x = np.array(x).reshape(-1,1)     
y = np.array(y).reshape(-1,1)   

model = linear_model.LinearRegression()    
model.fit(x,y)                             

r2 = round(model.score(x,y), 2)            
predicted_y = model.predict(x) 

plt.scatter(x, y, s=15, alpha=.5)                            
plt.plot(x, predicted_y, color = 'black')                    
plt.title('Relationship Between FGA and PPG')          
plt.xlabel('FGA per Game')                                   
plt.ylabel('Points Per Game') 

player1 = NBAPlayer(leaders.PLAYER[0])
player1d = player1.details()                              

plt.annotate(player1d['last_name'],                       
              (x[0], y[0]),                       
              (x[0]-6,y[0]-2),                    
              arrowprops=dict(arrowstyle='-'))

player2 = NBAPlayer(leaders.PLAYER[7])
player2d = player2.details()

plt.annotate(player2d['first_name'],
             (x[7], y[7]),
             (x[7]-7, y[7]+3),
             arrowprops=dict(arrowstyle='-'))

player3 = NBAPlayer(leaders.PLAYER[1])
player3d = player3.details()

plt.annotate(player3d['first_name'],
             (x[1], y[1]),
             (x[1], y[1]-10),
             arrowprops=dict(arrowstyle='-'))

player4 = NBAPlayer(leaders.PLAYER[13])
player4d = player4.details()

plt.annotate(player4d['first_name'],
             (x[13], y[13]),
             (x[13]-3, y[13]-11),
             arrowprops=dict(arrowstyle='-'))

plt.savefig('graph2.png', dpi=300)