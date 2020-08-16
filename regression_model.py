import numpy as np
from matplotlib import pyplot as plt
from nba_api.stats import endpoints
from sklearn import linear_model
from adjustText import adjust_text

from constants import BLACK, LAST_NAME
from NBA_Player.nba_player import NBAPlayer


# Creates a Linear Regression Model by taking in two variables
class RegressionModel:
    def __init__(self, var1, var2, leaderVariable, annotations=1):
        self.var1 = var1
        self.var2 = var2
        self.leaderVariable = leaderVariable
        self.annotations = annotations

    @staticmethod
    def getData(self):
        data = endpoints.leagueleaders.LeagueLeaders(stat_category_abbreviation=self.leaderVariable)
        leaders = data.league_leaders.get_data_frame()

        return leaders

    def draw(self):
        leaders = self.getData(self)
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
        plt.plot(x, predicted_y, color=BLACK)

        return self.dotAnnotations(x, y, predicted_y)

    def dotAnnotations(self, x, y, predicted_y):
        # Get data for player annotations
        leaders = self.getData(self)
        
        # Places an annotation for the No.1 Player
        for i in range(0, len(self.annotations)):
            player1 = NBAPlayer(leaders.PLAYER[self.annotations[i]-1])
            player1d = player1.details()
            texts = [plt.text(x[self.annotations[i]-1], y[self.annotations[i]-1], player1d[LAST_NAME])]
            adjust_text(texts, arrowprops=dict(arrowstyle="-", color="red"))
            # plt.annotate(texts,
            #              (x[self.annotations[i]-1], y[self.annotations[i]-1]),
            #              (x[self.annotations[i]-1], y[self.annotations[i]-1]),
            #              arrowprops=dict(arrowstyle='-'))

        return self.labels()

    def labels(self):
        plt.title(f"Relationship Between {self.var1} and {self.var2}")
        plt.xlabel(f"{self.var1} per Game", fontsize="small")
        plt.ylabel(f"{self.var2} Per Game", fontsize="small")
        
        # Saves image and names it accordingly, using the variables inputted
        plt.savefig(f"{self.var1} VS {self.var2}.png", dpi=300)