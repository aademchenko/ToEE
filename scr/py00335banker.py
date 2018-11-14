from toee import *
from utilities import *
from InventoryRespawn import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 10 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[917] == 0):
		game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
		game.global_flags[917] = 1
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[963] == 6):
		game.global_vars[963] = 7
		game.timevent_add( repo_man, (), 1814400000 )	# 21 days
	return RUN_DEFAULT


def repo_man():
	if (game.global_vars[963] == 7):
		game.quests[82].state = qs_botched
		game.global_vars[963] = 8
		game.global_flags[966] = 0
		game.party[0].reputation_add(38)
		game.party[0].reputation_remove(37)
	return RUN_DEFAULT


def respawn(attachee):
	box = find_container_near(attachee,1077)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
	return


def make_withdrawal( attachee, triggerer ):
	triggerer.money_adj(2000000)
	game.global_vars[899] = game.global_vars[899] + 1
	game.global_flags[810] = 1
	time_limit( attachee, triggerer )
	return RUN_DEFAULT


def time_limit( attachee, triggerer ):
	game.timevent_add(reset_flag_806, (attachee), 86400000 ) #86400000ms is 24 hours
	return RUN_DEFAULT


def reset_flag_806( attachee ):
	game.global_flags[810] = 0
	return RUN_DEFAULT