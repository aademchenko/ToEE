from toee import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.quests[6].state = qs_botched
	game.global_flags[334] = 1
	game.global_vars[23] = game.global_vars[23] + 1
	if (game.global_vars[23] >= 2):
		game.party[0].reputation_add( 92 )
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[334] = 0
	return RUN_DEFAULT