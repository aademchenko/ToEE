from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	triggerer.turn_towards(attachee)
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[561] = 1
	if (game.global_flags[560] == 1 and game.global_flags[562] == 1):
		game.party[0].reputation_add( 62 )
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	return SKIP_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		if (not game.combat_is_active()):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_30_and_under(attachee, obj)):
					attachee.turn_towards(obj)
					obj.begin_dialog( attachee, 1 )
					game.new_sid = 0
	return RUN_DEFAULT


def is_30_and_under(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 30):
			return 1
	return 0


def increment_rep( attachee, triggerer ):
	if (game.party[0].reputation_has(81) == 1):
		game.party[0].reputation_add(82)
		game.party[0].reputation_remove(81)
	elif (game.party[0].reputation_has(82) == 1):
		game.party[0].reputation_add(83)
		game.party[0].reputation_remove(82)
	elif (game.party[0].reputation_has(83) == 1):
		game.party[0].reputation_add(84)
		game.party[0].reputation_remove(83)
	elif (game.party[0].reputation_has(84) == 1):
		game.party[0].reputation_add(85)
		game.party[0].reputation_remove(84)
	elif (game.party[0].reputation_has(85) == 1):
		game.party[0].reputation_add(86)
		game.party[0].reputation_remove(85)
	elif (game.party[0].reputation_has(86) == 1):
		game.party[0].reputation_add(87)
		game.party[0].reputation_remove(86)
	elif (game.party[0].reputation_has(87) == 1):
		game.party[0].reputation_add(88)
		game.party[0].reputation_remove(87)
	elif (game.party[0].reputation_has(88) == 1):
		game.party[0].reputation_add(89)
		game.party[0].reputation_remove(88)
	else:
		game.party[0].reputation_add(81)
	return RUN_DEFAULT