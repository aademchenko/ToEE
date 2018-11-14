from toee import *
from utilities import *


def san_use( attachee, triggerer ):
	# play slides and end game
	set_end_slides_co8( attachee, triggerer )
	game.moviequeue_play_end_game()
	return RUN_DEFAULT


