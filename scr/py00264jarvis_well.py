from toee import *
from combat_standard_routines import *


def san_remove_item( attachee, triggerer ):
	game.global_flags[63] = 1
	return SKIP_DEFAULT
