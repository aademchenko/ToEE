from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 200 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[298] = 1
	if game.global_flags[295] == 1:
#		game.party[0].prestige_class_add[3]
		game.party[0].reputation_add( 24 )
		return RUN_DEFAULT
	game.global_vars[23] = game.global_vars[23] + 1
	if (game.global_vars[23] >= 2):
		game.party[0].reputation_add( 92 )
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[298] = 0
	return RUN_DEFAULT
