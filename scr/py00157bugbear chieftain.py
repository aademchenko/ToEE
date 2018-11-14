from toee import *
from utilities import *
from py00439script_daemon import record_time_stamp, get_v, set_v, inc_v, get_f, set_f, npc_set, npc_unset, npc_get, tsc, tpsts, within_rect_by_corners
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if get_v(454) & (2**1) != 0 and game.global_flags[108] == 0: # Water Temple regrouped, and he's stuck there
		if (not attachee.has_met(triggerer)):
			if ( anyone(triggerer.group_list(),"has_wielded",3017) ):
				triggerer.begin_dialog( attachee, 140 )
			else:
				triggerer.begin_dialog( attachee, 1000 )
		else:
			if get_f('realized_grurz_new_situation') == 1:
				if get_v('grurz_float_counter') < 5:
					rand1 = game.random_range(0,1)
					attachee.float_line(1100 + rand1, triggerer)
					inc_v('grurz_float_counter')
				elif get_v('grurz_float_counter') == 5:
					attachee.float_line(1102, triggerer)
					inc_v('grurz_float_counter')
				elif get_v('grurz_float_counter') == 6:
					attachee.float_line(1103, triggerer)
					inc_v('grurz_float_counter')
				elif get_v('grurz_float_counter') == 7:
					attachee.float_line(1104, triggerer)
					inc_v('grurz_float_counter')
				elif get_v('grurz_float_counter') == 8:
					attachee.float_line(1105, triggerer)
					attachee.attack(triggerer)
			else:
				triggerer.begin_dialog( attachee, 900 )
		
	elif (not attachee.has_met(triggerer)):
		if ( anyone(triggerer.group_list(),"has_follower",8023) ):
			triggerer.begin_dialog( attachee, 60 )
		elif ( anyone(triggerer.group_list(),"has_wielded",3020) ):
			triggerer.begin_dialog( attachee, 120 )
		elif ( anyone(triggerer.group_list(),"has_wielded",3017) ):
			triggerer.begin_dialog( attachee, 140 )
		else:
			triggerer.begin_dialog( attachee, 1 )
	else:
			triggerer.begin_dialog( attachee, 100 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_vars[11] = game.global_vars[11] + 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_vars[11] = game.global_vars[11] - 1
	return RUN_DEFAULT