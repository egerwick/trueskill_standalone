from trueskill_lib import *
from combination_analysis import *
from json_import import extract
import time
start_time = time.time()
#----------------------------------------------
# Main rating scipt
#----------------------------------------------

# get the games from json
games = extract()

# execute the ranking (last argument is starting game)
# return the list of sorted, ranked players
f_mu = 25.0
f_tau = 0
track_mu_over_time = False
list_players = games_in_trueskill(games, f_mu, f_tau, track_mu_over_time, 0)

# Present the ranking results to terminal
min_number_games = 0
player_ranking_to_json(list_players, min_number_games, track_mu_over_time)

print("--- %s seconds ---" % (time.time() - start_time))

