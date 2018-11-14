from toee import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	if ( (game.quests[66].state == qs_accepted) and (attachee.map == 5061) ):	##turns on jewel merchant in Nulb Hostel
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[965] = 1
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	return RUN_DEFAULT