from toee import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	game.global_flags[155] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[155] = 0
	return RUN_DEFAULT