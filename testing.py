from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players

players_dict = players.get_players()

curry = [player for player in players_dict if player['full_name'] == 'Stephen Curry'][0]

findingCurryGames = playergamelog.PlayerGameLog(player_id='201939', season='2015')
curryGameLog = findingCurryGames.get_data_frames()[0]