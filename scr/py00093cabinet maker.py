from toee import *
from InventoryRespawn import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
		attachee.object_flag_set(OF_OFF)
	elif (game.global_vars[967] == 0):
		attachee.object_flag_unset(OF_OFF)
		if (game.global_flags[909] == 0):
			game.timevent_add(respawn, (attachee), 604800000 ) #604800000ms is 1 week
			game.global_flags[909] = 1
	elif (game.global_vars[967] >= 1):
		attachee.object_flag_set(OF_OFF)
		game.global_vars[967] = 2
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[297] = 1
	if (game.global_flags[294] == 1):
		game.party[0].prestige_class_add[3]
	game.global_vars[23] = game.global_vars[23] + 1
	if (game.global_vars[23] >= 2):
		game.party[0].reputation_add( 92 )
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[297] = 0
	return RUN_DEFAULT


def respawn(attachee):
	box = find_container_near(attachee,1001)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 604800000 ) #604800000ms is 1 week
	return