from toee import *
from utilities import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.has_met(triggerer)):
		triggerer.turn_towards(attachee)
		triggerer.begin_dialog( attachee, 30 )	
	else:
		triggerer.turn_towards(attachee)
		triggerer.begin_dialog( attachee, 1 )	
	return SKIP_DEFAULT


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
					game.new_sid = 0
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT