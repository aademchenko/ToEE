from toee import *
from utilities import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (game.global_vars[969] == 1):
		triggerer.begin_dialog( attachee, 1 )
	else:
		return RUN_DEFAULT
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[969] == 2):
		attachee.object_flag_unset(OF_OFF)
	elif (game.global_vars[969] != 2):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (is_better_to_talk(attachee, game.party[0])):
			if (game.global_vars[969] == 2):
				attachee.turn_towards(triggerer)
				game.party[0].begin_dialog( attachee, 1 )
				game.global_vars[969] = 3
			elif (game.global_vars[969] == 4 and game.global_vars[993] == 8):
				attachee.turn_towards(triggerer)
				game.party[0].begin_dialog( attachee, 10 )
				game.global_vars[969] = 5
			elif (game.global_vars[969] == 4 and game.global_vars[993] != 8):
				attachee.turn_towards(triggerer)
				game.party[0].begin_dialog( attachee, 240 )
				game.global_vars[969] = 5
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 20):
		return 1
	return 0


def clear_reps( attachee, triggerer ):
	game.party[0].reputation_remove(35)	# Constable Killer
	game.party[0].reputation_remove(34)	# Slaughterer of Verbobonc
	if (game.global_vars[993] == 8):
		game.global_vars[993] = 9	# removes Dyvers rescuer murder arrest status
	return RUN_DEFAULT