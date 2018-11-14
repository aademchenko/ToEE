from toee import *
from utilities import *
from InventoryRespawn import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	attachee.turn_towards(triggerer)
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[914] == 0):
		game.timevent_add(respawn, (attachee), 604800000 ) #604800000ms is 1 week
		game.global_flags[914] = 1
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def respawn(attachee):
	box = find_container_near(attachee,1001)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 604800000 ) #604800000ms is 1 week
	return