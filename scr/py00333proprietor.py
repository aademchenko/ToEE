from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 10 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	game.global_vars[333] = game.global_vars[333] + 1
	if (game.global_vars[333] >= 2):
		game.party[0].reputation_add( 34 )
	game.timevent_add( go_away, ( attachee, ), 60000 )
	return RUN_DEFAULT


def go_away( attachee ):
	attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT