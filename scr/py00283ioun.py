from toee import *
from utilities import *
from combat_standard_routines import *


def san_insert_item( attachee, triggerer ):
	if (triggerer.type == obj_t_pc or triggerer.type == obj_t_npc):
		game.particles( "sp-Magic Stone", triggerer )
	return RUN_DEFAULT

def san_new_map( attachee, triggerer ):		# Ron after moathouse
	st = attachee.obj_get_int( obj_f_npc_pad_i_5 )
	if (st == 0 and (attachee.stat_level_get(stat_level_cleric) == 17)):
		attachee.obj_set_int( obj_f_npc_pad_i_5, 1 )
		game.party[0].begin_dialog( attachee, 2000 )
	if (st == 1 and attachee.map == 5011):
		attachee.obj_set_int( obj_f_npc_pad_i_5, 2 )
		game.party[0].begin_dialog( attachee, 2070 )
		game.new_sid = 0
	return RUN_DEFAULT

## 1 when he has mentioned he needs to get to the church, 2 when he has done his spiel at the top floor, 3 when it is all done