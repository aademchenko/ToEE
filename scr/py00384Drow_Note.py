from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog(attachee,1)
	return SKIP_DEFAULT


def san_use( attachee, triggerer ):
	loc = triggerer.location
	n = 0
	for pc in game.party:
		item = pc.item_find_by_proto(9999)
		FLAGS = item.item_flags_get()
		if (FLAGS  & OIF_IDENTIFIED):
			n = 1
	if (attachee.name == 9999):
		if (n == 1):
			npc = game.obj_create( 14643, loc )
			triggerer.begin_dialog(npc,1)
		else:
			npc = game.obj_create( 14643, loc )
			triggerer.begin_dialog(npc,100)
	return SKIP_DEFAULT