from toee import *
from combat_standard_routines import *


def san_will_kos( attachee, triggerer ):
	saw_robe = 0
	for obj in triggerer.group_list():
		robe = obj.item_worn_at(12)
		if (robe != OBJ_HANDLE_NULL):
			if ( ( robe.name == 3020) or (robe.name == 3016 ) or (robe.name == 3017 ) or (robe.name == 3010) or (robe.name == 3021) ):
				saw_robe = 1
				break
	if (saw_robe):
		return SKIP_DEFAULT
	else:
		return RUN_DEFAULT
