from toee import *
from py00439script_daemon import record_time_stamp, get_v, set_v, npc_set, npc_unset, npc_get, tsc, within_rect_by_corners
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	record_time_stamp(506)
	set_v(500, get_v(500) + 1 )
	if ( get_v(498) / 75.0 )** 3 +  ( get_v(499) / 38.0 ) ** 3  + ( get_v(500) / 13.0 )**3 >= 1:
		record_time_stamp(511)
	return RUN_DEFAULT
