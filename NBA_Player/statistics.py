from nba_api.stats.endpoints import PlayerProfileV2

from constants import ID, NA
from NBA_Player.nba_player import NBAPlayer


class Statistics(NBAPlayer):
    # Initialising class
    def __init__(self, fullname, season=None, opponentTeam=None, playerTeam=None):
        super().__init__(fullname, season, opponentTeam, playerTeam)
        self.fullname = fullname
        self.season = season
        self.playerTeam = playerTeam
        self.opponentTeam = opponentTeam

        # Career year by year averages

    def careerAverages(self):
        try:
            # Finds data for player
            playerDetails = self.details()

            # Returns career year by year averages (per game) < can be changed
            return PlayerProfileV2(player_id=playerDetails[ID], per_mode36="PerGame").get_data_frames()[0]
        except:
            return NA
    
    def careerTotals(self):
        try:
            # Finds data for player
            playerDetails = self.details()
            
            # Returns career year by year advanced stats 
            return PlayerProfileV2(player_id=playerDetails[ID], per_mode36="Totals").get_data_frames()[0]
        except:
            return NA