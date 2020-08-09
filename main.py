# noinspection PyBroadException
from regression_model import RegressionModel
from nba_api.stats.static import teams
from nba_player import NBAPlayer
from nba_api.stats import endpoints

# To check what these dataframes offer (which variables I can see)
teams_dict = teams.get_teams()
team_details = [team for team in teams_dict]
data = endpoints.leagueleaders.LeagueLeaders()
leaders = data.league_leaders.get_data_frame()

# Linear regression model class can take in two viable variables and creates
# a linear regression graph plotting them against each other
model1 = RegressionModel('STL', 'BLK', 1)
model1.draw()

# Can now get shot chart of a player for their entire career
lebron = NBAPlayer(fullname='LeBron James')
lbjShots = lebron.careerShotChart()

curry = NBAPlayer(fullname='Stephen Curry')
curryShots = curry.careerShotChart()

