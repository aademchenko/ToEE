from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		if (game.global_flags[45] == 1):
			triggerer.begin_dialog( attachee, 100 )
		else:
			triggerer.begin_dialog( attachee, 1 )
	elif (game.global_flags[45] == 1):
		triggerer.begin_dialog( attachee, 250 )
	else:
		triggerer.begin_dialog( attachee, 200 )
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
	game.global_flags[44] = 1
	attachee.float_line(12014,triggerer)
	if (attachee.leader_get() != OBJ_HANDLE_NULL and attachee.map != 5091 and attachee.map != 5002):
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[44] = 0
	return RUN_DEFAULT


def san_heartbeat(attachee, triggerer):
	if game.global_flags[44] == 1:
		attachee.object_flag_set(OF_OFF)
		return SKIP_DEFAULT
	return RUN_DEFAULT


def san_join( attachee, triggerer ):
	if (not game.combat_is_active()):
		obj = find_npc_near( attachee, 8004)
		if (obj != OBJ_HANDLE_NULL and game.global_flags[806] == 0):
			triggerer.follower_add(obj)
	itemA = attachee.item_find(4205)
	if (itemA != OBJ_HANDLE_NULL):
		itemA.item_flag_set(OIF_NO_TRANSFER)
	itemD = attachee.item_find(6120)
	if (itemD != OBJ_HANDLE_NULL):
		itemD.item_flag_set(OIF_NO_TRANSFER)
	itemE = attachee.item_find(6059)
	if (itemE != OBJ_HANDLE_NULL):
		itemE.item_flag_set(OIF_NO_TRANSFER)
	return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	for obj in triggerer.group_list():
		if (obj.name == 8004 and game.global_flags[806] == 0):
			triggerer.follower_remove(obj)
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
		attachee.reaction_set( pc, 50 )
	return RUN_DEFAULT


def switch_to_turuko( attachee, triggerer, line):
	npc = find_npc_near(attachee,8004)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
	return SKIP_DEFAULT


def equip_transfer( attachee, triggerer ):
	itemA = attachee.item_find(4205)
	if (itemA != OBJ_HANDLE_NULL):
		itemA.destroy()
		create_item_in_inventory( 4205, triggerer )
	itemB = attachee.item_find(6026)
	if (itemB != OBJ_HANDLE_NULL):
		itemB.destroy()
		create_item_in_inventory( 6026, triggerer )
	itemC = attachee.item_find(6233)
	if (itemC != OBJ_HANDLE_NULL):
		itemC.destroy()
		create_item_in_inventory( 6233, triggerer )
	itemD = attachee.item_find(6120)
	if (itemD != OBJ_HANDLE_NULL):
		itemD.destroy()
		create_item_in_inventory( 6120, triggerer )
	itemE = attachee.item_find(6059)
	if (itemE != OBJ_HANDLE_NULL):
		itemE.destroy()
		create_item_in_inventory( 6059, triggerer )
	itemF = attachee.item_find(6045)
	if (itemF != OBJ_HANDLE_NULL):
		itemF.destroy()
		create_item_in_inventory( 6045, triggerer )
	itemG = attachee.item_find(4060)
	if (itemG != OBJ_HANDLE_NULL):
		itemG.destroy()
		create_item_in_inventory( 4060, triggerer )
	create_item_in_inventory( 7002, attachee )
	create_item_in_inventory( 7002, attachee )
	create_item_in_inventory( 7002, attachee )
	create_item_in_inventory( 7002, attachee )
	create_item_in_inventory( 7002, attachee )
	create_item_in_inventory( 7002, attachee )
	return RUN_DEFAULT