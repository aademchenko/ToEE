from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		if (game.global_flags[134] == 0):
			triggerer.begin_dialog( attachee, 100 )
		else:
			triggerer.begin_dialog( attachee, 170 )
	elif ((not attachee.has_met(triggerer)) or (game.global_flags[131] == 0)):
		if (game.global_flags[131] == 1):
			triggerer.begin_dialog( attachee, 90 )
		else:
			triggerer.begin_dialog( attachee, 1 )
	elif (game.global_flags[134] == 0):
			triggerer.begin_dialog( attachee, 150 )
	else:
			triggerer.begin_dialog( attachee, 190 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)	# added by ShiningTed
	game.global_flags[135] = 1
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[135] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ): # added by ShiningTed
	if (not game.combat_is_active()):
		for obj in game.obj_list_vicinity(attachee.location,OLC_NPC):
			if (obj.name == 8730) and (attachee.map == 5066):
				if (attachee.can_see(obj)):
					game.party[0].begin_dialog(obj,700)
					game.new_sid = 0
	return RUN_DEFAULT


def san_join( attachee, triggerer ):
	obj = find_npc_near( attachee, 8025)
	if (obj != OBJ_HANDLE_NULL):
		triggerer.follower_add(obj)
	return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	for obj in triggerer.group_list():
		if (obj.name == 8025):
			triggerer.follower_remove(obj)
			for pc in game.party:
				obj.ai_shitlist_remove( pc )
				obj.reaction_set( pc, 50 )
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
		attachee.reaction_set( pc, 50 )
	return RUN_DEFAULT


def argue_ron( attachee, triggerer, line): # added by ShiningTed
	npc = find_npc_near(attachee,8730)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(triggerer)
		triggerer.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,300)
	return SKIP_DEFAULT


### The circumstances under which Tuelk and Pintark will join have been modified by ShiningTed to allow for parties using the PC Count patcher to have more than 3 NPCs. Tuelk and Pintark will still not be able to join a party of more than 6 (of course). However, the onus is now on the PLAYERS not to stupidly go over their NPC limit. ###