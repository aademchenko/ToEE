from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (not attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 1 )
	elif (game.quests[35].state == qs_mentioned):
		triggerer.begin_dialog( attachee, 70 )
	elif (game.quests[35].state == qs_accepted):
		triggerer.begin_dialog( attachee, 100 )
	elif (game.quests[35].state == qs_completed):
		triggerer.begin_dialog( attachee, 150 )
	else:
		triggerer.begin_dialog( attachee, 170 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.quests[35].state = qs_botched
	game.global_flags[329] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[329] = 0
	return RUN_DEFAULT

