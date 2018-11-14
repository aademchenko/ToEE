from toee import *
from combat_standard_routines import *
from py00446earthcombat import switch_to_gatekeeper

def san_dialog( attachee, triggerer ):
	if (not attachee.has_met(triggerer)):
		if (game.quests[43].state >= qs_mentioned):
			triggerer.begin_dialog( attachee, 1 )
		else:
			triggerer.begin_dialog( attachee, 10 )
	elif (game.quests[44].state >= qs_accepted):
		triggerer.begin_dialog( attachee, 20 )
	else:
		triggerer.begin_dialog( attachee, 30 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT