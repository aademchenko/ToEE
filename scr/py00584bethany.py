from toee import *
from utilities import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.map == 5070 or attachee.map == 5071 or attachee.map == 5072 or attachee.map == 5073 or attachee.map == 5074 or attachee.map == 5075 or attachee.map == 5076 or attachee.map == 5077):
		if (triggerer.stat_level_get(stat_race) == race_halforc):
			triggerer.begin_dialog( attachee, 6 )
		else:
			triggerer.begin_dialog( attachee, 1 )
	elif (attachee.map == 5171):
		if (game.global_flags[560] == 1 and game.global_flags[561] == 1 and game.global_flags[562] == 1):
			if (game.global_flags[549] == 0):
				triggerer.begin_dialog( attachee, 240 )
			else:
				if (game.global_flags[962] == 0):
					triggerer.begin_dialog( attachee, 510 )
				else:
					triggerer.begin_dialog( attachee, 520 )
		else:
			if (game.global_flags[563] == 1):
				triggerer.begin_dialog( attachee, 540 )
			else:
				if (not npc_get(attachee,1)):
					triggerer.begin_dialog( attachee, 530 )
					npc_set(attachee,1)
				else:
					if (game.global_flags[962] == 0):
						triggerer.begin_dialog( attachee, 550 )
					else:
						triggerer.begin_dialog( attachee, 560 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5171):
		if (game.global_flags[826] == 0 and game.quests[62].state == qs_accepted):
			attachee.object_flag_unset( OF_OFF )
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		if should_modify_CR( attachee ):
			modify_CR( attachee, get_av_level() )
	game.global_flags[826] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[826] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.map == 5071):
		if (not npc_get(attachee,3)):
			attachee.obj_set_int( obj_f_hp_damage, 50 )
			game.timevent_add( talk_talk, ( attachee, triggerer ), 2000 )
			npc_set(attachee,3)
		if (npc_get(attachee,2) and not npc_get(attachee,4)):
			game.timevent_add( beth_exit, ( attachee, triggerer ), 200 )
			npc_set(attachee,4)
	return RUN_DEFAULT


def face_holly( attachee, triggerer ):
	holly = find_npc_near(attachee,8714)
	attachee.turn_towards(holly)
	holly.turn_towards(attachee)
	return RUN_DEFAULT


def heal_beth( attachee, triggerer ):
	dice = dice_new("1d10+1000")
	attachee.heal( OBJ_HANDLE_NULL, dice )
	attachee.healsubdual( OBJ_HANDLE_NULL, dice )
	game.sound( 4182, 1 )
	game.particles( "sp-Heal", attachee )
	return RUN_DEFAULT


def is_25_and_under(speaker,listener):
	if (speaker.distance_to(listener) <= 25):
		return 1
	return 0


def run_off( attachee, triggerer ):
	attachee.runoff( attachee.location-3 )
	return RUN_DEFAULT


def talk_talk( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 1 )
	npc_set(attachee,2)
	return


def beth_exit( attachee, triggerer ):
	attachee.npc_flag_unset(ONF_WAYPOINTS_DAY)
	attachee.npc_flag_unset(ONF_WAYPOINTS_NIGHT)
	attachee.runoff( location_from_axis( 480, 480 ) )
	return RUN_DEFAULT