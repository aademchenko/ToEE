#### Added by Ranth for High Level Expansion
from toee import *
from utilities import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 100)
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[501] == 3 and is_daytime() == 0):
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_vars[511] = game.global_vars[511] + 1
	if (game.global_vars[511] >= 24 and game.global_flags[501] == 1):
		game.global_flags[511] = 1
		if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
			game.quests[97].state = qs_completed
			game.party[0].reputation_add( 52 )
			game.global_vars[501] = 7
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (game.global_vars[505] == 0):
		game.timevent_add( out_of_time, ( attachee, triggerer ), 7200000 )	# 2 hours
		game.global_vars[505] = 1
	if (triggerer.type == obj_t_pc):
		if anyone( triggerer.group_list(), "has_follower", 8736 ):
			wakefield = find_npc_near( triggerer, 8736 )
			if (wakefield != OBJ_HANDLE_NULL):
				triggerer.follower_remove(wakefield)
				wakefield.float_line( 20000,triggerer )
				wakefield.attack(triggerer)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.quests[97].state == qs_botched):
		attachee.object_flag_set(OF_OFF)
	elif (game.global_vars[503] == 0):
		attachee.cast_spell(spell_stoneskin, attachee)
		game.global_vars[503] = 1
	return RUN_DEFAULT


def switch_to_ariakas( attachee, triggerer, line):
	npc = find_npc_near(attachee,8731)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
	return SKIP_DEFAULT


def dump_old_man( attachee, triggerer ):
	attachee.object_flag_set(OF_OFF)
	game.sound ( 4035, 1 )
	game.particles( "sp-Teleport", attachee )
	return RUN_DEFAULT


def shake( attachee, triggerer ):
	game.sound( 4130 )
	game.shake(50,6400)
	return


def out_of_time( attachee, triggerer ):
	game.global_vars[505] = 3
	return