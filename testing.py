from nba_api.stats.static import players

players_dict = players.get_players()

bron = [player for player in players_dict if player['full name'] == 'LeBron James'][0]