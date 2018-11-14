from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.map == 5170):
		triggerer.begin_dialog( attachee, 80 )
	elif (is_daytime() == 1):
		triggerer.begin_dialog( attachee, 10 )
	else:
		triggerer.begin_dialog( attachee, 20 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5156 and game.global_vars[704] == 3 and is_daytime() == 1 and game.quests[76].state != qs_accepted):
	##turns on warehouse Wilfrick escort
		attachee.object_flag_unset(OF_OFF)
	elif (attachee.map == 5093 and game.global_vars[960] == 3):
	##turns on Welkwood Thaddeus escort
		attachee.object_flag_unset(OF_OFF)
	elif (attachee.map == 5171 and game.global_vars[944] == 4 and game.global_flags[861] == 1):
	##turns on Watch Post main floor replacements
		attachee.object_flag_unset(OF_OFF)
	elif ( (game.party[0].reputation_has(35) == 1 or game.party[0].reputation_has(42) == 1) and (attachee.map == 5121) ):
	##turns on Verbobonc Exterior backup patrol
		attachee.object_flag_unset(OF_OFF)
	elif ( (game.party[0].reputation_has(35) == 0) and (attachee.map == 5121) ):
	##turns off Verbobonc Exterior backup patrol
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	if (attachee.map == 5093):
		ditch_rings( attachee, triggerer )
		if (game.global_vars[956] == 0):
			game.global_vars[957] = game.global_vars[957] + 1
	elif (attachee.map == 5121 or attachee.map == 5135 or attachee.map == 5169 or attachee.map == 5170 or attachee.map == 5171 or attachee.map == 5172):
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
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	leader = game.leader
	if ( (attachee.map == 5093) and (game.global_vars[956] == 1) ):
		attachee.obj_set_int(obj_f_critter_strategy, 21)
		return RUN_DEFAULT
	elif (attachee.map != 5093 and game.global_vars[969] == 1):
		game.global_vars[969] = 0
	elif ( (game.quests[67].state == qs_accepted) and (game.global_flags[963] == 0) ):
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
	# get arrested for various reps
	if ( (attachee.map != 5156) and (game.party[0].reputation_has(34) == 1 or game.party[0].reputation_has(35) == 1 or game.party[0].reputation_has(42) == 1 or game.party[0].reputation_has(44) == 1 or game.party[0].reputation_has(45) == 1 or game.party[0].reputation_has(43) == 1 or game.party[0].reputation_has(46) == 1 or (game.global_vars[993] == 5 and game.global_flags[870] == 0)) ):
		if ( (game.global_vars[969] == 0) and (game.global_flags[955] == 0) ):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (is_better_to_talk(attachee,obj)):
						game.timevent_add( get_arrested, ( attachee, triggerer ), 2000 )
	# viscount guard talks about arrow to the knee
	elif (attachee.name == 8800):
		if (game.global_vars[829] == 0):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (is_peachy_to_talk(attachee,obj)):
						game.timevent_add( talk_arrow_knee, ( attachee, triggerer ), 2000 )
						game.global_vars[829] = 1
	return RUN_DEFAULT


def san_will_kos( attachee, triggerer ):
	if (game.party[0].reputation_has(34) == 1) or (game.party[0].reputation_has(35) == 1):
		return RUN_DEFAULT
	elif (game.global_flags[992] == 0) or (game.global_flags[975] == 0):
		return SKIP_DEFAULT
	return RUN_DEFAULT


def guard_backup( attachee, triggerer ):
	guard_1 = game.obj_create(14716, attachee.location-4)
	guard_1.turn_towards(game.party[0])
	guard_2 = game.obj_create(14716, attachee.location-4)
	guard_2.turn_towards(game.party[0])
	guard_3 = game.obj_create(14716, attachee.location-4)
	guard_3.turn_towards(game.party[0])
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 50):
			return 1
	return 0


def is_peachy_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 20):
			return 1
	return 0


def is_distant_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 100):
			return 1
	return 0


def execution( attachee, triggerer ):
	cleric = find_npc_near(attachee,14471)
	game.particles( "cast-Evocation-cast", cleric )
	game.sound( 4049, 1 )
	pc1 = game.party[0]
	pc1.critter_kill_by_effect()
	game.particles( "sp-Flame Strike", pc1 )
	pc2 = game.party[1]
	pc2.critter_kill_by_effect()
	game.particles( "sp-Flame Strike", pc2 )
	pc3 = game.party[2]
	pc3.critter_kill_by_effect()
	game.particles( "sp-Flame Strike", pc3 )
	pc4 = game.party[3]
	pc4.critter_kill_by_effect()
	game.particles( "sp-Flame Strike", pc4 )
	pc5 = game.party[4]
	pc5.critter_kill_by_effect()
	game.particles( "sp-Flame Strike", pc5 )
	pc6 = game.party[5]
	pc6.critter_kill_by_effect()
	game.particles( "sp-Flame Strike", pc6 )
	pc7 = game.party[6]
	pc7.critter_kill_by_effect()
	game.particles( "sp-Flame Strike", pc7 )
	pc8 = game.party[7]
	pc8.critter_kill_by_effect()
	game.particles( "sp-Flame Strike", pc8 )
	return 1


def go_away( attachee ):
	attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def ditch_rings( attachee, triggerer ):
	acid_minor = attachee.item_find(12630)
	cold_minor = attachee.item_find(12629)
	electricity_minor = attachee.item_find(12627)
	fire_minor = attachee.item_find(6101)
	sonic_minor = attachee.item_find(12628)
	acid_minor.destroy()
	cold_minor.destroy()
	electricity_minor.destroy()
	fire_minor.destroy()
	sonic_minor.destroy()
	return


def get_arrested( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 30 )
	return RUN_DEFAULT


def talk_arrow_knee( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 140 )
	return RUN_DEFAULT


def new_entry_guard( attachee, triggerer ):
	entry_guard = game.obj_create(14817, location_from_axis(236, 490))
	entry_guard.rotation = 3.0
	return RUN_DEFAULT