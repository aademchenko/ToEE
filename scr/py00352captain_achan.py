from toee import *
from scripts import *
from utilities import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (game.global_vars[962] == 1):
		triggerer.begin_dialog( attachee, 250 )
	elif (attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 20 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5170 or attachee.map == 5135):
		if (game.global_vars[946] == 1):
			attachee.object_flag_unset(OF_OFF)
		elif (game.global_vars[946] == 2):
			attachee.object_flag_set(OF_OFF)
	elif (attachee.map == 5172):
		if (game.global_vars[946] == 2) and tpsts('achan_off_to_arrest', 1*60*60) == 0:
			attachee.object_flag_set(OF_OFF)
		elif (game.global_vars[946] == 3) or tpsts('achan_off_to_arrest', 1*60*60):
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if ((attachee.map == 5170 or attachee.map == 5135) and game.global_vars[946] == 1):
		if (not game.combat_is_active()):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_groovier_to_talk(attachee, obj)):
					game.timevent_add( start_talking, ( attachee, triggerer ), 2000 )
					game.new_sid = 0
	else:
		if ( (game.party[0].reputation_has(34) == 1 or game.party[0].reputation_has(35) == 1 or game.party[0].reputation_has(42) == 1 or game.party[0].reputation_has(44) == 1 or game.party[0].reputation_has(35) == 1 or game.party[0].reputation_has(43) == 1 or game.party[0].reputation_has(46) == 1 or (game.global_vars[993] == 5 and game.global_flags[870] == 0)) ):
			if ( (game.global_vars[969] == 0) and (game.global_flags[955] == 0) ):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (is_better_to_talk(attachee,obj)):
							attachee.turn_towards(obj)
							obj.begin_dialog( attachee, 230 )
							game.global_vars[969] = 1
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 50):
		return 1
	return 0


def is_groovier_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 40):
			return 1
	return 0


def start_talking( attachee, triggerer ):
	npc = find_npc_near(attachee,8703)
	attachee.turn_towards(npc)
	game.party[0].begin_dialog( attachee, 460 )
	return RUN_DEFAULT


def switch_to_wilfrick( attachee, triggerer, line):
	npc = find_npc_near(attachee,8703)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
		npc.turn_towards(triggerer)
	return SKIP_DEFAULT


def run_off( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT