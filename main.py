# Several imports from different files
from regression_model import RegressionModel
from nba_api.stats.static import teams
from nba_api.stats.static import players
from NBA_Player.nba_player import NBAPlayer
from nba_api.stats.endpoints import teamyearbyyearstats
from nba_api.stats import endpoints
from NBA_Player.shot_charts import ShotCharts
from NBA_Player.statistics import Statistics
from NBA_Player.box_scores import BoxScores

# To check what these sets of data offer offer (which variables I can use)
teams_dict = teams.get_teams()
team_details = [team for team in teams_dict]
data = endpoints.leagueleaders.LeagueLeaders(stat_category_abbreviation='FGA')
leaders = data.league_leaders.get_data_frame()
lakers = [team for team in teams_dict if team["full_name"] == "Los Angeles Lakers"][0]
player_dict = players.get_players()
lakersStats = teamyearbyyearstats.TeamYearByYearStats(team_id=lakers['id']).get_data_frames()[0]

# Linear regression model class can take in two viable variables and creates
# a linear regression graph plotting them against each other
# model1 = RegressionModel('PTS', 'AST', 'AST', [1, 2, 5, 8, 12])
# model1.draw()

# Creating an NBA Player using class
lebron = NBAPlayer(fullname='LeBron James', playerTeam="Los Angeles Lakers",
                   opponentTeam="Golden State Warriors")

# Can get career / season wide box score logs
lbjCareerBoxScores = BoxScores.careerLog(player=lebron)
lbj2020BoxScores = BoxScores.seasonLog(player=lebron, season="2019")

# Can get different shot charts for a player (career or team wide)
lbjCareerShots = ShotCharts.careerShotChart(lebron)
lbjShotsLakers = ShotCharts.teamShotChart(lebron)
lbjShotsAgainstGSWWithLakers = ShotCharts.againstTeamShotChart(lebron)
lbjShotsAgainstGSW = ShotCharts.careerAgainstTeamShotChart(lebron)

# Career averages / totals year by year
lbjCareerStats = Statistics.careerAverages(lebron) 
lbjCareerTotals = Statistics.careerTotals(lebron)

