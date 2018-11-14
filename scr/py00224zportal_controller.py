from toee import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[30] >= 4):
		for obj in game.obj_list_vicinity(attachee.location,OLC_SCENERY):
			if (obj.name == 1609):
				obj.object_flag_unset(OF_DONTDRAW)
				attachee.destroy()
	return SKIP_DEFAULT
