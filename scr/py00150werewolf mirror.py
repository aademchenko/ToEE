from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.global_flags[154] == 0 and game.global_flags[155] == 0):
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT

def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (game.global_flags[154] == 0 and game.global_flags[155] == 0):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_safe_to_talk(attachee,obj)):
					if (attachee.distance_to(obj) <= 10):
						obj.begin_dialog( attachee, 1 )
	return RUN_DEFAULT