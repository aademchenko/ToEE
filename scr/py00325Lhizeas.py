from toee import *
from utilities import *
from scripts import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (not attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 10 )
	else:
		if (game.global_vars[56] == 1):
			triggerer.begin_dialog( attachee, 70 )
		elif (game.global_vars[56] == 2):
			triggerer.begin_dialog( attachee, 60 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_better_to_talk(attachee, obj)):
				attachee.turn_towards(obj)
				obj.begin_dialog( attachee, 10 )
				game.new_sid = 0
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 45):
			return 1
	return 0