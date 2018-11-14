from toee import *
from utilities import *
from combat_standard_routines import *


def san_will_kos( attachee, triggerer ):
	if (triggerer.type == obj_t_pc):
		if (game.global_flags[147] == 1 or game.global_flags[990] == 1):
			return RUN_DEFAULT
	return SKIP_DEFAULT