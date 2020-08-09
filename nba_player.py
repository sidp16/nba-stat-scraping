from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.static import players
from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail

from constants import FULL_NAME, NA, YEAR_NOT_IN_RANGE_ERROR_MESSAGE, ID


class NBAPlayer:
    # Initialising class
    def __init__(self, fullname, season=0):
        self.fullname = fullname
        self.season = season
        
    # Details about player itself
    def details(self):
        try:
            players_dict = players.get_players()
            player_details = [player for player in players_dict if player[FULL_NAME].lower() == self.fullname.strip().lower()][0]

            return player_details
        except:
            return NA
        
    # Seasonal box score numbers
    def seasonLog(self):
        try:
            if int(self.season) < 1900:
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
            return ShotChartDetail(player_id=playerDetails[ID], team_id=0, context_measure_simple="FGA").get_data_frames()[0]
        except:
            return NA
    
