from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (triggerer.has_wielded(3005)):
		triggerer.begin_dialog(attachee,1)
		return SKIP_DEFAULT
	elif (triggerer.has_wielded(3021)):
		triggerer.begin_dialog(attachee,1)
		return SKIP_DEFAULT
	elif (triggerer.has_wielded(3020)):
		triggerer.begin_dialog(attachee,40)
		return SKIP_DEFAULT
	triggerer.begin_dialog(attachee,30)
	return SKIP_DEFAULT

def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		first_pc_seen = OBJ_HANDLE_NULL
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_safe_to_talk(attachee,obj)):
				if (first_pc_seen == OBJ_HANDLE_NULL):
					first_pc_seen = obj
				if (obj.has_wielded(3005)):
					obj.begin_dialog(attachee,1)
					game.new_sid = 0
					return RUN_DEFAULT
				elif (obj.has_wielded(3021)):
					obj.begin_dialog(attachee,1)
					game.new_sid = 0
					return RUN_DEFAULT
				elif (obj.has_wielded(3020)):
					obj.begin_dialog(attachee,40)
					game.new_sid = 0
					return RUN_DEFAULT
		if (first_pc_seen != OBJ_HANDLE_NULL):
			first_pc_seen.begin_dialog(attachee,30)
			game.new_sid = 0
	return RUN_DEFAULT