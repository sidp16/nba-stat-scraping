from regression_model import RegressionModel
from nba_api.stats.static import teams
from nba_player import NBAPlayer
from nba_api.stats import endpoints

# To check what these sets of data offer offer (which variables I can use)
teams_dict = teams.get_teams()
team_details = [team for team in teams_dict]
data = endpoints.leagueleaders.LeagueLeaders(stat_category_abbreviation='FGA')
leaders = data.league_leaders.get_data_frame()
lakers = [team for team in teams_dict if team["full_name"] == "Los Angeles Lakers"][0]

# Linear regression model class can take in two viable variables and creates
# a linear regression graph plotting them against each other
model1 = RegressionModel('PTS', 'AST', 'AST', [1, 2, 5, 8, 12],)
model1.draw()

# Can now get shot chart of a player for their entire career
lebron = NBAPlayer(fullname='LeBron James', playerTeam="Los Angeles Lakers",
                   opponentTeam="Golden State Warriors")

lbjShotsLakers = lebron.teamShotChart()
lbjShotsAgainstGSWWithLakers = lebron.againstTeamShotChart()
lbjCareerShots = lebron.careerShotChart()
lbjShotsAgainstGSW = lebron.careerAgainstTeamShotChart()


curry = NBAPlayer(fullname='Stephen Curry')
curryShots = curry.careerShotChart()


