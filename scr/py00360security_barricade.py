from toee import *
from utilities import *
from scripts import *
from Co8 import *
from combat_standard_routines import *


def san_use( door, triggerer ):
	if (door.name == 1621):
		if (game.global_flags[966] == 0):
		## if security barricade is active, disable outside door portal
			return SKIP_DEFAULT
		else:
		## do normal transition
			return RUN_DEFAULT
	elif (door.name == 1623):
		if (game.global_flags[966] == 0):
		## if security barricade is active, disable inside door portal
			return SKIP_DEFAULT
		else:
		## do regional patrol dues flag routine and normal transition
			if (game.global_flags[260] == 0):
				game.global_flags[260] = 1
			return RUN_DEFAULT


def san_dialog( attachee, triggerer ):
	if (attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 10 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[966] == 1):
		attachee.object_flag_set(OF_OFF)
	elif (game.global_flags[966] == 0):
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	leader = game.party[0]
	StopCombat(attachee, 0)
	leader.begin_dialog( attachee, 4000 )
	return RUN_DEFAULT