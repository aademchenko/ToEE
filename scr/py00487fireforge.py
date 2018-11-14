from utilities import *
from toee import *
from py00439script_daemon import *
from InventoryRespawn import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.map == 5008):
		triggerer.begin_dialog(attachee,100)
	else:
		triggerer.begin_dialog(attachee,1)
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5008):
		if (game.quests[98].state != qs_completed):
			if (game.global_flags[505] == 1):
				attachee.object_flag_unset(OF_OFF)
		elif (game.quests[98].state == qs_completed):
			attachee.object_flag_set(OF_OFF)
	elif (attachee.map == 5121):
		if (game.global_vars[507] == 1):
			if (is_daytime() == 1):
				attachee.object_flag_unset(OF_OFF)
				if (game.global_flags[924] == 0):
					game.timevent_add(respawn_fireforge, (attachee), 86400000 )	#86400000ms is 24 hours
					game.global_flags[924] = 1
			elif (is_daytime() == 0):
				attachee.object_flag_set(OF_OFF)
		else:
			attachee.object_flag_set(OF_OFF)
	elif (attachee.map == 5163):
		if (game.global_vars[507] == 2):
			attachee.object_flag_unset(OF_OFF)
			if (game.global_flags[924] == 0):
				game.timevent_add(respawn_fireforge, (attachee), 86400000 )	#86400000ms is 24 hours
				game.global_flags[924] = 1
		else:
			attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def respawn_fireforge(attachee):
	box = find_container_near(attachee,1005)
	RespawnInventory(box)
	game.timevent_add(respawn_fireforge, (attachee), 86400000 )	#86400000ms is 24 hours
	return