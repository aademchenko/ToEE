from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5114): # Inside Ogre Cave
		if (game.quests[53].state == 0):
			attachee.object_flag_set(OF_OFF)
		else:
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if (attachee.map == 5114): # Inside Ogre Cave
		game.global_vars[14] = game.global_vars[14] + 1
		if (attachee.stat_level_get(stat_subdual_damage) >= attachee.stat_level_get(stat_hp_current)):
			game.global_vars[13] = game.global_vars[13] - 1
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (attachee.map == 5114): # Inside Ogre Cave
		for obj in game.obj_list_vicinity(attachee.location,OLC_NPC):
			if (obj.name == 14248 or obj.name == 14249):
				obj.turn_towards(triggerer)
				obj.attack(triggerer)
		game.new_sid = 0
	return RUN_DEFAULT


def san_exit_combat( attachee, triggerer ):
	if (attachee.map == 5114): # Inside Ogre Cave
		if (attachee.stat_level_get(stat_subdual_damage) >= attachee.stat_level_get(stat_hp_current)):
			game.global_vars[13] = game.global_vars[13] + 1
		if game.global_vars[13] > 5: 
			game.global_vars[13] = 5 
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	if (attachee.map == 5114): # Inside Ogre Cave
		game.global_vars[14] = game.global_vars[14] - 1
	return RUN_DEFAULT