from toee import *
from utilities import *
from InventoryRespawn import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.name == 14453):	# burne assistant
		if (game.global_vars[510] == 2):
			attachee.object_flag_set(OF_OFF)
		else:
			attachee.object_flag_unset(OF_OFF)
			if (game.global_flags[901] == 0):
				game.timevent_add(respawn_burne_assistant, (attachee), 86400000 )	#86400000ms is 24 hours
				game.global_flags[901] = 1
	elif (attachee.name == 14454):	# otis assistant
		if (game.global_flags[923] == 0):
			game.timevent_add(respawn_otis_assistant, (attachee), 604800000 )	#604800000ms is 1 week
			game.global_flags[923] = 1
	elif (attachee.name == 14595):	# screng assistant
		if (game.global_flags[911] == 0):
			game.timevent_add(respawn_screng_assistant, (attachee), 604800000 )	#604800000ms is 1 week
			game.global_flags[911] = 1
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def respawn_burne_assistant(attachee):
	box = find_container_near(attachee,1001)
	RespawnInventory(box)
	game.timevent_add(respawn_burne_assistant, (attachee), 86400000 )	#86400000ms is 24 hours
	return


def respawn_otis_assistant(attachee):
	box = find_container_near(attachee,1001)
	RespawnInventory(box)
	game.timevent_add(respawn_otis_assistant, (attachee), 604800000 )	#604800000ms is 1 week
	return


def respawn_screng_assistant(attachee):
	box = find_container_near(attachee,1001)
	RespawnInventory(box)
	game.timevent_add(respawn_screng_assistant, (attachee), 604800000 )	#604800000ms is 1 week
	return