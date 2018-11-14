from toee import *
from InventoryRespawn import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.map == 5006):
		attachee.float_line( 23000, triggerer )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5007):
		if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
			attachee.object_flag_set(OF_OFF)
		else:
			attachee.object_flag_unset(OF_OFF)
			if (game.global_flags[908] == 0):
				game.timevent_add(respawn, (attachee), 3600000 ) #3600000ms is 1 hour
				game.global_flags[908] = 1
	elif (attachee.map == 5006):
		if (game.global_vars[510] != 2):
			if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6):
				attachee.object_flag_unset(OF_OFF)
		else:
			attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[961] == 3):
		if (not game.combat_is_active()):
			if (is_better_to_talk(attachee, game.party[0])):
				game.global_vars[961] = 4
				attachee.turn_towards(game.party[0])
				game.party[0].begin_dialog(attachee,90)
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 10):
		return 1
	return 0


def respawn(attachee):
	box = find_container_near(attachee,1001)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 3600000 ) #3600000ms is 1 hour
	return