from toee import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	for npc in game.obj_list_vicinity(attachee.location,OLC_NPC):
		if (npc.leader_get() == OBJ_HANDLE_NULL):
			npc.attack(triggerer)
	return RUN_DEFAULT