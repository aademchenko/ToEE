from toee import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (not attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 1 )
	elif ( game.global_flags[93] == 1 ):
		triggerer.begin_dialog( attachee, 180 )
	else:
		triggerer.begin_dialog( attachee, 240 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active() and game.party[0].reputation_has( 23 ) == 1 and game.global_flags[94] == 1 and game.global_vars[706] == 0):
		game.timevent_add( set_heads_up_var, ( attachee, triggerer ), 172800000 )	# 2 days
		game.global_vars[706] = 1
	elif (not game.combat_is_active() and game.party[0].reputation_has( 23 ) == 1 and game.global_flags[94] == 1 and game.global_vars[706] == 2):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_safe_to_talk(attachee,obj)):
				obj.turn_towards(attachee)
				attachee.turn_towards(obj)
				obj.begin_dialog(attachee,400)
				game.global_vars[706] = 3
	return RUN_DEFAULT


def buttin( attachee, triggerer, line):
	npc = find_npc_near(attachee,8020)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,220)
	return SKIP_DEFAULT


def set_heads_up_var( attachee, triggerer ):
	game.global_vars[706] = 2
	return RUN_DEFAULT