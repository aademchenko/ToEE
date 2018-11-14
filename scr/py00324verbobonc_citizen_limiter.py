from toee import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5121 and game.global_vars[950] == 1):
		game.timevent_add( twelve_hour_time_limit_to_kill_wilfrick, (), 43200000 )	## 12 hours
		game.global_vars[950] = 2
	return RUN_DEFAULT


def twelve_hour_time_limit_to_kill_wilfrick():
	game.global_vars[704] = 20
	return RUN_DEFAULT