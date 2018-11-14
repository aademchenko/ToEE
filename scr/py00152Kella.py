from utilities import *
from combat_standard_routines import *
from toee import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 80 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	attachee.float_line(12057,triggerer)
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		game.timevent_add( ask_to_rejoin, (attachee, triggerer) , 1 )
	return RUN_DEFAULT


def ask_to_rejoin( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_safe_to_talk(attachee,obj)):
				obj.begin_dialog( attachee, 50 )
				return SKIP_DEFAULT
		game.timevent_add( ask_to_rejoin, (attachee, triggerer) , 1000 )
	return SKIP_DEFAULT


def run_off( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	return SKIP_DEFAULT


def switch_to_tarah( attachee, triggerer, line):
	npc = find_npc_near(attachee,8805)
	kella = find_npc_near(attachee,8070)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
		npc.turn_towards(kella)
		kella.turn_towards(npc)
	return SKIP_DEFAULT