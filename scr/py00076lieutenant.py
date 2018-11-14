from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	ggv400 = game.global_vars[400]

	if attachee.leader_get() != OBJ_HANDLE_NULL:
		return RUN_DEfAULT
	elif anyone( triggerer.group_list(), "has_follower", 8002 ):
		attachee.float_line(16002, triggerer)
	elif ( ggv400 & (2**0) ) != 0 :
		attachee.float_line(15500, triggerer)
	elif (not attachee.has_met( triggerer )):
		triggerer.begin_dialog( attachee, 1 )
	elif (game.global_flags[48] == 1 and game.global_flags[49] == 0):
		triggerer.begin_dialog( attachee, 70 )
	else:
		triggerer.begin_dialog( attachee, 100 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	ggv400 = game.global_vars[400]
	ggv403 = game.global_vars[403]
	if (  not game.combat_is_active() and ( ggv403 & (2**1) ) == 0   ) and ( ggv400 & (2**5) ) == 0:
		if (is_better_to_talk(attachee,game.party[0])): 
			if (not critter_is_unconscious(game.party[0])):
				if (not attachee.has_met(game.party[0])):
					if (is_better_to_talk(attachee,game.party[0])):
						attachee.turn_towards(game.party[0])
						game.party[0].begin_dialog( attachee, 1 )
						game.new_sid = 0
		else:
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_safe_to_talk(attachee,obj)):
					if (not attachee.has_met(obj)):
						attachee.turn_towards(obj)
						obj.begin_dialog( attachee, 1 )
						game.new_sid = 0
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 20):
			return 1
	return 0


def call_leader(npc, pc): 
	leader = game.party[0]
	leader.move(pc.location - 2)
	leader.begin_dialog(npc, 1)
	return 