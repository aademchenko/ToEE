from toee import *
from utilities import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	obj = find_npc_near(attachee,8002)
	if (obj != OBJ_HANDLE_NULL and critter_is_unconscious(obj) != 1):
		if (obj.leader_get() == OBJ_HANDLE_NULL):
			if (cant_see( triggerer, obj )):
				return RUN_DEFAULT
			else:
				triggerer.begin_dialog( obj, 1 )
				return SKIP_DEFAULT	
		elif ( game.global_flags[198] == 1 ):
			triggerer.begin_dialog( obj, 260 )
			return SKIP_DEFAULT
		elif (obj.leader_get() != OBJ_HANDLE_NULL):
			if (game.global_flags[53] == 1):
				triggerer.begin_dialog( obj, 320 )
				return SKIP_DEFAULT
			else:
				triggerer.begin_dialog( obj, 220 )
				return SKIP_DEFAULT
		elif ( game.global_flags[52] == 1 ):
				triggerer.begin_dialog( obj, 20 )
				return SKIP_DEFAULT
		elif ( game.global_flags[48] == 1 ):
				triggerer.begin_dialog( obj, 1 )
				return SKIP_DEFAULT
		else:
				triggerer.begin_dialog( obj, 10 )
				return SKIP_DEFAULT
	return RUN_DEFAULT



def cant_see( triggerer, obj ):
	if (obj.can_see(triggerer)):
		return 0
	return 1