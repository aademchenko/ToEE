from utilities import *
from toee import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	#used by door in Moathouse Interior to Moathouse Back Door to tell which Ambush to turn on
	game.global_vars[710] = 3
	return RUN_DEFAULT


def san_heartbeat(attachee, triggerer):
	if (game.global_vars[765] == 1 or game.global_vars[765] == 2 or game.global_flags[283] == 1):
		attachee.object_flag_set(OF_OFF)
		return SKIP_DEFAULT
	elif ((attachee.map == 5002) and (game.global_vars[765] == 0) and (game.party_alignment != LAWFUL_EVIL) and (game.global_flags[977] == 1) and (game.global_vars[710] == 3)) and (game.global_vars[450] & 2**0 == 0) and (game.global_vars[450] & 2**11 == 0):
		if not anyone( game.leader.group_list(), "has_follower", 8002 ) and not anyone( game.leader.group_list(), "has_follower", 8004 ) and not anyone( game.leader.group_list(), "has_follower", 8005 ) and not anyone( game.leader.group_list(), "has_follower", 8010 ):
			if ((game.global_flags[44] != 1) and (game.global_flags[45] != 1) and (game.global_flags[700] != 1) and (game.global_flags[37] == 1) and (game.global_flags[283] == 0)):
				attachee.object_flag_unset(OF_OFF)
	attachee.scripts[15] = 2 # san_start_combat
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_vars[765] = 3
	return RUN_DEFAULT