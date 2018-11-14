from utilities import *
from combat_standard_routines import *
from toee import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog(attachee,1)
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.timevent_add( acolyte_start_game, (), 8000 )
	return RUN_DEFAULT


def san_exit_combat( attachee, triggerer ):
	if (attachee.stat_level_get(stat_subdual_damage) >= attachee.stat_level_get(stat_hp_current)):
		game.timevent_add( acolyte_start_game, (), 8000 )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_safe_to_talk(attachee,obj)):
				obj.begin_dialog(attachee,1)
				game.new_sid = 0
				return RUN_DEFAULT
	return RUN_DEFAULT


def acolyte_start_game():
	game.fade(0,0,1016,0)
	start_game_with_quest(29)
	return RUN_DEFAULT