from toee import *
from utilities import *
from scripts import *
from Co8 import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5095):
		if (game.global_vars[982] == 1 and game.global_vars[986] == 3 and game.global_flags[569] == 0):
		## turns on kallop outside cave
			attachee.object_flag_unset(OF_OFF)
	elif (attachee.map == 5115):
		if (game.global_vars[982] == 2 and game.global_flags[569] == 0):
		## turns on kallop inside cave
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_vars[982] = 3
	game.global_flags[569] = 1
	return RUN_DEFAULT


def san_will_kos( attachee, triggerer ):
	if (attachee.map == 5095) and (game.global_vars[986] == 3):
		attachee.attack(game.leader)
		game.new_sid = 0
		return RUN_DEFAULT
	else:
		return SKIP_DEFAULT
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.map == 5095):
		if (not game.combat_is_active()):
			if (attachee != OBJ_HANDLE_NULL and critter_is_unconscious(attachee) != 1 and not attachee.d20_query(Q_Prone) and attachee.leader_get() == OBJ_HANDLE_NULL):
				if (game.global_vars[986] != 3):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (talk_40(attachee, obj)):
							if (not npc_get(attachee,1)):
								attachee.turn_towards(game.party[0])
								game.party[0].begin_dialog( attachee, 1 )
								npc_set(attachee,1)
						elif (comment_20(attachee, obj)):
							if (not npc_get(attachee,3)):
								comment = game.random_range(1,400)
								if (comment == 20):
									attachee.float_line(10000,triggerer)
								if (comment == 60):
									attachee.float_line(10001,triggerer)
								if (comment == 100):
									attachee.float_line(10002,triggerer)
								if (comment == 140):
									attachee.float_line(10003,triggerer)
								if (comment == 180):
									attachee.float_line(10004,triggerer)
								if (comment == 220):
									attachee.float_line(10005,triggerer)
								if (comment == 260):
									attachee.float_line(10006,triggerer)
								if (comment == 300):
									attachee.float_line(10007,triggerer)
								if (comment == 340):
									attachee.float_line(10008,triggerer)
								if (comment == 380):
									attachee.float_line(10009,triggerer)
					if (game.global_vars[982] == 1 and not npc_get(attachee,2)):
						game.timevent_add( kallop_exit, ( attachee, triggerer ), 200 )
						npc_set(attachee,2)
		if (npc_get(attachee,3)):
			attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def talk_40(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 40):
			return 1
	return 0


def comment_20(speaker,listener):
	if (speaker.distance_to(listener) <= 20):
		return 1
	return 0


def switch_to_boonthag( attachee, triggerer, line ):
	npc = find_npc_near(attachee,8816)
	if (npc != OBJ_HANDLE_NULL):
		npc.turn_towards(game.party[0])
		triggerer.begin_dialog(npc, line)
	return SKIP_DEFAULT


def kallop_exit( attachee, triggerer ):
	attachee.npc_flag_unset(ONF_WAYPOINTS_DAY)
	attachee.npc_flag_unset(ONF_WAYPOINTS_NIGHT)
	attachee.standpoint_set( STANDPOINT_NIGHT, 424 )
	attachee.standpoint_set( STANDPOINT_DAY, 424 )
#	attachee.standpoint_set( STANDPOINT_SCOUT, 424 )
#	attachee.obj_set_int(obj_f_speed_walk, 1085353216)
	attachee.runoff( location_from_axis( 387, 466 ) )
	game.timevent_add( kallop_off, ( attachee, triggerer ), 8000 )
	return RUN_DEFAULT


def kallop_off( attachee, triggerer ):
	attachee.object_flag_set(OF_OFF)
	npc_set(attachee,3)
	return RUN_DEFAULT


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