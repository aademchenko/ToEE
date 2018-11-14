from toee import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_vars[28] = game.global_vars[28] + 1
	if (game.global_vars[28] >= 5):
		game.obj_create(14330, game.leader.location)
	return RUN_DEFAULT


def san_exit_combat( attachee, triggerer ):
	if (attachee.stat_level_get(stat_subdual_damage) >= attachee.stat_level_get(stat_hp_current)):
		game.global_vars[28] = game.global_vars[28] + 1
		if (game.global_vars[28] >= 5):
			game.obj_create(14330, game.leader.location)
	return RUN_DEFAULT