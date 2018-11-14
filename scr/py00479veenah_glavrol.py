from toee import *
from InventoryRespawn import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 10 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[895] == 0):
		game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
		game.global_flags[895] = 1
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def respawn(attachee):
	box = find_container_near(attachee,1080)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
	return