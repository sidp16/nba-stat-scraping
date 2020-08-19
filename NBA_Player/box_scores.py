from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll

from constants import YEAR_NOT_IN_RANGE_ERROR_MESSAGE, ID, NA
from NBA_Player.nba_player import NBAPlayer


class BoxScores(object):
    
    SEASON_MINIMUM = 1850
    
    @classmethod
    def seasonLog(cls, player, season):
        """
        Parameters
        ----------
        cls : BoxScores
        player : NBAPlayer
            Player to return statistics for, in a given season.

        Returns
        -------
        DataFrame
            Season log for the player.

        """
        try:
            # Checks whether inputted season is valid
            if int(season) < cls.SEASON_MINIMUM:
                return YEAR_NOT_IN_RANGE_ERROR_MESSAGE

            playerDetails = player.details()

            findGames = playergamelog.PlayerGameLog(player_id=playerDetails[ID],
                                                    season=season.strip())
            gameLog = findGames.get_data_frames()[0]

            return gameLog
        except:
            return NA
    
    @classmethod
    def careerLog(cls, player):
        try:
            playerDetails = player.details()

            findGames = playergamelog.PlayerGameLog(player_id=playerDetails[ID],
                                                    season=SeasonAll.all)
            careerLog = findGames.get_data_frames()[0]

            return careerLog
        except:
            return NA

