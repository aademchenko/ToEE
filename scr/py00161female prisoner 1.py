from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if ((game.global_flags[131] == 1) and not (attachee.map == 5121)):
		triggerer.begin_dialog( attachee, 140 )
	else:
		triggerer.begin_dialog( attachee, 80 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	if (attachee.map == 5121):
		leader = attachee.leader_get()
		if (leader != OBJ_HANDLE_NULL):
			leader.begin_dialog( attachee, 90 )
	return SKIP_DEFAULT


def run_off( attachee, triggerer ):
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT


def npc_check1 (attachee, triggerer, line):
	npc = find_npc_near(attachee,14251)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,100)
	return SKIP_DEFAULT


def npc_check2 (attachee, triggerer,line):
	npc = find_npc_near(attachee,14430)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,60)
	return SKIP_DEFAULT


def npc_check3 (attachee, triggerer, line):
	npc = find_npc_near(attachee,14431)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,60)
	return SKIP_DEFAULT


def get_rep( attachee, triggerer ):
	if triggerer.reputation_has( 7 ) == 0:
		triggerer.reputation_add( 7 )
	game.global_vars[25] = game.global_vars[25] + 2
	if ( game.global_vars[25] >= 3 and triggerer.reputation_has( 8 ) == 0):
		triggerer.reputation_add( 8 )
	return RUN_DEFAULT


def free_rep( attachee, triggerer ):
	if triggerer.reputation_has( 16 ) == 0:
		triggerer.reputation_add( 16 )
	game.global_vars[26] = game.global_vars[26] + 1
	if ( game.global_vars[26] >= 3 and triggerer.reputation_has( 17 ) == 0):
		triggerer.reputation_add( 17 )
	return RUN_DEFAULT