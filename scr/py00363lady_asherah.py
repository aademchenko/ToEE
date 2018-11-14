from utilities import *
from toee import *
from Co8 import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.map == 5122):
		if (game.quests[102].state == qs_completed):
			if (game.global_flags[864] == 0 and game.global_flags[807] == 0 and game.global_flags[699] == 0):
				triggerer.begin_dialog( attachee, 920 )
			elif (game.global_flags[864] == 1 or game.global_flags[807] == 1):
				if (game.party_alignment == LAWFUL_NEUTRAL or game.party_alignment == LAWFUL_GOOD or game.party_alignment == NEUTRAL_GOOD):
					triggerer.begin_dialog( attachee, 1160 )
				elif (game.party_alignment == NEUTRAL_EVIL or game.party_alignment == CHAOTIC_EVIL or game.party_alignment == CHAOTIC_NEUTRAL):
					triggerer.begin_dialog( attachee, 1180 )
				elif (game.party_alignment == LAWFUL_EVIL or game.party_alignment == TRUE_NEUTRAL or game.party_alignment == CHAOTIC_GOOD):
					triggerer.begin_dialog( attachee, 1170 )
			elif (game.global_flags[699] == 1):
				if (game.party_alignment == LAWFUL_NEUTRAL or game.party_alignment == LAWFUL_GOOD or game.party_alignment == NEUTRAL_GOOD):
					triggerer.begin_dialog( attachee, 1230 )
				elif (game.party_alignment == NEUTRAL_EVIL or game.party_alignment == CHAOTIC_EVIL or game.party_alignment == CHAOTIC_NEUTRAL):
					triggerer.begin_dialog( attachee, 1250 )
				elif (game.party_alignment == LAWFUL_EVIL or game.party_alignment == TRUE_NEUTRAL or game.party_alignment == CHAOTIC_GOOD):
					triggerer.begin_dialog( attachee, 1240 )
		elif (game.global_vars[506] == 1):
			triggerer.begin_dialog( attachee, 270 )
		elif (game.party[0].reputation_has(56) == 1 or game.party[0].reputation_has(57) == 1):
			if (game.global_flags[865] == 0):
				triggerer.begin_dialog( attachee, 130 )
			elif (game.global_flags[865] == 1):
				if (game.party_alignment == LAWFUL_NEUTRAL or game.party_alignment == LAWFUL_GOOD or game.party_alignment == NEUTRAL_GOOD):
					triggerer.begin_dialog( attachee, 600 )
				elif (game.party_alignment == NEUTRAL_EVIL or game.party_alignment == CHAOTIC_EVIL or game.party_alignment == CHAOTIC_NEUTRAL):
					triggerer.begin_dialog( attachee, 710 )
				elif (game.party_alignment == LAWFUL_EVIL or game.party_alignment == TRUE_NEUTRAL or game.party_alignment == CHAOTIC_GOOD):
					triggerer.begin_dialog( attachee, 820 )
		else:
			return RUN_DEFAULT
	elif (attachee.map == 5145):
		if (game.global_vars[506] == 2):
			triggerer.begin_dialog( attachee, 1 )
		else:
			return RUN_DEFAULT
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.name == 8801):
		if (game.quests[102].state == qs_completed):
			if (attachee.map == 5122):
				attachee.object_flag_unset(OF_OFF)
			else:
				attachee.object_flag_set(OF_OFF)
		elif (attachee.map == 5122 and game.global_vars[506] == 1):
			attachee.object_flag_unset(OF_OFF)
		elif (attachee.map == 5145 and game.global_vars[506] == 2):
			if (game.global_vars[778] <= 2):
				game.global_vars[778] = game.global_vars[778] + 1
				if (game.global_vars[778] == 3):
					attachee.object_flag_unset(OF_OFF)
					game.global_vars[778] = 4
		elif (attachee.map == 5122 and (game.party[0].reputation_has(56) == 1 or game.party[0].reputation_has(57) == 1)):
			attachee.object_flag_unset(OF_OFF)
		elif (attachee.map == 5151 and (game.party[0].reputation_has(56) == 1 or game.party[0].reputation_has(57) == 1)):
			attachee.object_flag_unset(OF_OFF)
		else:
			attachee.object_flag_set(OF_OFF)
	elif (attachee.name == 8763):
		if (attachee.map == 5145 and game.global_vars[506] == 2 and game.global_vars[778] == 4):
			attachee.object_flag_unset(OF_OFF)
		elif (game.quests[102].state == qs_completed):
			if (game.global_vars[508] == 2 or game.global_vars[508] == 3):
				attachee.object_flag_set(OF_OFF)
		elif (game.quests[102].state == qs_accepted and (game.global_vars[734] == 2 or game.global_vars[697] == 2 or game.global_vars[698] == 2)):
			attachee.object_flag_set(OF_OFF)
	elif (attachee.name == 8764):
		if (game.quests[102].state == qs_completed):
			if (game.global_vars[508] == 2 or game.global_vars[508] == 3):
				attachee.object_flag_unset(OF_OFF)
				attachee.obj_set_int( obj_f_hp_damage, 200 )
		elif (game.quests[102].state == qs_accepted and (game.global_vars[734] == 2 or game.global_vars[697] == 2 or game.global_vars[698] == 2)):
				attachee.object_flag_unset(OF_OFF)
				attachee.obj_set_int( obj_f_hp_damage, 200 )
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[884] = 1
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	game.global_vars[333] = game.global_vars[333] + 1
	if (game.global_vars[333] >= 2):
		game.party[0].reputation_add( 34 )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.map == 5145):
		if (game.global_vars[506] == 2 and game.global_vars[778] == 4 and game.global_vars[534] != 2):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (is_better_to_talk(attachee, obj)):
						game.timevent_add( start_talking_1, ( attachee, triggerer ), 1000 )
						game.global_vars[534] = 2
	elif (attachee.map == 5122):
		if (game.quests[102].state == qs_completed):
			if (game.global_vars[508] == 1):
				if (not game.combat_is_active()):
					game.sound ( 4141, 1 )
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (is_better_to_talk(attachee, obj)):
							game.timevent_add( start_talking_7, ( attachee, triggerer ), 2000 )
							game.global_vars[508] = 4
			elif (game.global_vars[508] == 2):
				if (not game.combat_is_active()):
					attachee.condition_add_with_args("Prone",4,0)
					game.sound ( 4142, 1 )
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (is_better_to_talk(attachee, obj)):
							game.timevent_add( start_talking_8, ( attachee, triggerer ), 4000 )
							game.global_vars[508] = 5
			elif (game.global_vars[508] == 3):
				if (not game.combat_is_active()):
					attachee.condition_add_with_args("Prone",4,0)
					attachee.obj_set_int( obj_f_hp_damage, 9 )
					game.sound ( 4140, 1 )
					wreckage()
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (is_better_to_talk(attachee, obj)):
							game.timevent_add( start_talking_9, ( attachee, triggerer ), 4000 )
							game.global_vars[508] = 6
		elif (game.quests[102].state == qs_accepted and (game.global_vars[734] == 2 or game.global_vars[697] == 2 or game.global_vars[698] == 2)):
			if (not game.combat_is_active()):
				attachee.condition_add_with_args("Prone",4,0)
				attachee.obj_set_int( obj_f_hp_damage, 9 )
				game.sound ( 4140, 1 )
				wreckage()
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (is_better_to_talk(attachee, obj)):
						game.timevent_add( start_talking_10, ( attachee, triggerer ), 4000 )
						game.quests[102].state = qs_botched
		elif (game.global_vars[506] == 1 and game.global_vars[534] != 1):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (is_better_to_talk(attachee, obj)):
						game.timevent_add( start_talking_3, ( attachee, triggerer ), 1000 )
						game.global_vars[534] = 1
		elif (game.global_vars[506] == 4 and game.global_vars[534] != 4):
			if (game.global_flags[865] == 0):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (is_better_to_talk(attachee, obj)):
							game.timevent_add( start_talking_2, ( attachee, triggerer ), 1000 )
							game.global_vars[534] = 4
			elif (game.global_flags[865] == 1):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (is_better_to_talk(attachee, obj)):
							if (game.party_alignment == LAWFUL_NEUTRAL or game.party_alignment == LAWFUL_GOOD or game.party_alignment == NEUTRAL_GOOD):
								game.timevent_add( start_talking_4, ( attachee, triggerer ), 1000 )
								game.global_flags[694] = 4
							elif (game.party_alignment == NEUTRAL_EVIL or game.party_alignment == CHAOTIC_EVIL or game.party_alignment == CHAOTIC_NEUTRAL):
								game.timevent_add( start_talking_5, ( attachee, triggerer ), 1000 )
								game.global_flags[694] = 4
							elif (game.party_alignment == LAWFUL_EVIL or game.party_alignment == TRUE_NEUTRAL or game.party_alignment == CHAOTIC_GOOD):
								game.timevent_add( start_talking_6, ( attachee, triggerer ), 1000 )
								game.global_flags[694] = 4
	elif (attachee.map == 5151):
		if (game.global_vars[506] == 3 and game.global_vars[534] != 3):
			if (game.global_flags[865] == 0):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (is_better_to_talk(attachee, obj)):
							game.timevent_add( start_talking_2, ( attachee, triggerer ), 1000 )
							game.global_vars[534] = 3
			elif (game.global_flags[865] == 1):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (is_better_to_talk(attachee, obj)):
							if (game.party_alignment == LAWFUL_NEUTRAL or game.party_alignment == LAWFUL_GOOD or game.party_alignment == NEUTRAL_GOOD):
								game.timevent_add( start_talking_4, ( attachee, triggerer ), 1000 )
								game.global_vars[534] = 3
							elif (game.party_alignment == NEUTRAL_EVIL or game.party_alignment == CHAOTIC_EVIL or game.party_alignment == CHAOTIC_NEUTRAL):
								game.timevent_add( start_talking_5, ( attachee, triggerer ), 1000 )
								game.global_vars[534] = 3
							elif (game.party_alignment == LAWFUL_EVIL or game.party_alignment == TRUE_NEUTRAL or game.party_alignment == CHAOTIC_GOOD):
								game.timevent_add( start_talking_6, ( attachee, triggerer ), 1000 )
								game.global_vars[534] = 3
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[884] = 0
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 40):
			return 1
	return 0


