from toee import *
from combat_standard_routines import *


def san_heartbeat( attachee, triggerer ):
	for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
		if (critter_is_unconscious(obj) == 0):
			#attachee.turn_towards(obj)
			if obj.distance_to( attachee ) < 30:
				if not game.tutorial_is_active():
					game.tutorial_toggle()
				game.tutorial_show_topic( TAG_TUT_ROOM6_OVERVIEW )
				game.new_sid = 0
				return RUN_DEFAULT
	return RUN_DEFAULT