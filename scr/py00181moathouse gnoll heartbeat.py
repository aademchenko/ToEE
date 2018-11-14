from toee import *
from combat_standard_routines import *


def san_heartbeat( attachee, triggerer ):
	if (game.global_flags[288] == 1):
		location = location_from_axis( 484, 490 )
		attachee.runoff(location)
	return RUN_DEFAULT
