from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		if ((game.global_flags[137] == 1) and (game.global_flags[138] == 1)):
			triggerer.begin_dialog( attachee, 160 )
		else:
			triggerer.begin_dialog( attachee, 100 )
	elif ((not attachee.has_met(triggerer)) or (game.global_flags[133] == 0)):
			triggerer.begin_dialog( attachee, 1 )
	elif ((game.global_flags[137] == 1) and (game.global_flags[138] == 1)):
		triggerer.begin_dialog( attachee, 190 )
	else:
		triggerer.begin_dialog( attachee, 150 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[351] == 0):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)
	game.global_flags[136] = 1
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[136] = 0
	return RUN_DEFAULTdef 


def san_join( attachee, triggerer ):
	obj = find_npc_near( attachee, 8029)
	if (obj != OBJ_HANDLE_NULL):
		triggerer.follower_add(obj)
	obj = find_npc_near( attachee, 8030)
	if (obj != OBJ_HANDLE_NULL):
		triggerer.follower_add(obj)
	return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	for obj in triggerer.group_list():
		if (obj.name == 8029):
			triggerer.follower_remove(obj)
		if (obj.name == 8030):
			triggerer.follower_remove(obj)
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
		attachee.reaction_set( pc, 50 )
	return RUN_DEFAULT


def get_rep( attachee, triggerer ):
	if triggerer.reputation_has( 16 ) == 0:
		triggerer.reputation_add( 16 )
	game.global_vars[26] = game.global_vars[26] + 1
	if ( game.global_vars[26] >= 3 and triggerer.reputation_has( 17 ) == 0):
		triggerer.reputation_add( 17 )
	return RUN_DEFAULT