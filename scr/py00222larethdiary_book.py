from toee import *
from utilities import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	loc = triggerer.location
	npc = game.obj_create( 14413, loc )
	obj = find_npc_near(triggerer,8002)
	if (obj != OBJ_HANDLE_NULL):
		if (obj.leader_get() != OBJ_HANDLE_NULL and obj.distance_to(triggerer) <= 15):
			where = triggerer.location
			where = where - 1
			obj.move(where)
			obj.turn_towards(triggerer)
			triggerer.turn_towards(obj)
			if ( game.global_flags[198] == 1 ):
				triggerer.begin_dialog( obj, 1000 )
			elif (obj.leader_get() != OBJ_HANDLE_NULL):
				if (game.global_flags[53] == 1):
					triggerer.begin_dialog( obj, 1100 )
				else:
					triggerer.begin_dialog( obj, 1200 )
			elif ( game.global_flags[52] == 1 ):
				triggerer.begin_dialog( obj, 1300 )
			elif ( game.global_flags[48] == 1 ):
				triggerer.begin_dialog( obj, 1400 )
			else:
				triggerer.begin_dialog( obj, 1500 )
		else:
#			if (game.global_vars[701] == 2):
#				triggerer.begin_dialog( npc,1 )
#			else:
			triggerer.begin_dialog( npc,1 )

#	elif (game.global_vars[701] == 2):
#		triggerer.begin_dialog( npc,1 )
	else:
		triggerer.begin_dialog( npc,1 )
	return SKIP_DEFAULT
