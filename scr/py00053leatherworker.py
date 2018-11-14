from toee import *
from utilities import *
from InventoryRespawn import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat(attachee, triggerer):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
		attachee.object_flag_set(OF_OFF)
	else:
		attachee.object_flag_unset(OF_OFF)
		if (game.global_flags[904] == 0):
			game.timevent_add(respawn, (attachee), 604800000 ) #604800000ms is 1 week
			game.global_flags[904] = 1
	return RUN_DEFAULT


def respawn(attachee):
	box = find_container_near(attachee,1001)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 604800000 ) #604800000ms is 1 week
	return
