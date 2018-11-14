from utilities import *
from combat_standard_routines import *
from toee import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (game.global_flags[139] == 1):
		triggerer.begin_dialog( attachee, 1 )
	elif (not attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 10 )
	elif (game.quests[52].state == qs_unknown):
		triggerer.begin_dialog( attachee, 20 )
	else:
		triggerer.begin_dialog( attachee, 40 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[311] == 1):
		attachee.object_flag_set(OF_OFF)
		game.global_flags[115] = 1
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[115] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[115] = 0
	return RUN_DEFAULT


def kill_tubal( attachee ):
	game.timevent_add( tubal_dead, ( attachee, ), 172800000 )
	return RUN_DEFAULT


def tubal_dead( attachee ):
	game.global_flags[310] = 1
	return RUN_DEFAULT