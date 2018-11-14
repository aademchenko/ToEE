from toee import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[341] == 1):
		for obj in game.obj_list_vicinity(attachee.location,OLC_SCENERY):
			if (obj.name == 1610):
				obj.object_flag_unset(OF_DONTDRAW)
			elif (obj.name == 1616):
				obj.destroy()
			elif (obj.name == 1617):
				obj.destroy()
		loc = location_from_axis( 489, 396 )
		throne = game.obj_create( 2090, loc )
		if (throne != OBJ_HANDLE_NULL):
			throne.rotation = 2.3561945
		attachee.destroy()
	return SKIP_DEFAULT
