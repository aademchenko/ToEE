from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.has_met(triggerer)):
		attachee.turn_towards(triggerer)
		triggerer.begin_dialog( attachee, 20 )
	else:
		attachee.turn_towards(triggerer)
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if ( (game.quests[66].state == qs_accepted) and (attachee.map == 5061) ):	##turns on merchant bodyguards in Nulb Hostel
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_safe_to_talk(attachee,obj)):
				if (not attachee.has_met(obj)):
					attachee.turn_towards(obj)
					obj.begin_dialog(attachee,1)
				elif (attachee.has_met(obj)):
					attachee.turn_towards(obj)
					obj.begin_dialog(attachee,20)
	return RUN_DEFAULT