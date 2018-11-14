from utilities import *
from combat_standard_routines import *


from toee import *

def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT

def beggar_soon( attachee, triggerer ):
	triggerer.condition_add_with_args("Fallen_Paladin",0,0)
	game.timevent_add( beggar_now, ( attachee, triggerer ), 86400000 )
	return RUN_DEFAULT

def beggar_now( attachee, triggerer ):
	attachee.object_flag_set(OF_OFF)
	game.global_flags[199] = 1
	game.global_vars[24] = game.global_vars[24] + 1
	if (triggerer.reputation_has( 5 ) == 0):
		triggerer.reputation_add( 5 )
	if ( (game.global_vars[24] >= 3) and (triggerer.reputation_has( 6 ) == 0 )):
		triggerer.reputation_add( 6 )
	return RUN_DEFAULT

def complete_quest( attachee, triggerer ):
	game.quests[10].state = qs_completed
	attachee.reaction_adj( triggerer,+30)
	game.timevent_add( visited_church, ( attachee, triggerer ), 90000000 )
	return RUN_DEFAULT

def visited_church( attachee, triggerer ):
	game.global_flags[302] == 1
	return RUN_DEFAULT
