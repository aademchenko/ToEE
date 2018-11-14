from utilities import *
from combat_standard_routines import *
from toee import *


def san_dialog( attachee, triggerer ):
	if (not attachee.has_met( triggerer )):
		triggerer.begin_dialog( attachee, 100 )
	elif (game.global_flags[91] == 1):
		triggerer.begin_dialog( attachee, 230 )
	else:
		triggerer.begin_dialog( attachee, 200 )
	return SKIP_DEFAULT

def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.quests[39].state = qs_botched
	game.global_flags[88] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[88] = 0
	return RUN_DEFAULT


def set_hostel_flag( attachee, triggerer ):
	game.global_flags[289] = 1
	game.timevent_add( hostel_room_no_longer_available, (), 86400000 )
	game.sleep_status_update()
	return RUN_DEFAULT
	

def hostel_room_no_longer_available():
	game.global_flags[289] = 0
	game.sleep_status_update()
	return RUN_DEFAULT