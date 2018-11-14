from toee import *
from combat_standard_routines import *


def san_insert_item( attachee, triggerer ):
	if (triggerer.name == 8065):
		if (triggerer.stat_level_get(stat_hp_current) <= -10):
			game.global_flags[114] = 1
	return RUN_DEFAULT


