from toee import *
from utilities import *
from Co8 import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_use( door, triggerer ):
	if (door.name == 1622):
		if (game.global_flags[532] == 0):
			game.global_flags[534] = 1
			return SKIP_DEFAULT
			## if doors to tunnels are locked, disable door portal, flag for attempt and fine
		elif (game.global_flags[532] == 1):
			if (game.global_vars[548] <= 2):
				game.global_vars[548] = game.global_vars[548] + 1
				if (game.global_vars[548] == 3):
					game.party[0].reputation_add( 68 )
					game.global_vars[548] = 4
			return RUN_DEFAULT


def san_dialog( attachee, triggerer ):
	if (game.global_vars[551] == 2):
		triggerer.begin_dialog( attachee, 270 )
	elif (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 240 )
	elif (attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 40 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5169 and game.global_vars[551] == 2):
		if (attachee.leader_get() == OBJ_HANDLE_NULL):
			attachee.object_flag_set(OF_OFF)
	elif (attachee.map == 5141):
		if (game.quests[109].state == qs_completed and game.global_vars[551] == 2):
			attachee.object_flag_set(OF_OFF)	
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[809] = 1
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	if (game.global_vars[538] != 4):
		game.global_vars[538] = game.global_vars[538] + 1
	if (game.global_vars[538] == 3):
		leader = game.party[0]
		StopCombat(attachee, 0)
		leader.begin_dialog( attachee, 100 )
		game.global_vars[538] = 4
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[809] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.quests[109].state == qs_mentioned or game.quests[109].state == qs_accepted):
		if (game.global_vars[536] == 2):
			if (attachee.name == 8791):
				if (game.global_vars[539] == 1):
					if (game.global_vars[542] == 1):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11058,attachee)
					elif (game.global_vars[542] == 2):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11009,attachee)
						create_item_in_inventory(11062,attachee)
					elif (game.global_vars[542] == 3):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11099,attachee)
			elif (attachee.name == 8792):
				if (game.global_vars[539] == 2):
					if (game.global_vars[542] == 1):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11058,attachee)
					elif (game.global_vars[542] == 2):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11009,attachee)
						create_item_in_inventory(11062,attachee)
					elif (game.global_vars[542] == 3):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11099,attachee)
			elif (attachee.name == 8793):
				if (game.global_vars[539] == 3):
					if (game.global_vars[542] == 1):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11058,attachee)
					elif (game.global_vars[542] == 2):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11009,attachee)
						create_item_in_inventory(11062,attachee)
					elif (game.global_vars[542] == 3):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11099,attachee)
			elif (attachee.name == 8794):
				if (game.global_vars[539] == 4):
					if (game.global_vars[542] == 1):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11058,attachee)
					elif (game.global_vars[542] == 2):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11009,attachee)
						create_item_in_inventory(11062,attachee)
					elif (game.global_vars[542] == 3):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11099,attachee)
			elif (attachee.name == 8795):
				if (game.global_vars[539] == 5):
					if (game.global_vars[542] == 1):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11058,attachee)
					elif (game.global_vars[542] == 2):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11009,attachee)
						create_item_in_inventory(11062,attachee)
					elif (game.global_vars[542] == 3):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11099,attachee)
			elif (attachee.name == 8796):
				if (game.global_vars[539] == 6):
					if (game.global_vars[542] == 1):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11058,attachee)
					elif (game.global_vars[542] == 2):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11009,attachee)
						create_item_in_inventory(11062,attachee)
					elif (game.global_vars[542] == 3):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11099,attachee)
			elif (attachee.name == 8797):
				if (game.global_vars[539] == 7):
					if (game.global_vars[542] == 1):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11058,attachee)
					elif (game.global_vars[542] == 2):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11009,attachee)
						create_item_in_inventory(11062,attachee)
					elif (game.global_vars[542] == 3):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11099,attachee)
			elif (attachee.name == 8798):
				if (game.global_vars[539] == 8):
					if (game.global_vars[542] == 1):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11058,attachee)
					elif (game.global_vars[542] == 2):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11009,attachee)
						create_item_in_inventory(11062,attachee)
					elif (game.global_vars[542] == 3):
						attachee.object_flag_unset(OF_OFF)
