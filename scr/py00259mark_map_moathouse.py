from toee import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	game.story_state = 1
	game.areas[2] = 1
	return RUN_DEFAULT


