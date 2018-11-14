from toee import *
from utilities import *
from scripts import *
from InventoryRespawn import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[921] == 0):
		game.timevent_add(respawn, (attachee), 3600000 ) #3600000ms is 1 hour
		game.global_flags[921] = 1
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	game.global_flags[972] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[972] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_flags[993] == 0 ):
		attachee.object_flag_set(OF_OFF)
	if (game.global_flags[993] == 1 ):
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT


def respawn(attachee):
	box = find_container_near(attachee,1001)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 3600000 ) #3600000ms is 1 hour
	return