def start_talking_1( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 1 )
	return RUN_DEFAULT


def start_talking_2( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 130 )
	return RUN_DEFAULT


def start_talking_3( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 270 )
	return RUN_DEFAULT


def start_talking_4( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 600 )
	return RUN_DEFAULT


def start_talking_5( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 710 )
	return RUN_DEFAULT


def start_talking_6( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 820 )
	return RUN_DEFAULT


def start_talking_7( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 920 )
	return RUN_DEFAULT


def start_talking_8( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 1080 )
	return RUN_DEFAULT


def start_talking_9( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 1120 )
	return RUN_DEFAULT


def start_talking_10( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 1270 )
	return RUN_DEFAULT


def schedule_transfer( attachee, triggerer ):
	game.timevent_add( play_dinner, ( attachee, triggerer ), 2000 )
	if (game.global_vars[699] == 0):
		game.timevent_add( play_bedsprings, ( attachee, triggerer ), 9000 )
		game.timevent_add( go_to_asherahs, ( attachee, triggerer ), 14000 )
	else:
		game.timevent_add( go_to_asherahs_2, ( attachee, triggerer ), 8000 )
	return RUN_DEFAULT


def schedule_transfer_2( attachee, triggerer ):
	game.timevent_add( play_dinner, ( attachee, triggerer ), 2000 )
	if (game.global_vars[699] == 0):
		game.timevent_add( play_bedsprings, ( attachee, triggerer ), 9000 )
		game.timevent_add( go_to_goose, ( attachee, triggerer ), 14000 )
	else:
		game.timevent_add( go_to_goose_2, ( attachee, triggerer ), 8000 )
	return RUN_DEFAULT


