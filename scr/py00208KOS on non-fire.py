from toee import *
from combat_standard_routines import *


def san_will_kos( attachee, triggerer ):
	if (game.global_flags[344] == 1):
		return SKIP_DEFAULT
	saw_ally_robe = 0
	saw_greater_robe = 0
	saw_enemy_robe = 0
	for obj in triggerer.group_list():
		robe = obj.item_worn_at(12)
		if (robe != OBJ_HANDLE_NULL):
			if ( robe.name == 3017 ):
				saw_ally_robe = 1
			elif ( robe.name == 3021 ):
				saw_greater_robe = 1
				break
			elif ( ( robe.name == 3020) or (robe.name == 3016 ) or (robe.name == 3010 ) ):
				saw_enemy_robe = 1
	if (saw_greater_robe):
		return SKIP_DEFAULT
	elif ((saw_ally_robe) and (not saw_enemy_robe)):
		return SKIP_DEFAULT
	else:
		return RUN_DEFAULT