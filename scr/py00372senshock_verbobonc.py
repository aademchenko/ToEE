from toee import *
from utilities import *
from py00439script_daemon import *
from Co8 import *
from InventoryRespawn import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5180) and (game.global_flags[990] == 1) and (game.global_flags[936] == 0):
		attachee.object_flag_unset(OF_OFF)
		game.global_flags[936] = 1
	if (game.global_flags[918] == 0):
		game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
		game.global_flags[918] = 1
	return RUN_DEFAULT


def respawn(attachee):
	box = find_container_near(attachee,1054)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
	return