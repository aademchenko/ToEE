from utilities import *
from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (not attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 1 )
	elif (attachee.has_met(triggerer) and game.global_vars[700] == 0):
		triggerer.begin_dialog( attachee, 120 )
	elif (game.global_vars[700] == 1):
		triggerer.begin_dialog( attachee, 100 )
	elif (game.global_vars[700] == 2):
		triggerer.begin_dialog( attachee, 110 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (not attachee.has_met(game.party[0])):
			if (is_cool_to_talk(attachee, game.party[0])):
				attachee.turn_towards(game.party[0])
				game.party[0].begin_dialog(attachee,1)
		elif (attachee.has_met(game.party[0]) and game.global_vars[700] == 0):
			if (is_cool_to_talk(attachee, game.party[0])):
				attachee.turn_towards(game.party[0])
				game.party[0].begin_dialog(attachee,120)
				game.new_sid = 0
		elif (game.global_vars[700] == 1):
			if (is_cool_to_talk(attachee, game.party[0])):
				attachee.turn_towards(game.party[0])
				game.party[0].begin_dialog(attachee,100)
	return RUN_DEFAULT


def is_cool_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 20):
		return 1
	return 0