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
            player_details = \
                [player for player in players_dict if player['full_name'].lower() == self.fullname.strip().lower()][0]

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


# Creates a Linear Regression Model by taking in two variables
class RegressionModel:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    @staticmethod
    def getData():
        data = endpoints.leagueleaders.LeagueLeaders()
        leaders = data.league_leaders.get_data_frame()

        return leaders

    def draw(self):
        leaders = self.getData()

        x, y = leaders[self.var1] / leaders.GP, leaders[self.var2] / leaders.GP

        x = np.array(x).reshape(-1, 1)
        y = np.array(y).reshape(-1, 1)

        # Creates the graph itself
        model = linear_model.LinearRegression()
        model.fit(x, y)

        round(model.score(x, y), 2)
        predicted_y = model.predict(x)

        # Places all the dots on the graph using the values (x, y) which are
        # defined above
        plt.scatter(x, y, s=15, alpha=.5)
        plt.plot(x, predicted_y, color='black')

        return self.dotAnnotations(x, y)

    def dotAnnotations(self, x, y):
        # Get data for player annotations
        leaders = self.getData()
        player1 = NBAPlayer(leaders.PLAYER[0])
        player1d = player1.details()

        # Places an annotation for the No.1 Player
        plt.annotate(player1d['last_name'],
                     (x[0], y[0]),
                     (x[0], y[0]),
                     arrowprops=dict(arrowstyle='-'))

        # Saves image and names it accordingly
        plt.savefig(f"{self.var1} VS {self.var2}.png", dpi=300)

        return self.labels()

    def labels(self):
        plt.title(f"Relationship Between {self.var1} and {self.var2}")
        plt.xlabel(f"{self.var1} per Game")
        plt.ylabel(f"{self.var2} Per Game")


assistSteal = RegressionModel('AST', 'FG3M')
assistSteal.draw()
