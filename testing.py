import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll

class NBAPlayer:
    def __init__(self, fullname, season):
        self.fullname = fullname
        self.season = season

    def details(self):
        try:
            players_dict = players.get_players()
            player_details = [player for player in players_dict if player['full_name'].lower() == self.fullname.strip().lower()][0]
            
            return player_details
        except:
            return "N/A"

    def seasonLog(self):
        try:
            if int(self.season) < 1900:
                    return "Year not in range!"
            
            playerDetails = self.details()
         
            findGames = playergamelog.PlayerGameLog(player_id=playerDetails['id'], season=self.season.strip())
            gamelog = findGames.get_data_frames()[0]

            return gamelog
        except:
            return "N/A"
        
    def careerlog(self):
        try:
            playerDetails = self.details()
            
            findGames = playergamelog.PlayerGameLog(player_id=playerDetails['id'], season=SeasonAll.all)
            careerlog = findGames.get_data_frames()[0]
            
            return careerlog
        except:
            return "N/A"
        
player = NBAPlayer('James Harden', '2017')

details = player.details()
gamelog = player.seasonLog()
careerlog = player.careerlog()


