from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (anyone(triggerer.group_list(),"has_wielded",3017)):
		triggerer.begin_dialog( attachee, 160 )
	elif (anyone(triggerer.group_list(),"has_follower",8023)):
		triggerer.begin_dialog( attachee, 200 )
	elif (attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 170 )
	elif (anyone(triggerer.group_list(),"has_wielded",3016)):
		triggerer.begin_dialog( attachee, 1 )
	else:
		triggerer.begin_dialog( attachee, 100 )
	return SKIP_DEFAULT



def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT



def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_safe_to_talk(attachee,obj)):
				if (anyone(obj.group_list(),"has_wielded",3017)):
					obj.begin_dialog( attachee, 160 )
				elif (anyone(obj.group_list(),"has_follower",8023)):
					obj.begin_dialog( attachee, 200 )
				elif (attachee.has_met(obj)):
					obj.begin_dialog( attachee, 170 )
				elif (anyone(obj.group_list(),"has_wielded",3016) ):
					obj.begin_dialog( attachee, 1 )
				else:
					obj.begin_dialog( attachee, 100 )
				game.new_sid = 0
	return RUN_DEFAULT
