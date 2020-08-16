from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll

from constants import YEAR_NOT_IN_RANGE_ERROR_MESSAGE, ID, NA
from NBA_Player.nba_player import NBAPlayer


class BoxScores(NBAPlayer):
    # Initialising class
    def __init__(self, fullname, season=None):
        super().__init__(fullname, season)
        self.fullname = fullname
        self.season = season

    # Seasonal box score numbers
    def seasonLog(self):
        try:
            # Checks whether inputted season is valid
            if int(self.season) < 1850:
                return YEAR_NOT_IN_RANGE_ERROR_MESSAGE

            playerDetails = self.details()

            findGames = playergamelog.PlayerGameLog(player_id=playerDetails[ID],
                                                    season=self.season.strip())
            gameLog = findGames.get_data_frames()[0]

            return gameLog
        except:
            return NA

    # Box score numbers for entire career
    def careerLog(self):
        try:
            playerDetails = self.details()

            findGames = playergamelog.PlayerGameLog(player_id=playerDetails[ID],
                                                    season=SeasonAll.all)
            careerLog = findGames.get_data_frames()[0]

            return careerLog
        except:
            return NA