from toee import *
from combat_standard_routines import *


def san_use( attachee, triggerer):
	loct = attachee.location
	npcboris = game.obj_create( 14800, loct)
	if (attachee.map == 5001):
		triggerer.begin_dialog(npcboris,1)
	if (attachee.map == 5051):
		triggerer.begin_dialog(npcboris,200)
	if (attachee.map == 5121):
		triggerer.begin_dialog(npcboris,400)
	return SKIP_DEFAULT

def san_first_heartbeat( attachee, triggerer ):
#	if (attachee.map == 5019):
#		game.fade_and_teleport(0,0,0,game.global_vars[830],game.global_vars[831],game.global_vars[832])
	dummy = 1
	return SKIP_DEFAULT