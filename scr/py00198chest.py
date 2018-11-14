from toee import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	obj = find_npc_near(attachee,8053)
	if (obj != OBJ_HANDLE_NULL):
		for pc in game.obj_list_vicinity(obj.location,OLC_PC):
			if (is_safe_to_talk(obj,pc)):
				pc.begin_dialog(obj,1)
				return SKIP_DEFAULT
	return SKIP_DEFAULT