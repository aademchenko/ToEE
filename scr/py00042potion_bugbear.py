from toee import *
from utilities import *
from combat_standard_routines import *


def san_start_combat( attachee, triggerer ):
	if (attachee != OBJ_HANDLE_NULL and critter_is_unconscious(attachee) != 1 and not attachee.d20_query(Q_Prone)):
		if (obj_percent_hp(attachee) <= 50):
			if (attachee.item_find(8014) != OBJ_HANDLE_NULL or attachee.item_find(8006) != OBJ_HANDLE_NULL or attachee.item_find(8007) != OBJ_HANDLE_NULL or attachee.item_find(8101) != OBJ_HANDLE_NULL):
				attachee.obj_set_int(obj_f_critter_strategy, 448)
			else:
				attachee.obj_set_int(obj_f_critter_strategy, 449)
		else:
			attachee.obj_set_int(obj_f_critter_strategy, 449)
	return RUN_DEFAULT