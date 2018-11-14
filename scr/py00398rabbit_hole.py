from toee import *
from utilities import *
from Co8 import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	if (game.global_vars[937] == 0 and game.quests[89].state >= qs_accepted):
		game.global_vars[937] = 1
	return RUN_DEFAULT


def san_dialog( attachee, triggerer ):
	if (game.global_vars[937] >= 4):
		triggerer.begin_dialog( attachee, 1 )
	elif (game.global_vars[937] == 3):
		triggerer.begin_dialog( attachee, 10 )
	else:
		return SKIP_DEFAULT
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[937] == 1):
		attachee.object_flag_unset(OF_OFF)
		game.global_vars[937] = 2
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	leader = game.party[0]
	StopCombat(attachee, 0)
	leader.begin_dialog( attachee, 4000 )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.map == 5143 and game.global_vars[937] == 2):
		if (not game.combat_is_active()):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (close_enough(attachee, obj)):
					if (obj.skill_level_get(attachee,skill_spot) >= 15):
						obj.begin_dialog( attachee, 20 )
						game.global_vars[937] = 3
						attachee.object_flag_unset(OF_DONTDRAW)
	return RUN_DEFAULT


def close_enough(speaker,listener):
	if (speaker.distance_to(listener) <= 5):
		return 1
	return 0