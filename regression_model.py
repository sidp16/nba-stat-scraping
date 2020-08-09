import numpy as np
from matplotlib import pyplot as plt
from nba_api.stats import endpoints
from sklearn import linear_model

from constants import BLACK, LAST_NAME
from nba_player import NBAPlayer


# Creates a Linear Regression Model by taking in two variables
class RegressionModel:
    def __init__(self, var1, var2, annotations=1):
        self.var1 = var1
        self.var2 = var2
        self.annotations = annotations

    @staticmethod
    def getData(self):
        data = endpoints.leagueleaders.LeagueLeaders(stat_category_abbreviation=self.var1)
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

        return self.dotAnnotations(x, y)

    def dotAnnotations(self, x, y):
        # Get data for player annotations
        leaders = self.getData(self)

        # Places an annotation for the No.1 Player
        for i in range(0, self.annotations):
            player1 = NBAPlayer(leaders.PLAYER[i])
            player1d = player1.details()
            plt.annotate(player1d[LAST_NAME],
                         (x[i], y[i]),
                         (x[i], y[i]),
                         arrowprops=dict(arrowstyle='-'))

        return self.labels()

    def labels(self):
        plt.title(f"Relationship Between {self.var1} and {self.var2}")
        plt.xlabel(f"{self.var1} per Game")
        plt.ylabel(f"{self.var2} Per Game")
        
        # Saves image and names it accordingly, using the variables inputted
        plt.savefig(f"{self.var1} VS {self.var2}.png", dpi=300)