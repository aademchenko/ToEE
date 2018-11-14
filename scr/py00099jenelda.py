from toee import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (not attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 1 )
	else:
		triggerer.begin_dialog( attachee, 20 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[330] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[330] = 0
	return RUN_DEFAULT


def get_rep( attachee, triggerer ):
	if triggerer.reputation_has( 7 ) == 0:
		triggerer.reputation_add( 7 )
	game.global_vars[25] = game.global_vars[25] + 1
	if ( game.global_vars[25] >= 3 and triggerer.reputation_has( 8 ) == 0):
		triggerer.reputation_add( 8 )
	return RUN_DEFAULT
		
