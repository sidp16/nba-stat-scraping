from nba_api.stats.static import players
from nba_api.stats.static import teams

from constants import FULL_NAME, NA


class NBAPlayer(object):
    # Initialising class
    def __init__(self, fullname, opponentTeam=None, playerTeam=None):
        self.fullname = fullname
        self.playerTeam = playerTeam
        self.opponentTeam = opponentTeam
    
  
    # Details about player itself
    def details(self):
        try:
            players_dict = players.get_players()
            player_details = \
                [player for player in players_dict if player[FULL_NAME].lower()
                 == self.fullname.strip().lower()][0]

            return player_details
        except:
            return NA

    # Returns details about the player's team
    def _playerTeamDetails(self):
        try:
            teams_dict = teams.get_teams()
            team_details = [team for team in teams_dict if team[FULL_NAME].lower()
                            == self.playerTeam.strip().lower()][0]

            return team_details
        except:
            return NA

    # Returns details about an opponent team
    def _opponentTeamDetails(self):
        try:
            teams_dict = teams.get_teams()
            team_details = \
                [team for team in teams_dict if team[FULL_NAME].lower()
                 == self.opponentTeam.strip().lower()][0]

            return team_details
        except:
            return NA
