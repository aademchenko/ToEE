from toee import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_vars[27] = game.global_vars[27] + 1
	if (game.global_vars[27] >= 3):
		game.obj_create(14316, attachee.location)
		game.global_vars[27] = -1000
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	attachee.float_line(game.random_range(1,3),triggerer)
	return RUN_DEFAULT


def san_exit_combat( attachee, triggerer ):
	if (attachee.stat_level_get(stat_subdual_damage) >= attachee.stat_level_get(stat_hp_current)):
		game.global_vars[27] = game.global_vars[27] + 1
		if (game.global_vars[27] >= 3):
			game.obj_create(14316, attachee.location)
			game.global_vars[27] = -1000
	return RUN_DEFAULT