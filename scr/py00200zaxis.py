from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.leader_get() == OBJ_HANDLE_NULL and game.global_flags[877] == 0 and not attachee.has_met(triggerer)):
		triggerer.begin_dialog(attachee,1)
	elif (attachee.leader_get() == OBJ_HANDLE_NULL and game.global_flags[877] == 1 and not attachee.has_met(triggerer)):
		triggerer.begin_dialog(attachee,200)
	elif (attachee.leader_get() == OBJ_HANDLE_NULL and attachee.has_met(triggerer)):
		triggerer.begin_dialog(attachee,280)
	else:
		triggerer.begin_dialog(attachee,80)
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5057):
		if (game.global_flags[877] == 1 and game.global_flags[880] == 0):
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	attachee.float_line(12057,triggerer)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)
	return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	randy1 = game.random_range(1,12)
	if ((attachee.map == 5066) and randy1 >= 9):
		attachee.float_line(12095,triggerer)
	elif ((attachee.map == 5058) and randy1 >= 11):
		attachee.float_line(12054,triggerer)
	elif ((attachee.map == 5059) and randy1 >= 5):
		attachee.float_line(12092,triggerer)
	elif ((attachee.map == 5057) and randy1 >= 9):
		attachee.float_line(12100,triggerer)
	return RUN_DEFAULT


def zaxis_runs_off( attachee, triggerer ):
	game.global_flags[877] = 1
	game.global_flags[879] = 1
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT


def zaxis_runs_off2( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT


def equip_transfer( attachee, triggerer ):
	itemA = attachee.item_find(6011)
	if (itemA != OBJ_HANDLE_NULL):
		itemA.destroy()
		create_item_in_inventory( 6011, triggerer )
	itemB = attachee.item_find(6012)
	if (itemB != OBJ_HANDLE_NULL):
		itemB.destroy()
		create_item_in_inventory( 6012, triggerer )
	itemC = attachee.item_find(6045)
	if (itemC != OBJ_HANDLE_NULL):
		itemC.destroy()
		create_item_in_inventory( 6045, triggerer )
	itemD = attachee.item_find(6091)
	if (itemD != OBJ_HANDLE_NULL):
		itemD.destroy()
		create_item_in_inventory( 6091, triggerer )
	itemE = attachee.item_find(4009)
	if (itemE != OBJ_HANDLE_NULL):
		itemE.destroy()
		create_item_in_inventory( 4009, triggerer )
	itemF = attachee.item_find(12562)
	if (itemF != OBJ_HANDLE_NULL):
		itemF.destroy()
		create_item_in_inventory( 12562, triggerer )
	itemG = attachee.item_find(12561)
	if (itemG != OBJ_HANDLE_NULL):
		itemG.destroy()
		create_item_in_inventory( 12561, triggerer )
	itemH = attachee.item_find(12563)
	if (itemH != OBJ_HANDLE_NULL):
		itemH.destroy()
		create_item_in_inventory( 12563, triggerer )
	itemI = attachee.item_find(12564)
	if (itemI != OBJ_HANDLE_NULL):
		itemI.destroy()
		create_item_in_inventory( 12564, triggerer )
	itemJ = attachee.item_find(12584)
	if (itemJ != OBJ_HANDLE_NULL):
		itemJ.destroy()
		create_item_in_inventory( 12584, triggerer )
	itemK = attachee.item_find(12585)
	if (itemK != OBJ_HANDLE_NULL):
		itemK.destroy()
		create_item_in_inventory( 12585, triggerer )
	itemL = attachee.item_find(12586)
	if (itemL != OBJ_HANDLE_NULL):
		itemL.destroy()
		create_item_in_inventory( 12586, triggerer )
	itemM = attachee.item_find(12587)
	if (itemM != OBJ_HANDLE_NULL):
		itemM.destroy()
		create_item_in_inventory( 12587, triggerer )
	create_item_in_inventory( 7003, attachee )
	create_item_in_inventory( 7003, attachee )
	create_item_in_inventory( 7003, attachee )
	create_item_in_inventory( 7002, attachee )
	create_item_in_inventory( 7002, attachee )
	create_item_in_inventory( 7002, attachee )
	create_item_in_inventory( 7002, attachee )
	create_item_in_inventory( 7002, attachee )
	return RUN_DEFAULT