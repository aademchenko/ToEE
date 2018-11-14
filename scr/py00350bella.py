from toee import *
from InventoryRespawn import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[920] == 0):
		game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
		game.global_flags[920] = 1
	return RUN_DEFAULT


def respawn(attachee):
	box = find_container_near(attachee,1064)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
	return