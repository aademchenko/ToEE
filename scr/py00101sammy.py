from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (anyone( triggerer.group_list(), "has_follower", 8014 )):
		triggerer.begin_dialog( attachee, 150 )
	elif (game.quests[32].state >= qs_mentioned) and (game.quests[63].state <= qs_mentioned):
		triggerer.begin_dialog( attachee, 100 )
	elif (game.quests[63].state >= qs_accepted):
		triggerer.begin_dialog( attachee, 210 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT
