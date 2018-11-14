from utilities import *
from scripts import *
from __main__ import game
from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[961] == 1):
		if (not game.combat_is_active()):
			if (is_better_to_talk(attachee, game.party[0])):
				game.global_vars[961] = 2
				attachee.turn_towards(game.party[0])
				game.party[0].begin_dialog(attachee,160)
	return RUN_DEFAULT


def set_room_flag( attachee, triggerer ):
	game.global_flags[997] = 1
	game.timeevent_add( room_no_longer_available, (), 86390000 )
	game.sleep_status_update()
	return RUN_DEFAULT
	

def room_no_longer_available():
	game.global_flags[997] = 0
	game.sleep_status_update()
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 25):
		return 1
	return 0