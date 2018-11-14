from toee import *
from scripts import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 260 )
	elif (game.global_flags[956] == 1) or (game.global_flags[957] == 1):
		triggerer.begin_dialog( attachee, 210 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.quests[81].state == qs_accepted and attachee.map == 5057):
		attachee.object_flag_unset(OF_OFF)
	elif (game.global_vars[953] == 1 and attachee.map == 5172):
		obj = attachee.leader_get()
		if (obj != OBJ_HANDLE_NULL):
			obj.follower_remove( attachee )
			game.global_vars[953] = 2
	elif (game.global_vars[953] == 3 and attachee.map == 5172):
		attachee.object_flag_set(OF_OFF)
		game.global_vars[953] = 4
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[958] = 1
	if (attachee.map == 5057):
		game.global_vars[961] = 5
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[958] = 0
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (attachee.map == 5057 or attachee.map == 5152 or attachee.map == 5008):
		kendrew = find_npc_near( attachee, 8717 )
		if (kendrew != OBJ_HANDLE_NULL):
			leader = kendrew.leader_get()
			if (leader != OBJ_HANDLE_NULL):
				leader.follower_remove(kendrew)
			kendrew.attack(triggerer)
		guntur = find_npc_near( attachee, 8716 )
		if (guntur != OBJ_HANDLE_NULL):
			leader = guntur.leader_get()
			if (leader != OBJ_HANDLE_NULL):
				leader.follower_remove(guntur)
			guntur.attack(triggerer)
	return RUN_DEFAULT


def san_join( attachee, triggerer ):
	boots = attachee.item_find( 6040 )
	boots.item_flag_set(OIF_NO_TRANSFER)
	gloves = attachee.item_find( 6021 )
	gloves.item_flag_set(OIF_NO_TRANSFER)
	kilt = attachee.item_find( 6438 )
	kilt.item_flag_set(OIF_NO_TRANSFER)
	armor = attachee.item_find( 6229 )
	armor.item_flag_set(OIF_NO_TRANSFER)
	sword = attachee.item_find( 4443 )
	sword.item_flag_set(OIF_NO_TRANSFER)
	return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	boots = attachee.item_find( 6040 )
	boots.item_flag_unset(OIF_NO_TRANSFER)
	gloves = attachee.item_find( 6021 )
	gloves.item_flag_unset(OIF_NO_TRANSFER)
	kilt = attachee.item_find( 6438 )
	kilt.item_flag_unset(OIF_NO_TRANSFER)
	armor = attachee.item_find( 6229 )
	armor.item_flag_unset(OIF_NO_TRANSFER)
	sword = attachee.item_find( 4443 )
	sword.item_flag_unset(OIF_NO_TRANSFER)
	return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		if ( attachee.map == 5169 ) or ( attachee.map == 5171 ):
			if (attachee.is_unconscious() == 0):
				attachee.float_line(2000,triggerer)
				attachee.runoff(attachee.location-3)
				game.timevent_add( go_away, ( attachee, ), 5000 )
			elif (attachee.is_unconscious() == 1):
				game.global_vars[953] = 1
		elif ( attachee.map == 5051 ):
			if (game.global_vars[942] == 0):
				game.global_vars[942] = 1
				game.timevent_add( stopwatch_for_time_in_party, ( attachee, ), 432000000 ) # 5 days
		elif (game.global_vars[942] == 2):
			attachee.float_line(3000,triggerer)
			attachee.runoff(attachee.location-3)
			game.timevent_add( go_away, ( attachee, ), 5000 )
	return RUN_DEFAULT


def go_away( attachee ):
	attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def stopwatch_for_time_in_party( attachee ):
	game.global_vars[942] = 2
	return RUN_DEFAULT