from toee import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.global_flags[196] == 1):
			triggerer.begin_dialog( attachee, 320 )
	elif (attachee.has_met(triggerer)):
		if (game.quests[6].state == qs_completed):
			triggerer.begin_dialog( attachee, 20 )
		elif (game.quests[6].state <= qs_accepted):
			if (game.global_flags[10] == 0):
				triggerer.begin_dialog( attachee, 120 )
			else:
				triggerer.begin_dialog( attachee, 150 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.quests[6].state = qs_botched
	game.global_flags[333] = 1
	game.global_vars[23] = game.global_vars[23] + 1
	if (game.global_vars[23] >= 2):
		game.party[0].reputation_add( 92 )
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[333] = 0
	return RUN_DEFAULT


def give_sword( pc ):
	item = game.obj_create( 4222, pc.loc )
	pc.item_get( item )
	return RUN_DEFAULT
