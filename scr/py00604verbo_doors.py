from toee import *
from combat_standard_routines import *


def san_use( door, triggerer ):
	if (game.global_flags[260] == 0):
		game.global_flags[260] = 1
	return RUN_DEFAULT