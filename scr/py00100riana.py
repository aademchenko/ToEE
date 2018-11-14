from toee import *
from utilities import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 170 )
	elif (game.global_flags[930] == 1):
		triggerer.begin_dialog( attachee, 10011 )
	elif (not attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 1 )
	else:
		triggerer.begin_dialog( attachee, 20 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5058 and game.global_flags[203] == 1 and game.global_flags[930] == 0):
		attachee.object_flag_unset(OF_OFF)
	elif (attachee.map != 5089) and (game.global_flags[930] == 1):
		attachee.object_flag_set(OF_OFF)
	elif (attachee.map == 5089) and (game.global_flags[930] == 1):
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	attachee.float_line(12057,triggerer)
	return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	for obj in triggerer.group_list():
		if (obj.name == 8056 and game.global_flags[806] == 0):
			triggerer.follower_remove(obj)
			triggerer.begin_dialog(attachee,1000)
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
		attachee.reaction_set( pc, 50 )
	return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	randy1 = game.random_range(1,12)
	if ((attachee.map == 5039) and randy1 >= 6):
		attachee.float_line(12094,triggerer)
	elif ((attachee.map == 5064) and randy1 >= 6):
		attachee.float_line(12069,triggerer)
	return RUN_DEFAULT


def together_again( attachee, triggerer ):
	for obj in triggerer.group_list():
		if (obj.name == 8056 and game.global_flags[806] == 0):
			triggerer.begin_dialog(attachee,1010)
	return RUN_DEFAULT


def buttin2( attachee, triggerer, line):
	npc = find_npc_near(attachee,8056)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	return SKIP_DEFAULT


def buttin3( attachee, triggerer, line):
	npc = find_npc_near(attachee,8015)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	return SKIP_DEFAULT


def switch_to_tarah( attachee, triggerer, line):
	npc = find_npc_near(attachee,8805)
	riana = find_npc_near(attachee,8058)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
		npc.turn_towards(riana)
		riana.turn_towards(npc)
	return SKIP_DEFAULT


def get_rep( attachee, triggerer ):
	if triggerer.reputation_has( 7 ) == 0:
		triggerer.reputation_add( 7 )
	game.global_vars[25] = game.global_vars[25] + 1
	if ( game.global_vars[25] >= 3 and triggerer.reputation_has( 8 ) == 0):
		triggerer.reputation_add( 8 )
	return RUN_DEFAULT


def disappear( attachee ):
	attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT