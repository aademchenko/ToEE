from toee import *
from scripts import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.has_met(triggerer)):
		triggerer.begin_dialog(attachee,20)
	else:
		triggerer.begin_dialog(attachee,1)
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5170 or attachee.map == 5135):
		if (game.global_vars[947] == 1):
			attachee.object_flag_unset(OF_OFF)
		elif (game.global_vars[947] == 2):
			attachee.object_flag_set(OF_OFF)
	elif (attachee.map == 5171):
		if (game.global_vars[947] == 2) and  tpsts('absalom_off_to_arrest', 1*60*60) == 0:
			attachee.object_flag_set(OF_OFF)
		elif (game.global_vars[947] == 3) or tpsts('absalom_off_to_arrest', 1*60*60):
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	if attachee.map == 5121 or attachee.map == 5135 or attachee.map == 5169 or attachee.map == 5170 or attachee.map == 5171 or attachee.map == 5172:
		game.global_vars[334] = game.global_vars[334] + 1	
		if (game.global_vars[334] >= 2):
			game.party[0].reputation_add( 35 )
		if (game.quests[67].state == qs_accepted):
			game.global_flags[964] = 1
		if (game.global_flags[942] == 1):
			game.party[0].reputation_add( 35 )
		if (attachee.name == 8770):
			game.timevent_add( new_entry_guard, ( attachee, triggerer ), 86400000 )
		game.timevent_add( go_away, ( attachee, ), 60000 )
	game.global_flags[419] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[419] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if ((attachee.map == 5170 or attachee.map == 5135) and game.global_vars[947] == 1):
		if (not game.combat_is_active()):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_groovier_to_talk(attachee, obj)):
					game.timevent_add( start_talking, ( attachee, triggerer ), 2000 )
					game.global_vars[947] = 2
	elif ( (game.party[0].reputation_has(34) == 1 or game.party[0].reputation_has(35) == 1 or game.party[0].reputation_has(42) == 1 or game.party[0].reputation_has(44) == 1 or game.party[0].reputation_has(35) == 1 or game.party[0].reputation_has(43) == 1 or game.party[0].reputation_has(46) == 1) ):
		if ( (game.global_vars[969] == 0) and (game.global_flags[955] == 0) ):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (is_better_to_talk(attachee,obj)):
						attachee.turn_towards(obj)
						obj.begin_dialog( attachee, 180 )
						game.global_vars[969] = 1
	elif (game.global_vars[993] == 5 and game.global_flags[870] == 1):
		if (not game.combat_is_active()):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_safe_to_talk(attachee,obj)):
					obj.begin_dialog( attachee, 200 )
					game.global_vars[993] = 7
	elif (game.global_vars[993] == 5 and game.global_flags[870] == 0):
		if (not game.combat_is_active()):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_safe_to_talk(attachee,obj)):
					obj.begin_dialog( attachee, 210 )
					game.global_vars[993] = 8
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 35):
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
	game.party[0].begin_dialog( attachee, 320 )
	return RUN_DEFAULT


def switch_to_wilfrick( attachee, triggerer, line):
	npc = find_npc_near(attachee,8703)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
		npc.turn_towards(triggerer)
	return SKIP_DEFAULT


def run_off( attachee, triggerer ):
	attachee.runoff(attachee.location-1)
	return RUN_DEFAULT