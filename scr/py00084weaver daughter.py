from toee import *
from utilities import find_npc_near
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.leader.reputation_has(32) == 1 or game.leader.reputation_has(30) == 1 or game.leader.reputation_has(29) == 1):
		attachee.float_line(11001,triggerer)
	else:
		attachee.turn_towards(triggerer)
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT

def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[698] == 5):
		game.obj_create( 14699, location_from_axis (476L, 595L) )
		game.global_vars[698] = game.global_vars[698] + 1
	return RUN_DEFAULT

def argue( attachee, triggerer, line):
	npc = find_npc_near(attachee,8007)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,30)
	return SKIP_DEFAULT

def make_hate( attachee, triggerer ):
	r = attachee.reaction_get( triggerer )
	if ( r > 20 ):
		n = 20 - r
		attachee.reaction_adj( triggerer, n)
	return SKIP_DEFAULT
