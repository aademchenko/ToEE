from toee import *


def san_use( attachee, triggerer ):
	if (triggerer.type == obj_t_pc):
		game.fade_and_teleport(0,0,0,5004,489,470)
	return SKIP_DEFAULT
