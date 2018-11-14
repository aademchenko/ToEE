from toee import *
from py00439script_daemon import record_time_stamp, get_v, set_v, npc_set, npc_unset, npc_get, tsc, tpsts, within_rect_by_corners
from combat_standard_routines import *
from py00446earthcombat import switch_to_gatekeeper

def san_dialog( attachee, triggerer ):
	if (not attachee.has_met(triggerer)):
		record_time_stamp(503)
		triggerer.begin_dialog( attachee, 1 )
	else:		
		triggerer.begin_dialog( attachee, 50 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	record_time_stamp(507)
	return RUN_DEFAULT