#						game.global_vars[539] = 9
						game.global_vars[536] = 3
						create_item_in_inventory(11059,attachee)
						create_item_in_inventory(11099,attachee)
		elif (game.global_vars[536] == 3):
			if (game.global_vars[539] == 1):
				if (attachee.name == 8791):
					if (not game.combat_is_active()):
						for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
							if (close_enough(attachee, obj)):
								if (obj.skill_level_get(attachee,skill_spot) >= 19):
									attachee.concealed_set(0)
									game.timevent_add( talk_talk, ( attachee, obj ), 2000 )
									game.global_vars[536] = 4
			elif (game.global_vars[539] == 2):
				if (attachee.name == 8792):
					if (not game.combat_is_active()):
						for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
							if (close_enough(attachee, obj)):
								if (obj.skill_level_get(attachee,skill_spot) >= 19):
									attachee.concealed_set(0)
									game.timevent_add( talk_talk, ( attachee, obj ), 2000 )
									game.global_vars[536] = 4
			elif (game.global_vars[539] == 3):
				if (attachee.name == 8793):
					if (not game.combat_is_active()):
						for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
							if (close_enough(attachee, obj)):
								if (obj.skill_level_get(attachee,skill_spot) >= 19):
									attachee.concealed_set(0)
									game.timevent_add( talk_talk, ( attachee, obj ), 2000 )
									game.global_vars[536] = 4
			elif (game.global_vars[539] == 4):
				if (attachee.name == 8794):
					if (not game.combat_is_active()):
						for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
							if (close_enough(attachee, obj)):
								if (obj.skill_level_get(attachee,skill_spot) >= 19):
									attachee.concealed_set(0)
									game.timevent_add( talk_talk, ( attachee, obj ), 2000 )
									game.global_vars[536] = 4
			elif (game.global_vars[539] == 5):
				if (attachee.name == 8795):
					if (not game.combat_is_active()):
						for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
							if (close_enough(attachee, obj)):
								if (obj.skill_level_get(attachee,skill_spot) >= 19):
									attachee.concealed_set(0)
									game.timevent_add( talk_talk, ( attachee, obj ), 2000 )
									game.global_vars[536] = 4
			elif (game.global_vars[539] == 6):
				if (attachee.name == 8796):
					if (not game.combat_is_active()):
						for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
							if (close_enough(attachee, obj)):
								if (obj.skill_level_get(attachee,skill_spot) >= 19):
									attachee.concealed_set(0)
									game.timevent_add( talk_talk, ( attachee, obj ), 2000 )
									game.global_vars[536] = 4
			elif (game.global_vars[539] == 7):
				if (attachee.name == 8797):
					if (not game.combat_is_active()):
						for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
							if (close_enough(attachee, obj)):
								if (obj.skill_level_get(attachee,skill_spot) >= 19):
									attachee.concealed_set(0)
									game.timevent_add( talk_talk, ( attachee, obj ), 2000 )
									game.global_vars[536] = 4
			elif (game.global_vars[539] == 8):
				if (attachee.name == 8798):
					if (not game.combat_is_active()):
						for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
							if (close_enough(attachee, obj)):
								if (obj.skill_level_get(attachee,skill_spot) >= 19):
									attachee.concealed_set(0)
									game.timevent_add( talk_talk, ( attachee, obj ), 2000 )
									game.global_vars[536] = 4
	return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	game.global_vars[551] = 2
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
		attachee.reaction_set( pc, 50 )
	return RUN_DEFAULT


def close_enough(speaker,listener):
	if (speaker.distance_to(listener) <= 10):
		return 1
	return 0


def talk_talk( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	triggerer.begin_dialog( attachee, 1 )
	return RUN_DEFAULT


def increment_var_543( attachee, triggerer ):
	game.global_vars[543] = game.global_vars[543] + 1
	return


def increment_var_544( attachee, triggerer ):
	game.global_vars[544] = game.global_vars[544] + 1
	return


def increment_var_545( attachee, triggerer ):
	game.global_vars[545] = game.global_vars[545] + 1
	return


def go_to_sleep( attachee, triggerer ):
	attachee.condition_add_with_args("Unconscious",8200,0)
	return