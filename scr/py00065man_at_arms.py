from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 1 )
	else:
		triggerer.begin_dialog( attachee, 30 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
			attachee.object_flag_set(OF_OFF)
		else:
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
	if (triggerer.type == obj_t_pc):
		leader = attachee.leader_get()
		if (leader != OBJ_HANDLE_NULL):
			leader.follower_remove(attachee)
		if ( game.global_flags[47] == 1 ):
			if (leader != OBJ_HANDLE_NULL):
				if (obj_percent_hp(attachee) > 70):
					if (group_percent_hp(leader) < 30):
						attachee.float_line(110,triggerer)
						attachee.attack(leader)
		if (obj_percent_hp(attachee) < 30):
			leader = attachee.leader_get()
			if (leader != OBJ_HANDLE_NULL):
				attachee.float_line(120,leader)
				leader.follower_remove(attachee)
				attachee.runoff(attachee.location-3)
	return RUN_DEFAULT	


def run_off( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT


def equip_transfer( attachee, triggerer ):
	itemA = attachee.item_find(4036)
	if (itemA != OBJ_HANDLE_NULL):
		itemA.destroy()
		create_item_in_inventory( 4036, triggerer )
	itemB = attachee.item_find(4087)
	if (itemB != OBJ_HANDLE_NULL):
		itemB.destroy()
		create_item_in_inventory( 4087, triggerer )
	itemC = attachee.item_find(6010)
	if (itemC != OBJ_HANDLE_NULL):
		itemC.destroy()
		create_item_in_inventory( 6010, triggerer )
	itemD = attachee.item_find(6011)
	if (itemD != OBJ_HANDLE_NULL):
		itemD.destroy()
		create_item_in_inventory( 6011, triggerer )
	itemE = attachee.item_find(6012)
	if (itemE != OBJ_HANDLE_NULL):
		itemE.destroy()
		create_item_in_inventory( 6012, triggerer )
	itemF = attachee.item_find(6013)
	if (itemF != OBJ_HANDLE_NULL):
		itemF.destroy()
		create_item_in_inventory( 6013, triggerer )
	create_item_in_inventory( 7002, attachee )
	create_item_in_inventory( 7002, attachee )
	create_item_in_inventory( 7001, attachee )
	create_item_in_inventory( 7001, attachee )
	return RUN_DEFAULT