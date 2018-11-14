from toee import *
from scripts import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (game.quests[96].state == qs_completed):
		triggerer.begin_dialog( attachee, 110 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
		attachee.object_flag_set(OF_OFF)
	else:
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
		attachee.object_flag_set(OF_OFF)
	else:
		if (attachee.name != 8073 and attachee.name != 8074 and attachee.name != 14019):
			attachee.object_flag_unset(OF_OFF)
		elif (attachee.name == 8073):
			if (is_daytime() != 1):
				attachee.object_flag_set(OF_OFF)
			elif (is_daytime() == 1):
				attachee.object_flag_unset(OF_OFF)
		elif (attachee.name == 8074):
			if (is_daytime() != 1):
				attachee.object_flag_unset(OF_OFF)
			elif (is_daytime() == 1):
				attachee.object_flag_set(OF_OFF)
		elif (attachee.name == 14019):				# otello of the field
			if (game.quests[9].state == qs_accepted):
				if (is_daytime() == 0):
					attachee.object_flag_unset(OF_OFF)
				else:
					attachee.object_flag_set(OF_OFF)
			else:
				attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT