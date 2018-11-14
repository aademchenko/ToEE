from toee import *
from utilities import *
from InventoryRespawn import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if ( game.quests[11].state != qs_botched and game.global_flags[978] != 1 and game.global_flags[34] != 1):
		triggerer.begin_dialog( attachee, 1 )
	else:
		triggerer.begin_dialog( attachee, 30 )
	return SKIP_DEFAULT


def san_first_heartbeat(attachee, triggerer):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
		attachee.object_flag_set(OF_OFF)
	elif ( (game.global_flags[978] == 1) and (attachee.map == 5026) ):		## turns on substitute bing
		attachee.object_flag_unset(OF_OFF)
		if (game.global_flags[906] == 0):
			game.timevent_add(respawn_bing, (attachee), 604800000 ) #604800000ms is 1 week
			game.global_flags[906] = 1
	return RUN_DEFAULT


def san_heartbeat(attachee, triggerer):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
		attachee.object_flag_set(OF_OFF)
	elif (game.global_flags[978] == 1):
		attachee.object_flag_set(OF_OFF)
	else:
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_spell_cast( attachee, triggerer, spell ):
	if ( spell.spell == spell_heal ):
		game.global_flags[34] = 1
		triggerer.begin_dialog( attachee, 60 )
	return RUN_DEFAULT


def respawn_bing(attachee):
	box = find_container_near(attachee,1004)
	RespawnInventory(box)
	game.timevent_add(respawn_bing, (attachee), 604800000 ) #604800000ms is 1 week
	return