def play_dinner( attachee, triggerer ):
	game.sound( 4046, 1 )
	if (game.global_vars[699] == 3 or game.global_vars[699] == 4):
		game.party[0].reputation_add(57)
	return RUN_DEFAULT


def play_bedsprings( attachee, triggerer ):
	game.sound( 4047, 1 )
	game.party[0].reputation_add(56)
	return RUN_DEFAULT


def go_to_asherahs( attachee, triggerer ):
	game.fade_and_teleport( 0,0,0,5122,474,482 )
	return RUN_DEFAULT


def go_to_asherahs_2( attachee, triggerer ):
	game.fade_and_teleport( 0,0,0,5122,479,479 )
	return RUN_DEFAULT


def go_to_goose( attachee, triggerer ):
	game.fade_and_teleport( 0,0,0,5151,497,478 )
	return RUN_DEFAULT


def go_to_goose_2( attachee, triggerer ):
	game.fade_and_teleport( 0,0,0,5151,490,478 )
	return RUN_DEFAULT


def run_off_castle( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	guard = find_npc_near(attachee,8763)
	guard.runoff(attachee.location-3)
	return RUN_DEFAULT


def run_off_home( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT


def ruin_asherah( attachee, triggerer ):
	run_off_home( attachee, triggerer )
	return RUN_DEFAULT


def kill_asherah( attachee, triggerer ):
	attachee.critter_kill_by_effect()
	return RUN_DEFAULT


def wreckage():
	game.particles( "ef-Embers Small", location_from_axis( 473, 484 ) )
	game.particles( "effect-chimney smoke", location_from_axis( 473, 484 ) )
	game.particles( "ef-ogrefire", location_from_axis( 478, 470 ) )
	game.particles( "ef-fire-lazy", location_from_axis( 476, 464 ) )
	game.particles( "ef-ogrefire", location_from_axis( 485, 480 ) )
	game.particles( "ef-ogrefire", location_from_axis( 481, 463 ) )
	game.particles( "effect-chimney smoke", location_from_axis( 475, 476 ) )
	game.particles( "effect-chimney smoke", location_from_axis( 474, 467 ) )
	return