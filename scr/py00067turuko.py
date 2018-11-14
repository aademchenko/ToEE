from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		if (game.global_flags[44] == 1):
			triggerer.begin_dialog( attachee, 200 )
		else:
			triggerer.begin_dialog( attachee, 1 )
	elif (game.global_flags[44] == 1):
		triggerer.begin_dialog( attachee, 400 )
	else:
		triggerer.begin_dialog( attachee, 300 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		if (attachee.map == 5007 or attachee.map == 5008):
			if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
				attachee.object_flag_set(OF_OFF)
			else:
				attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)
	if (attachee.leader_get() != OBJ_HANDLE_NULL and attachee.map != 5091 and attachee.map != 5002):
		game.global_vars[29] = game.global_vars[29] + 1
	game.global_flags[45] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[45] = 0
	return RUN_DEFAULT


def san_heartbeat(attachee, triggerer):
	if game.global_flags[45] == 1:
		attachee.object_flag_set(OF_OFF)
		return SKIP_DEFAULT
	return RUN_DEFAULT


def san_join( attachee, triggerer ):
	if (not game.combat_is_active()):
		obj = find_npc_near( attachee, 8005)
		if (obj != OBJ_HANDLE_NULL and game.global_flags[806] == 0):
			triggerer.follower_add(obj)
		return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	for obj in triggerer.group_list():
		if (obj.name == 8005 and game.global_flags[806] == 0):
			triggerer.follower_remove(obj)
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
		attachee.reaction_set( pc, 50 )
	return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	if ((attachee.map == 5062) or (attachee.map == 5111) or (attachee.map == 5112) or (attachee.map == 5002) or (attachee.map == 5091)):
		leader = attachee.leader_get()
		if (leader != OBJ_HANDLE_NULL):
			percent = group_kobort_percent_hp(attachee, leader)
			if (percent < 30):
				if (obj_percent_hp(attachee) > 70):
					leader.begin_dialog( attachee, 420 )
	return RUN_DEFAULT


def switch_to_zert( attachee, triggerer, line):
	npc = find_npc_near(attachee,8010)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
		npc.turn_towards(triggerer)
	return SKIP_DEFAULT


def run_off( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	obj = find_npc_near( attachee, 8005)
	if (obj != OBJ_HANDLE_NULL):
		obj.runoff(obj.location-3)
	return RUN_DEFAULT


def equip_transfer( attachee, triggerer ):
	itemA = attachee.item_find(4110)
	if (itemA != OBJ_HANDLE_NULL):
		itemA.destroy()
		create_item_in_inventory( 4110, triggerer )
	itemB = attachee.item_find(4060)
	if (itemB != OBJ_HANDLE_NULL):
		itemB.destroy()
		create_item_in_inventory( 4060, triggerer )
	itemC = attachee.item_find(4060)
	if (itemC != OBJ_HANDLE_NULL):
		itemC.destroy()
		create_item_in_inventory( 4060, triggerer )
	itemD = attachee.item_find(6203)
	if (itemD != OBJ_HANDLE_NULL):
		itemD.destroy()
		create_item_in_inventory( 6203, triggerer )
	itemE = attachee.item_find(6202)
	if (itemE != OBJ_HANDLE_NULL):
		itemE.destroy()
		create_item_in_inventory( 6202, triggerer )
	itemF = attachee.item_find(6025)
	if (itemF != OBJ_HANDLE_NULL):
		itemF.destroy()
		create_item_in_inventory( 6025, triggerer )
	create_item_in_inventory( 7001, attachee )
	create_item_in_inventory( 7001, attachee )
	create_item_in_inventory( 7001, attachee )
	return RUN_DEFAULT


def talk_to_cleric( attachee, triggerer, line):
	npc = find_npc_near(attachee,14717)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,460)
	return SKIP_DEFAULT