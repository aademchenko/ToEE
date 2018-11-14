from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (is_daytime() == 1):
		triggerer.begin_dialog( attachee, 10 )
	else:
		triggerer.begin_dialog( attachee, 20 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if ( (game.party[0].reputation_has(35) == 1 or game.party[0].reputation_has(42) == 1) and (attachee.map == 5121) ):	##turns on Verbobonc Exterior backup patrol
		attachee.object_flag_unset(OF_OFF)
	elif ( (game.party[0].reputation_has(35) == 0) and (attachee.map == 5121) ):	##turns off Verbobonc Exterior backup patrol
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	game.global_vars[334] = game.global_vars[334] + 1
	if (game.global_vars[334] >= 2):
		game.party[0].reputation_add( 35 )
	if (game.quests[67].state == qs_accepted):
		game.global_flags[964] = 1
	game.timevent_add( go_away, ( attachee, ), 60000 )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	leader = game.leader
	if ( (game.quests[67].state == qs_accepted) and (game.global_flags[963] == 0) ):
		game.counters[0] = game.counters[0] + 1
		if (game.counters[0] >= 2):
			for pc in game.party:
				if pc.type == obj_t_pc:
					attachee.ai_shitlist_remove( pc )
			game.global_flags[963] = 1
			leader.begin_dialog( attachee, 1 )
			return SKIP_DEFAULT
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if ( (game.party[0].reputation_has(34) == 1 or game.party[0].reputation_has(35) == 1 or game.party[0].reputation_has(42) == 1 or game.party[0].reputation_has(44) == 1 or game.party[0].reputation_has(35) == 1 or game.party[0].reputation_has(43) == 1 or game.party[0].reputation_has(46) == 1 or (game.global_vars[993] == 5 and game.global_flags[870] == 0)) ):
		if ( (game.global_vars[969] == 0) and (game.global_flags[955] == 0) ):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (is_better_to_talk(attachee,obj)):
						attachee.turn_towards(obj)
						obj.begin_dialog( attachee, 30 )
						game.global_vars[969] = 1
	return RUN_DEFAULT


def san_will_kos( attachee, triggerer ):
	if (game.party[0].reputation_has(34) == 1) or (game.party[0].reputation_has(35) == 1):
		return RUN_DEFAULT
	elif (game.global_flags[992] == 0) or (game.global_flags[975] == 0):
		return SKIP_DEFAULT
	return RUN_DEFAULT


def guard_backup( attachee, triggerer ):
	guard_1 = game.obj_create(14700, attachee.location-4)
	guard_1.turn_towards(game.party[0])
	guard_2 = game.obj_create(14700, attachee.location-4)
	guard_2.turn_towards(game.party[0])
	guard_3 = game.obj_create(14700, attachee.location-4)
	guard_3.turn_towards(game.party[0])
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 35):
			return 1
	return 0


def is_close(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 15):
			return 1
	return 0


def go_away( attachee ):
	attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT