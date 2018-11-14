from toee import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	game.moviequeue_add(268)
	game.moviequeue_play_end_game()
	return RUN_DEFAULT
