from toee import *
from utilities import *
from scripts import *
from py00439script_daemon import *
from Co8 import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (game.global_vars[979] == 2) and (game.global_flags[980] == 1):
		triggerer.begin_dialog( attachee, 120 )
	elif (game.global_vars[979] == 1) and (is_daytime() == 1):
		triggerer.begin_dialog( attachee, 50 )
	elif (game.global_vars[979] == 1) and (is_daytime() == 0):
		triggerer.begin_dialog( attachee, 60 )
	elif (attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 70 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5170 or attachee.map == 5135):
		if (game.global_vars[948] == 1):
			attachee.object_flag_unset(OF_OFF)
		elif (game.global_vars[948] == 2):
			attachee.object_flag_set(OF_OFF)
	elif (attachee.map == 5169):
		if (game.global_vars[948] == 2) and tpsts('abiram_off_to_arrest', 1*60*60) == 0:
			attachee.object_flag_set(OF_OFF)
		elif (game.global_vars[948] == 3) or tpsts('abiram_off_to_arrest', 1*60*60):
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	game.global_flags[550] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[550] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if ((attachee.map == 5170 or attachee.map == 5135) and game.global_vars[948] == 1):
		if (not game.combat_is_active()):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_groovier_to_talk(attachee, obj)):
					game.timevent_add( start_talking, ( attachee, triggerer ), 2000 )
					game.new_sid = 0
	else:
		if ( (game.party[0].reputation_has(34) == 1 or game.party[0].reputation_has(35) == 1 or game.party[0].reputation_has(42) == 1 or game.party[0].reputation_has(44) == 1 or game.party[0].reputation_has(35) == 1 or game.party[0].reputation_has(43) == 1 or game.party[0].reputation_has(46) == 1 or (game.global_vars[993] == 5 and game.global_flags[870] == 0)) ):
			if ( (game.global_vars[969] == 0) and (game.global_flags[955] == 0) ):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (is_better_to_talk(attachee,obj)):
							attachee.turn_towards(obj)
							obj.begin_dialog( attachee, 140 )
							game.global_vars[969] = 1
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 50):
		return 1
	return 0


def is_groovier_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 40):
			return 1
	return 0


def start_talking( attachee, triggerer ):
	npc = find_npc_near(attachee,8703)
	attachee.turn_towards(npc)
	game.party[0].begin_dialog( attachee, 270 )
	return RUN_DEFAULT


def switch_to_wilfrick( attachee, triggerer, line):
	npc = find_npc_near(attachee,8703)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
		npc.turn_towards(triggerer)
	return SKIP_DEFAULT


def run_off( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT


def remove_panathaes( attachee, triggerer ):
	if anyone( triggerer.group_list(), "has_follower", 8791 ):
		for npc in game.party[0].group_list():
			if (npc.name == 8791 and npc.leader_get() != OBJ_HANDLE_NULL):
				triggerer.follower_remove(npc)
				for pc in game.party:
					npc.ai_shitlist_remove( pc )
					npc.reaction_set( pc, 50 )
	elif anyone( triggerer.group_list(), "has_follower", 8792 ):
		for npc in game.party[0].group_list():
			if (npc.name == 8792 and npc.leader_get() != OBJ_HANDLE_NULL):
				triggerer.follower_remove(npc)
				for pc in game.party:
					npc.ai_shitlist_remove( pc )
					npc.reaction_set( pc, 50 )
	elif anyone( triggerer.group_list(), "has_follower", 8793 ):
		for npc in game.party[0].group_list():
			if (npc.name == 8793 and npc.leader_get() != OBJ_HANDLE_NULL):
				triggerer.follower_remove(npc)
				for pc in game.party:
					npc.ai_shitlist_remove( pc )
					npc.reaction_set( pc, 50 )
	elif anyone( triggerer.group_list(), "has_follower", 8794 ):
		for npc in game.party[0].group_list():
			if (npc.name == 8794 and npc.leader_get() != OBJ_HANDLE_NULL):
				triggerer.follower_remove(npc)
				for pc in game.party:
					npc.ai_shitlist_remove( pc )
					npc.reaction_set( pc, 50 )
	elif anyone( triggerer.group_list(), "has_follower", 8795 ):
		for npc in game.party[0].group_list():
			if (npc.name == 8795 and npc.leader_get() != OBJ_HANDLE_NULL):
				triggerer.follower_remove(npc)
				for pc in game.party:
					npc.ai_shitlist_remove( pc )
					npc.reaction_set( pc, 50 )
	elif anyone( triggerer.group_list(), "has_follower", 8796 ):
		for npc in game.party[0].group_list():
			if (npc.name == 8796 and npc.leader_get() != OBJ_HANDLE_NULL):
				triggerer.follower_remove(npc)
				for pc in game.party:
					npc.ai_shitlist_remove( pc )
					npc.reaction_set( pc, 50 )
	elif anyone( triggerer.group_list(), "has_follower", 8797 ):
		for npc in game.party[0].group_list():
			if (npc.name == 8797 and npc.leader_get() != OBJ_HANDLE_NULL):
				triggerer.follower_remove(npc)
				for pc in game.party:
					npc.ai_shitlist_remove( pc )
					npc.reaction_set( pc, 50 )
	elif anyone( triggerer.group_list(), "has_follower", 8798 ):
		for npc in game.party[0].group_list():
			if (npc.name == 8798 and npc.leader_get() != OBJ_HANDLE_NULL):
				triggerer.follower_remove(npc)
				for pc in game.party:
					npc.ai_shitlist_remove( pc )
					npc.reaction_set( pc, 50 )
	game.global_vars[551] = 2
#	game.global_vars[549] = 2
	return RUN_DEFAULT


def remove_rakham( attachee, triggerer ):
	if anyone( triggerer.group_list(), "has_follower", 8766 ):
		for npc in game.party[0].group_list():
			if (npc.name == 8766 and npc.leader_get() != OBJ_HANDLE_NULL):
				triggerer.follower_remove(npc)
				for pc in game.party:
					npc.ai_shitlist_remove( pc )
					npc.reaction_set( pc, 50 )
	game.global_vars[549] = 3
	return RUN_DEFAULT


def remove_boroquin( attachee, triggerer ):
	if anyone( triggerer.group_list(), "has_follower", 8767 ):
		for npc in game.party[0].group_list():
			if (npc.name == 8767 and npc.leader_get() != OBJ_HANDLE_NULL):
				triggerer.follower_remove(npc)
				for pc in game.party:
					npc.ai_shitlist_remove( pc )
					npc.reaction_set( pc, 50 )
	game.global_vars[549] = 1
	return RUN_DEFAULT


def rep_routine( attachee, triggerer ):
	if (game.party[0].reputation_has(75)==1):
		game.party[0].reputation_add(78)
		game.party[0].reputation_remove(75)
	elif (game.party[0].reputation_has(76)==1):
		game.party[0].reputation_add(78)
		game.party[0].reputation_remove(76)
	elif (game.party[0].reputation_has(77)==1):
		game.party[0].reputation_add(78)
		game.party[0].reputation_remove(77)
	return