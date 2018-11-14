from toee import *
from utilities import *
from scripts import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (game.global_flags[966] == 1 and game.global_vars[939] == 1 and attachee.has_met(triggerer) and game.quests[108].state == qs_mentioned):
		triggerer.begin_dialog( attachee, 240 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	game.global_flags[975] = 1
	game.party[0].reputation_add( 45 )
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[975] = 0
	return RUN_DEFAULT