from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 100 )
	elif (game.global_flags[931] == 1):
		triggerer.begin_dialog( attachee, 10011 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map != 5089) and (game.global_flags[931] == 1):
		attachee.object_flag_set(OF_OFF)
	elif (attachee.map == 5089) and (game.global_flags[931] == 1):
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)
	game.quests[59].state = qs_botched
	return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	randy1 = game.random_range(1,12)
	if ((attachee.map == 5113) and randy1 >= 5):
		attachee.float_line(12080,triggerer)
		game.new_sid = 0
	return RUN_DEFAULT


def san_join( attachee, triggerer ):
	ring = attachee.item_find( 6088 )
	ring.item_flag_set(OIF_NO_TRANSFER)
	return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	for obj in triggerer.group_list():
		if (obj.name == 8058 and game.global_flags[806] == 0):
			triggerer.follower_remove(obj)
			triggerer.begin_dialog(attachee,1000)
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
		attachee.reaction_set( pc, 50 )
	ring = attachee.item_find( 6088 )
	ring.item_flag_unset(OIF_NO_TRANSFER)
	return RUN_DEFAULT


def together_again( attachee, triggerer ):
	for obj in triggerer.group_list():
		if (obj.name == 8058 and game.global_flags[806] == 0):
			triggerer.begin_dialog(attachee,1010)
	return RUN_DEFAULT


def buttin( attachee, triggerer, line):
	npc = find_npc_near(attachee,8058)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,240)
	return SKIP_DEFAULT


def buttin2( attachee, triggerer, line):
	npc = find_npc_near(attachee,8058)
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
	else:
		triggerer.begin_dialog(attachee,170)
	return SKIP_DEFAULT


def switch_to_tarah( attachee, triggerer, line):
	npc = find_npc_near(attachee,8805)
	serena = find_npc_near(attachee,8056)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
		npc.turn_towards(serena)
		serena.turn_towards(npc)
	return SKIP_DEFAULT