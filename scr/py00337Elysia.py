from toee import *
from utilities import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	game.global_flags[971] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[971] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_flags[994] == 0 ):
		attachee.object_flag_set(OF_OFF)
	if (game.global_flags[994] == 1 ):
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT