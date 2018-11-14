from utilities import *
from combat_standard_routines import *
from toee import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.name == 14083 and attachee.leader_get() == OBJ_HANDLE_NULL and attachee.map == 5094):
		loc = attachee.location
		attachee.destroy()
		monsterD = game.obj_create( 14615, loc )
		monsterD.concealed_set(1)
		return RUN_DEFAULT
	if (attachee.name == 14123 and attachee.leader_get() == OBJ_HANDLE_NULL and attachee.map == 5094):
		loc = attachee.location
		attachee.destroy()
		monsterD = game.obj_create( 14616, loc )
		monsterD.concealed_set(1)
		return RUN_DEFAULT
	itemA = attachee.item_find(4096)
	itemB = attachee.item_find(4097)
	itemC = attachee.item_find(4117)
	if (attachee.name == 14107 and attachee.leader_get() == OBJ_HANDLE_NULL and attachee.map == 5094 and (itemA != OBJ_HANDLE_NULL or itemB != OBJ_HANDLE_NULL or itemC != OBJ_HANDLE_NULL)):
		loc = attachee.location
		attachee.destroy()
		monsterD = game.obj_create( 14603, loc )
		monsterD.concealed_set(1)
		return RUN_DEFAULT
	if (attachee.name == 14107 and attachee.leader_get() == OBJ_HANDLE_NULL and attachee.map == 5094):
		loc = attachee.location
		attachee.destroy()
		monsterD = game.obj_create( 14600, loc )
		monsterD.concealed_set(1)
		return RUN_DEFAULT
	if (itemA != OBJ_HANDLE_NULL and attachee.leader_get() == OBJ_HANDLE_NULL):
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
	if (itemB != OBJ_HANDLE_NULL and attachee.leader_get() == OBJ_HANDLE_NULL):
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
	if (itemA != OBJ_HANDLE_NULL and attachee.leader_get() != OBJ_HANDLE_NULL):
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
	if (itemB != OBJ_HANDLE_NULL and attachee.leader_get() != OBJ_HANDLE_NULL):
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
	game.new_sid = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.name == 14083 and attachee.leader_get() == OBJ_HANDLE_NULL and attachee.map == 5094):
		loc = attachee.location
		attachee.destroy()
		monsterD = game.obj_create( 14615, loc )
		monsterD.concealed_set(1)
		return RUN_DEFAULT
	if (attachee.name == 14123 and attachee.leader_get() == OBJ_HANDLE_NULL and attachee.map == 5094):
		loc = attachee.location
		attachee.destroy()
		monsterD = game.obj_create( 14616, loc )
		monsterD.concealed_set(1)
		return RUN_DEFAULT
	itemA = attachee.item_find(4096)
	itemB = attachee.item_find(4097)
	itemC = attachee.item_find(4117)
	if (attachee.name == 14107 and attachee.leader_get() == OBJ_HANDLE_NULL and attachee.map == 5094 and (itemA != OBJ_HANDLE_NULL or itemB != OBJ_HANDLE_NULL or itemC != OBJ_HANDLE_NULL)):
		loc = attachee.location
		attachee.destroy()
		monsterD = game.obj_create( 14603, loc )
		monsterD.concealed_set(1)
		return RUN_DEFAULT
	if (attachee.name == 14107 and attachee.leader_get() == OBJ_HANDLE_NULL and attachee.map == 5094):
		loc = attachee.location
		attachee.destroy()
		monsterD = game.obj_create( 14600, loc )
		monsterD.concealed_set(1)
		return RUN_DEFAULT
	if (itemA != OBJ_HANDLE_NULL and attachee.leader_get() == OBJ_HANDLE_NULL):
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
	if (itemB != OBJ_HANDLE_NULL and attachee.leader_get() == OBJ_HANDLE_NULL):
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
	if (itemA != OBJ_HANDLE_NULL and attachee.leader_get() != OBJ_HANDLE_NULL):
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
	if (itemB != OBJ_HANDLE_NULL and attachee.leader_get() != OBJ_HANDLE_NULL):
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
		create_item_in_inventory ( 5005, attachee )
	game.new_sid = 0
	return RUN_DEFAULT