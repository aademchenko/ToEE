from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog(attachee,1)
	return SKIP_DEFAULT


def san_use( attachee, triggerer ):
	loc = triggerer.location
	# if attachee.name == 11300:
		# npc = game.obj_create( 14456, loc )
		# triggerer.begin_dialog(npc,1)
	# if attachee.name == 11301:
		# npc = game.obj_create( 14457, loc )
		# triggerer.begin_dialog(npc,100)
	# if attachee.name == 11302:
		# npc = game.obj_create( 14457, loc )
		# triggerer.begin_dialog(npc,300)
	return SKIP_DEFAULT
	

def create_store( attachee, triggerer ):
	loc = attachee.location
	target = game.obj_create( 14456, loc)
#	triggerer.barter(target)
	triggerer.begin_dialog( target, 700 )
	return SKIP_DEFAULT
