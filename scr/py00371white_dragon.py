from utilities import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[995] = 1
	if triggerer.reputation_has( 26 ) == 0:
		triggerer.reputation_add( 26 )
	return RUN_DEFAULT

	
def san_start_combat( attachee, triggerer ):
	if attachee.name == 14999:	## Old White Dragon
		attachee.d20_send_signal(S_SetPowerAttack, 5)
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[995] = 0
	return RUN_DEFAULT