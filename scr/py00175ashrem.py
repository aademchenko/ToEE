from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 170 )
	elif (not attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 30 )
	else:
		triggerer.begin_dialog( attachee, 150 )
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


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		alrrem = find_npc_near(attachee,8047)
		if (alrrem != OBJ_HANDLE_NULL):
			if ( game.global_flags[192] == 0 ):
				triggerer.begin_dialog( attachee, 230 )
	return RUN_DEFAULT


def talk_Taki( attachee, triggerer, line ):
	taki = find_npc_near(attachee,8039)
	if (taki != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(taki,line)
		taki.turn_towards(attachee)
		attachee.turn_towards(taki)
	return SKIP_DEFAULT


def talk_Alrrem( attachee, triggerer, line ):
	alrrem = find_npc_near(attachee,8047)
	if (alrrem != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(alrrem,line)
		alrrem.turn_towards(attachee)
		attachee.turn_towards(alrrem)
	return SKIP_DEFAULT