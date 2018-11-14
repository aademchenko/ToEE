from toee import *
from utilities import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[991] <= 2):
		game.sound( 4037, 1 )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_safe_to_talk(attachee,obj)):
				attachee.turn_towards(obj)
				obj.begin_dialog(attachee,1)
	return RUN_DEFAULT


def kill_spirit( attachee, triggerer ):
	game.particles( "CounterSpell", attachee )
	game.global_vars[991] = 3
	attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT