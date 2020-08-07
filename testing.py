import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players

class NBAPlayer:
    def __init__(self, fullname, season, status=None):
        self.fullname = fullname
        self.season = season

    def details(self):
        try:
            players_dict = players.get_players()
            player_details = [player for player in players_dict if player['full_name'].lower() == self.fullname.strip().lower()][0]
            
            return player_details
        except:
            return "N/A"

    def gameLog(self):
        try:
            if self.season < 1900:
                    return "N/A"
            
            playerDetails = self.details()
         
            findGames = playergamelog.PlayerGameLog(player_id=playerDetails['id'], season=self.season.strip())
            gamelog = findGames.get_data_frames()[0]

            return gamelog
        except:
            return "N/A"
        
        
curry = NBAPlayer('lebron james ', '1016')

details = curry.details()
gamelog = curry.gameLog()


