from utilities import *
from toee import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5008):
		if (game.global_flags[56] == 1):
			game.timeevent_add( wench_no_longer_available, (), 86390000 )
	if (attachee.map == 5061):
		if (game.global_flags[289] == 1):
			game.timeevent_add( hostel_no_longer_available, (), 86390000 )
	if (attachee.map == 5152):
		if (game.global_flags[997] == 1):
			game.timeevent_add( goose_no_longer_available, (), 86390000 )
	return RUN_DEFAULT


def wench_no_longer_available():
	game.global_flags[56] = 0
	game.sleep_status_update()
	return RUN_DEFAULT


def hostel_no_longer_available():
	game.global_flags[289] = 0
	game.sleep_status_update()
	return RUN_DEFAULT


def goose_no_longer_available():
	game.global_flags[997] = 0
	game.sleep_status_update()
	return RUN_DEFAULT