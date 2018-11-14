from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (not attachee.has_met( triggerer )):
		triggerer.begin_dialog( attachee, 1 )
	elif (game.quests[38].state == qs_accepted):
		triggerer.begin_dialog( attachee, 110 )
	else:
		triggerer.begin_dialog( attachee, 20 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.quests[38].state = qs_botched
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	if (attachee != OBJ_HANDLE_NULL and critter_is_unconscious(attachee) != 1 and not attachee.d20_query(Q_Prone)):
		run_off( attachee, triggerer )
		return SKIP_DEFAULT
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	lfa = location_from_axis(492,488)
	attachee.runoff(lfa)
	return RUN_DEFAULT
