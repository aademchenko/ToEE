from toee import *
from utilities import *
from scripts import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.quests[77].state == qs_completed and game.global_flags[992] == 1 and game.global_flags[935] == 0):
		attachee.turn_towards(triggerer)
		triggerer.begin_dialog( attachee, 360 )
	else:
		attachee.turn_towards(triggerer)
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[974] == 1):
		attachee.object_flag_set(OF_OFF)
	elif (attachee.map == 5170 and game.quests[77].state == qs_completed and game.global_flags[992] == 1 and game.global_flags[935] == 0):
		attachee.object_flag_unset(OF_OFF)
	elif (attachee.map == 5169 and game.quests[77].state == qs_completed and game.global_flags[992] == 1 and game.global_flags[935] == 0):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[974] = 1
	if (game.quests[77].state == qs_completed and game.global_flags[992] == 1 and game.global_flags[935] == 0):
		game.party[0].reputation_add( 43 )
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[974] = 0
	return RUN_DEFAULT


def party_spot_check():
	highest_spot = -999
	for pc in game.party:
		if pc.skill_level_get(skill_spot) > highest_spot:
			highest_spot = pc.skill_level_get(skill_spot) 
	return highest_spot