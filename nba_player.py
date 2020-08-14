from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail

from constants import FULL_NAME, NA, YEAR_NOT_IN_RANGE_ERROR_MESSAGE, ID


class NBAPlayer:
    # Initialising class
    def __init__(self, fullname, season=None, opponentTeam=None, playerTeam=None):
        self.fullname = fullname
        self.season = season
        self.playerTeam = playerTeam
        self.opponentTeam = opponentTeam
        
    # Details about player itself
    def details(self):
        try:
            players_dict = players.get_players()
            player_details = [player for player in players_dict if player[FULL_NAME].lower() == self.fullname.strip().lower()][0]

            return player_details
        except:
            return NA
    
    # Returns details about the player's team
    def _playerTeamDetails(self):
        try:
            teams_dict = teams.get_teams()
            team_details = [team for team in teams_dict if team[FULL_NAME].lower() == self.playerTeam.strip().lower()][0]
            
            return team_details
        except:
            return NA
    
    # Returns details about an opponent team
    def _opponentTeamDetails(self):
        try:
            teams_dict = teams.get_teams()
            team_details = [team for team in teams_dict if team[FULL_NAME].lower() == self.opponentTeam.strip().lower()][0]
            
            return team_details
        except:
            return NA
        
    # Seasonal box score numbers
    def seasonLog(self):
        try:
            # Checks whether inputted season is valid
            if int(self.season) < 1850:
                return YEAR_NOT_IN_RANGE_ERROR_MESSAGE

            playerDetails = self.details()

            findGames = playergamelog.PlayerGameLog(player_id=playerDetails[ID], season=self.season.strip())
            gameLog = findGames.get_data_frames()[0]

            return gameLog
        except:
            return NA

    # Career box score numbers
    def careerLog(self):
        try:
            playerDetails = self.details()

            findGames = playergamelog.PlayerGameLog(player_id=playerDetails[ID], season=SeasonAll.all)
            careerLog = findGames.get_data_frames()[0]

            return careerLog
        except:
            return NA
    
    # Career shot chart for inputted player
    def careerShotChart(self):
        try:
            playerDetails = self.details()
            
            # Returns a shot chart (career-wide) for that player by passing in 
            # the FGA context measure to ensure it is ALL shots taken by the player
            return ShotChartDetail(player_id=playerDetails[ID], team_id=0, context_measure_simple="FGA").get_data_frames()[0]
        except:
            return NA
    
    # Team-based shot chart for a player (if they have played for multiple teams)
    def teamShotChart(self):
        try:
            # Finds data for the player and team they play for
            playerDetails = self.details()
            playerTeamDetails = self._playerTeamDetails()
            
            return ShotChartDetail(player_id=playerDetails[ID], team_id=playerTeamDetails[ID], context_measure_simple="FGA").get_data_frames()[0]
        except:
            return NA
        
    # Shot chart for player against a certain team with a certain team
    def againstTeamShotChart(self):
        try:
            # Finds data for the player, team they play for and team they played against
            playerDetails = self.details()
            playerTeamDetails = self._playerTeamDetails()
            opponentTeamDetails = self._opponentTeamDetails()
            
            return ShotChartDetail(player_id=playerDetails[ID], team_id=playerTeamDetails[ID], opponent_team_id=opponentTeamDetails[ID], context_measure_simple="FGA").get_data_frames()[0]
        except:
            return NA
    
    # Shot chart for player against a certain team for an entire career
    def careerAgainstTeamShotChart(self):
        try:
            # Finds data for player and the team they play against
            playerDetails = self.details()
            opponentTeamDetails = self._opponentTeamDetails()
            print("getting here")
            return ShotChartDetail(player_id=playerDetails[ID], opponent_team_id=opponentTeamDetails[ID], context_measure_simple="FGA").get_data_frames()[0]
        except:
            return NA