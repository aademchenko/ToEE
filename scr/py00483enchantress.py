#### Added by Ranth for High Level Expansion
from toee import *
from utilities import *
from combat_standard_routines import *


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
	if (game.global_vars[502] == 0):
		attachee.cast_spell(spell_mage_armor, attachee)
		game.global_vars[502] = 1
	return RUN_DEFAULT


def out_of_time( attachee, triggerer ):
	game.global_vars[505] = 3
	return