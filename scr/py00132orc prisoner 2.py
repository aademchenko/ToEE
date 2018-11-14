from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		if (game.global_flags[135] == 0):
			triggerer.begin_dialog( attachee, 70 )
		else:
			triggerer.begin_dialog( attachee, 110 )
	elif ((not attachee.has_met(triggerer)) or (game.global_flags[131] == 0)):
		if (game.global_flags[131] == 1):
			triggerer.begin_dialog( attachee, 30 )
		else:
			triggerer.begin_dialog( attachee, 1 )
	elif (game.global_flags[135] == 0):
			triggerer.begin_dialog( attachee, 50 )
	else:
			triggerer.begin_dialog( attachee, 120 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)
	game.global_flags[134] = 1
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[134] = 0
	return RUN_DEFAULT 


def tuelk_talk( attachee, triggerer, line):
	npc = find_npc_near(attachee,8026)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,40)
	return SKIP_DEFAULT


def ron_talk( attachee, triggerer, line):
	npc = find_npc_near(attachee,8730)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,130)
	return SKIP_DEFAULT