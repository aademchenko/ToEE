from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 120 )
	else:
		triggerer.begin_dialog( attachee, 1 )
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
	game.global_flags[700] = 1
	attachee.float_line(12014,triggerer)
	if (attachee.leader_get() != OBJ_HANDLE_NULL and attachee.map != 5091 and attachee.map != 5002):
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	attachee.float_line(12057,triggerer)
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[700] = 0
	return RUN_DEFAULT


def san_heartbeat(attachee, triggerer):
	if game.global_flags[700] == 1:
		attachee.object_flag_set(OF_OFF)
		return SKIP_DEFAULT
	return RUN_DEFAULT


def san_join( attachee, triggerer ):
	itemA = attachee.item_find(6047)
	if (itemA != OBJ_HANDLE_NULL):
		itemA.item_flag_set(OIF_NO_TRANSFER)
	itemB = attachee.item_find(6060)
	if (itemB != OBJ_HANDLE_NULL):
		itemB.item_flag_set(OIF_NO_TRANSFER)
	itemD = attachee.item_find(4036)
	if (itemD != OBJ_HANDLE_NULL):
		itemD.item_flag_set(OIF_NO_TRANSFER)
	return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	if ((attachee.map == 5066) or (attachee.map == 5067) or (attachee.map == 5105) or (attachee.map == 5080)):
		leader = attachee.leader_get()
		if (leader != OBJ_HANDLE_NULL):
			percent = group_pc_percent_hp(attachee, leader)
			if (percent < 30):
				if (obj_percent_hp(attachee) > 70):
					leader.begin_dialog( attachee, 320 )
	return RUN_DEFAULT


def switch_to_turuko( attachee, triggerer, line):
	npc = find_npc_near(attachee,8004)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
		npc.turn_towards(triggerer)
	return SKIP_DEFAULT


def they_attack(attachee, triggerer):
	for npc in game.obj_list_vicinity( attachee.location, OLC_NPC ):
		if npc.name == 14642 or npc.name == 14314 or npc.name == 14078 or npc.name == 14079 or npc.name == 14080:
			npc.attack(triggerer)
	kobort = find_npc_near(attachee, 8005)
	turuko = find_npc_near(attachee, 8004)
	attachee.attack(triggerer)
	kobort.attack(triggerer)
	turuko.attack(triggerer)
	return


def find_pm_nearest( obj ):
	distance = 1000000
	target = OBJ_HANDLE_NULL
	for pc in pc.group_list():
		if (obj.distance_to(pc) < distance):
			distance = obj.distance_to(pc)
			target = pc
	if (pc != OBJ_HANDLE_NULL):
		return target
	return OBJ_HANDLE_NULL


def equip_transfer( attachee, triggerer ):
	itemA = attachee.item_find(6047)
	if (itemA != OBJ_HANDLE_NULL):
		itemA.destroy()
		create_item_in_inventory( 6047, triggerer )
	itemB = attachee.item_find(6060)
	if (itemB != OBJ_HANDLE_NULL):
		itemB.destroy()
		create_item_in_inventory( 6060, triggerer )
	itemC = attachee.item_find(6045)
	if (itemC != OBJ_HANDLE_NULL):
		itemC.destroy()
		create_item_in_inventory( 6045, triggerer )
	itemD = attachee.item_find(4036)
	if (itemD != OBJ_HANDLE_NULL):
		itemD.destroy()
		create_item_in_inventory( 4036, triggerer )
	itemE = attachee.item_find(4060)
	if (itemE != OBJ_HANDLE_NULL):
		itemE.destroy()
		create_item_in_inventory( 4060, triggerer )
	create_item_in_inventory( 7001, attachee )
	create_item_in_inventory( 7001, attachee )
	create_item_in_inventory( 7001, attachee )
	create_item_in_inventory( 7001, attachee )
	create_item_in_inventory( 7001, attachee )
	create_item_in_inventory( 7001, attachee )
	create_item_in_inventory( 7001, attachee )
	create_item_in_inventory( 7001, attachee )
	create_item_in_inventory( 7002, attachee )
	return RUN_DEFAULT