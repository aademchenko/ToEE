from toee import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	game.global_vars[12] = game.global_vars[12] + 1
	if attachee.name == 8065:
		x = attachee.obj_get_int(obj_f_critter_flags2)
		x = x | 64
		attachee.obj_set_int(obj_f_critter_flags2, x)
	return RUN_DEFAULT