from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.area != 3):
		if (game.quests[60].state == qs_completed):
			triggerer.begin_dialog( attachee, 210 )
		elif (game.global_flags[86] == 1):
			triggerer.begin_dialog( attachee, 200 )
		elif (attachee.map == 5037):
			triggerer.begin_dialog( attachee, 1 )
		elif (attachee.map == 5007):
			triggerer.begin_dialog( attachee, 320 )
	elif (attachee.area == 3):
		if (game.global_flags[871] == 1):
			triggerer.begin_dialog( attachee, 400 )
		else:
			triggerer.begin_dialog( attachee, 60 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if ((game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2) and (attachee.area == 1)):
		attachee.object_flag_set(OF_OFF)
	elif (game.global_flags[859] == 1):
	# nulb business is over
		if (attachee.map == 5060):
		# waterside hostel
			attachee.object_flag_set(OF_OFF)
		elif (attachee.map == 5037):
		# brewhouse
			if (is_daytime() == 1):
				attachee.object_flag_unset(OF_OFF)
			if (is_daytime() == 0):
				attachee.object_flag_set(OF_OFF)
		elif (attachee.map == 5007):
		# welcome wench
			if (is_daytime() == 1):
				attachee.object_flag_set(OF_OFF)
			elif (is_daytime() == 0):
				attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[86] = 1
	game.global_flags[860] = 1
	if (game.party[0].reputation_has(9) == 0):
		game.party[0].reputation_add(9)
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (attachee.map == 5037):
		for obj in game.obj_list_vicinity(attachee.location,OLC_NPC):
			if (obj.leader_get() != OBJ_HANDLE_NULL):
				obj.turn_towards(triggerer)
				obj.attack(triggerer)
		game.new_sid = 0
	return RUN_DEFAULT


def san_exit_combat( attachee, triggerer ):
	if (attachee.stat_level_get(stat_subdual_damage) >= attachee.stat_level_get(stat_hp_current) and attachee.stat_level_get(stat_hp_current) >=1 and not game.combat_is_active()):
		for pc in game.party:
			if pc.type == obj_t_pc:
				attachee.ai_shitlist_remove( pc )
		game.global_flags[871] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[860] = 0
	if (game.global_flags[859] == 0 and attachee.map == 5060):
		game.global_flags[86] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_flags[871] == 1 and attachee.map == 5060 and critter_is_unconscious(attachee) != 1 and not attachee.d20_query(Q_Prone) and (attachee.stat_level_get(stat_hp_current) - attachee.stat_level_get(stat_subdual_damage)) != 0):
		game.global_flags[859] = 1
#		game.global_flags[86] = 1
#		attachee.object_flag_set(OF_OFF)
#		attachee.runoff(attachee.location-3)
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_safe_to_talk(attachee,obj)):
				obj.begin_dialog( attachee, 600 )
				return RUN_DEFAULT
		attachee.object_flag_set(OF_OFF)
		return RUN_DEFAULT
	if (game.global_flags[871] == 1 and attachee.map != 5060 and game.global_flags[859] == 0):
		game.global_flags[859] = 1
	if (game.global_flags[871] == 1 and attachee.item_find(6016) == OBJ_HANDLE_NULL and attachee.item_find(6149) == OBJ_HANDLE_NULL and attachee.map == 5037):
		create_item_in_inventory( 6149, attachee )
		attachee.item_wield_best_all()
	if ((game.global_flags[871] == 1 or game.global_flags[858] == 1) and attachee.item_find(5815) != OBJ_HANDLE_NULL and attachee.map == 5007):
		itemB = attachee.item_find(5815)
		itemB.destroy()
	if (attachee.item_find(5815) == OBJ_HANDLE_NULL and game.global_flags[858] == 0):
		game.global_flags[858] = 1
	if (game.global_flags[871] == 1 and attachee.item_find(6149) == OBJ_HANDLE_NULL and attachee.map == 5007):
		itemB = attachee.item_find(6016)
		if (itemB != OBJ_HANDLE_NULL):
			itemB.destroy()
		itemC = attachee.item_find(4074)
		if (itemC != OBJ_HANDLE_NULL):
			itemC.destroy()
		create_item_in_inventory( 6149, attachee )
		attachee.item_wield_best_all()
	if (game.global_flags[860] == 1 ):
		attachee.object_flag_set(OF_OFF)
		return RUN_DEFAULT
	return RUN_DEFAULT


def san_will_kos( attachee, triggerer ):
	if (game.global_flags[871] == 1):
		return SKIP_DEFAULT
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
#	attachee.standpoint_set( STANDPOINT_NIGHT, 255 )
#	attachee.standpoint_set( STANDPOINT_NIGHT, 38 )
#	game.global_flags[86] = 1
	game.global_flags[859] = 1
	attachee.object_flag_set(OF_OFF)
#	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT