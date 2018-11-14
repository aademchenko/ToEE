from utilities import *
from toee import *
from combat_standard_routines import *


def san_heartbeat(attachee, triggerer):
	if (game.global_vars[765] == 1 or game.global_vars[765] == 3 or game.global_flags[283] == 1):
		attachee.object_flag_set(OF_OFF)
		return SKIP_DEFAULT
	elif ((attachee.map == 5002) and (game.global_vars[765] == 0) and (game.party_alignment != LAWFUL_EVIL) and (game.global_flags[977] == 1) and (game.global_vars[710] == 2))  and (game.global_vars[450] & 2**0 == 0) and (game.global_vars[450] & 2**11 == 0):
		if not anyone( game.leader.group_list(), "has_follower", 8002 ) and not anyone( game.leader.group_list(), "has_follower", 8004 ) and not anyone( game.leader.group_list(), "has_follower", 8005 ) and not anyone( game.leader.group_list(), "has_follower", 8010 ):
			if ((game.global_flags[44] != 1) and (game.global_flags[45] != 1) and (game.global_flags[700] != 1) and (game.global_flags[37] == 1) and (game.global_flags[283] == 0)):
				attachee.object_flag_unset(OF_OFF)
				if (not game.combat_is_active()):
					if (is_better_to_talk(attachee, game.party[0])):
						game.timevent_add( start_talking, ( attachee, triggerer ), 2000 )
						game.new_sid = 0
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 50):
		return 1
	return 0


def start_talking( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 600 )
	return RUN_DEFAULT