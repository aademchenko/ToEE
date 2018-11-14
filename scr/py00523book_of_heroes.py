from toee import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	loc = triggerer.location
	npc = game.obj_create( 14577, loc )
	if (npc.map == 5119):
		triggerer.begin_dialog( npc, 60 )
	elif (game.global_vars[994] != 0):
		if (game.quests[65].state != qs_completed):
			triggerer.begin_dialog( npc, 40 )
		else:
			triggerer.begin_dialog ( npc, 50)
	else:
		triggerer.begin_dialog( npc, 1 )
	return SKIP_DEFAULT