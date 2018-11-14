from utilities import *
from toee import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	game.global_vars[708] = 0
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	for pc in game.party:
		curr = pc.stat_level_get( stat_hp_current )
		if (curr <= -1 and curr >= -9 and pc.distance_to(attachee) <= 10 and game.global_vars[708] <= 3):
			create_item_in_inventory( 8905, attachee )
			game.global_vars[708] = game.global_vars[708] + 1
			return RUN_DEFAULT
	return RUN_DEFAULT