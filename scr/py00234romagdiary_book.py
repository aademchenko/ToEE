from toee import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	loc = triggerer.location
	npc = game.obj_create( 14427, loc )
	triggerer.begin_dialog(npc,1)
	return SKIP_DEFAULT
