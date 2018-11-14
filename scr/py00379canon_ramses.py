from toee import *
from scripts import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.has_met(triggerer)):
		triggerer.begin_dialog(attachee,10)
	else:
		triggerer.begin_dialog(attachee,1)
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	game.global_flags[941] = 1
	game.party[0].reputation_add( 46 )
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[941] = 0
	return RUN_DEFAULT