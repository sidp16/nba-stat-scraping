from nba_api.stats.endpoints import ShotChartDetail

from constants import ID, NA
from NBA_Player.nba_player import NBAPlayer


class ShotCharts(NBAPlayer):
    # Initialising class
    def __init__(self, fullname, season=None, opponentTeam=None, playerTeam=None):
        super().__init__(fullname, season, opponentTeam, playerTeam)
        self.fullname = fullname
        self.season = season
        self.playerTeam = playerTeam
        self.opponentTeam = opponentTeam

    # Career shot chart for inputted player
    def careerShotChart(self):
        try:
            playerDetails = self.details()

            # Returns a shot chart (career-wide) for that player by passing in
            # the FGA context measure to ensure it is ALL shots taken by the player
            return \
                ShotChartDetail(player_id=playerDetails[ID], team_id=0,
                                context_measure_simple="FGA").get_data_frames()[
                    0]
        except:
            return NA

    # Team-based shot chart for a player (if they have played for multiple teams)
    def teamShotChart(self):
        try:
            # Finds data for the player and team they play for
            playerDetails = self.details()
            playerTeamDetails = self._playerTeamDetails()

            return ShotChartDetail(player_id=playerDetails[ID], team_id=playerTeamDetails[ID],
                                   context_measure_simple="FGA").get_data_frames()[0]
        except:
            return NA

    # Shot chart for player against a certain team with a certain team
    def againstTeamShotChart(self):
        try:
            # Finds data for the player, team they play for and team they played against
            playerDetails = self.details()
            playerTeamDetails = self._playerTeamDetails()
            opponentTeamDetails = self._opponentTeamDetails()

            return ShotChartDetail(player_id=playerDetails[ID], team_id=playerTeamDetails[ID],
                                   opponent_team_id=opponentTeamDetails[ID],
                                   context_measure_simple="FGA").get_data_frames()[0]
        except:
            return NA

    # Shot chart for player against a certain team for an entire career
    def careerAgainstTeamShotChart(self):
        try:
            # Finds data for player and the team they play against
            playerDetails = self.details()
            opponentTeamDetails = self._opponentTeamDetails()
            return ShotChartDetail(player_id=playerDetails[ID], team_id=0, opponent_team_id=opponentTeamDetails[ID],
                                   context_measure_simple="FGA").get_data_frames()[0]
        except:
            return NA
        
    def yearBasedShotChart(self):
        pass