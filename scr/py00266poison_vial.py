from toee import *
from combat_standard_routines import *


def san_insert_item( attachee, triggerer ):
	if (triggerer.name == 8047):
		game.global_flags[113] = 1
	else:
		game.global_flags[113] = 0
	return RUN_DEFAULT
