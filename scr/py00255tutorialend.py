from toee import *
from combat_standard_routines import *


def san_heartbeat( attachee, triggerer ):
	for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
		if (critter_is_unconscious(obj) == 0):
			if attachee.distance_to( obj ) < 10:
				for pc in game.party:
					if ((pc.name == 8066) and (pc.stat_level_get( stat_hp_current ) >= 0)):
						game.moviequeue_add( 1028 )
						game.moviequeue_play_end_game()
						return RUN_DEFAULT
				game.moviequeue_add( 1029 )
				game.moviequeue_play_end_game()
				return RUN_DEFAULT
	return RUN_DEFAULT
