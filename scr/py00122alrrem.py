from toee import *
from utilities import *
from py00439script_daemon import record_time_stamp, get_v, set_v, npc_set, npc_unset, npc_get, tsc, tpsts, within_rect_by_corners, buffee
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	record_time_stamp(517)
	triggerer.turn_towards(attachee)			## added by Livonya
	attachee.turn_towards(triggerer)			## added by Livonya
	if ( anyone(triggerer.group_list(),"has_follower",8031) ):
	# Prince Thrommel in your party
			triggerer.begin_dialog( attachee, 700 )
	elif ( anyone(triggerer.group_list(),"has_follower",8040) and (game.global_flags[192] == 0) ):
	# Ashrem in your party
		triggerer.begin_dialog( attachee, 860 )
	elif ( (game.global_flags[115] == 1) and (game.global_flags[116] == 1) and (game.global_flags[125] == 0) ):
	# Tubal and Antonio are dead (116 & 115 respectively), and you haven't bluffed him yet (125)
		triggerer.begin_dialog( attachee, 400 )
	elif (not attachee.has_met(triggerer)):
		if (game.global_flags[92] == 1):
		# Recruited via Wat
			triggerer.begin_dialog( attachee, 200 )
		else:
		# Waltzing In (TM)
			triggerer.begin_dialog( attachee, 1 )
	else:
		# "What news have you for me"
		triggerer.begin_dialog( attachee, 300 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[372] == 1):
		attachee.object_flag_set(OF_OFF)
	else:
		if (attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
			game.global_vars[713] = 0
		if (game.global_flags[312] == 1):
			attachee.object_flag_set(OF_OFF)
			game.global_flags[107] = 1
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[107] = 1
	record_time_stamp(459)
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	game.global_flags[344] = 0
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[107] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (not attachee.has_met(obj)):
				if (is_safe_to_talk(attachee,obj)):
					record_time_stamp(517)
					if ( anyone(triggerer.group_list(),"has_follower",8031) ):
					# Thrommel in Party
						obj.turn_towards(attachee)	## added by Livonya
						attachee.turn_towards(obj)	## added by Livonya
						obj.begin_dialog( attachee, 700 )
					elif ( anyone(triggerer.group_list(),"has_follower",8040) and (game.global_flags[192] == 0) ):
					# Ashrem in Party
						obj.turn_towards(attachee)	## added by Livonya
						attachee.turn_towards(obj)	## added by Livonya
						obj.begin_dialog( attachee, 860 )
					elif ( (game.global_flags[104] == 1) or (game.global_flags[105] == 1) or (game.global_flags[106] == 1) ):
					# Killed one of the other priests
						obj.turn_towards(attachee)	## added by Livonya
						attachee.turn_towards(obj)	## added by Livonya
						obj.begin_dialog( attachee, 730 )
					elif (game.global_flags[92] == 1):
					# Recruited by Wat
						obj.turn_towards(attachee)	## added by Livonya
						attachee.turn_towards(obj)	## added by Livonya
						obj.begin_dialog( attachee, 200 )
					else:
						obj.turn_towards(attachee)	## added by Livonya
						attachee.turn_towards(obj)	## added by Livonya
						obj.begin_dialog(attachee,1)
						#game.new_sid = 0			## removed by Livonya

	#########################################################
	# Prebuffing self and Underpriests			#
	# Added by Livonya, modified by S.A. Oct-2009		#
	#########################################################
	if (game.global_vars[713] == 2 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
		attachee.cast_spell(spell_resist_elements, attachee)
		attachee.spells_pending_to_memorized()
	if (game.global_vars[713] == 6 and not game.combat_is_active()):
		Tubal = find_npc_near(attachee, 14212)
		if Tubal != OBJ_HANDLE_NULL and Tubal.leader_get() == OBJ_HANDLE_NULL:
			Tubal.cast_spell(spell_resist_elements, Tubal)
			Tubal.spells_pending_to_memorized()
		Antonio = find_npc_near(attachee, 14211)
		if Antonio != OBJ_HANDLE_NULL and Antonio.leader_get() == OBJ_HANDLE_NULL:
			Antonio.cast_spell(spell_resist_elements, Antonio)
			Antonio.spells_pending_to_memorized()
	if (game.global_vars[713] == 8 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
		attachee.cast_spell(spell_protection_from_elements, attachee)
		attachee.spells_pending_to_memorized()
	if (game.global_vars[713] == 10 and not game.combat_is_active()):
		Tubal = find_npc_near(attachee, 14212)
		if Tubal != OBJ_HANDLE_NULL and Tubal.leader_get() == OBJ_HANDLE_NULL:
			Tubal.cast_spell(spell_endure_elements, Tubal)
			Tubal.spells_pending_to_memorized()
	if (game.global_vars[713] == 11 and not game.combat_is_active()):
		Antonio = find_npc_near(attachee, 14211)
		if Antonio != OBJ_HANDLE_NULL and Antonio.leader_get() == OBJ_HANDLE_NULL:
			Antonio.cast_spell(spell_endure_elements, Antonio)
			Antonio.spells_pending_to_memorized()
	if (game.global_vars[713] == 12 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
		attachee.cast_spell(spell_freedom_of_movement, attachee)
		attachee.spells_pending_to_memorized()

	#########################################################
	# Prebuffing other critters when on Fire Temple Alert	#
	# Added by S.A. Oct-2009				#
	#########################################################
	if get_v(454) & 8 != 0 and game.global_vars[713] > 12 and game.global_vars[713] < 100:

		if (game.global_vars[713] == 16 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
			buff_list = [14344, 14195, 14343] # Werewolf, Oohlgrist, Hydra
			mang1 = buffee( attachee.location, 20, buff_list, [] )
			if mang1 == OBJ_HANDLE_NULL:
				game.global_vars[713] = game.global_vars[713] + 1
				return RUN_DEFAULT
			attachee.cast_spell(spell_freedom_of_movement, mang1)
			attachee.spells_pending_to_memorized()

		if (game.global_vars[713] == 17 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
			buff_list = [14344, 14195, 14343] # Werewolf, Oohlgrist, Hydra
			Tubal = find_npc_near(attachee, 14212)
			mang1 = buffee( Tubal.location, 20, buff_list, [] )
			if mang1 == OBJ_HANDLE_NULL:
				game.global_vars[713] = game.global_vars[713] + 1
				return RUN_DEFAULT
			if Tubal != OBJ_HANDLE_NULL and Tubal.leader_get() == OBJ_HANDLE_NULL:
				Tubal.cast_spell(spell_endure_elements, mang1)
				Tubal.spells_pending_to_memorized()

		if (game.global_vars[713] == 18 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
			buff_list = [14344, 14224] # Werewolf, Aern
			Antonio = find_npc_near(attachee, 14211)
			mang1 = buffee( Antonio.location, 20, buff_list, [] )
			if mang1 == OBJ_HANDLE_NULL:
				game.global_vars[713] = game.global_vars[713] + 1
				return RUN_DEFAULT
			if Antonio != OBJ_HANDLE_NULL and Antonio.leader_get() == OBJ_HANDLE_NULL:
				Antonio.cast_spell(spell_endure_elements, mang1)
				Antonio.spells_pending_to_memorized()

		if (game.global_vars[713] == 20 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
			buff_list = [14344, 14195, 14343] # Werewolf, Oohlgrist, Hydra
			mang1 = buffee( attachee.location, 20, buff_list, [] )
			if mang1 == OBJ_HANDLE_NULL:
				game.global_vars[713] = game.global_vars[713] + 1
				return RUN_DEFAULT
			attachee.cast_spell(spell_resist_elements, mang1)
			attachee.spells_pending_to_memorized()

		if (game.global_vars[713] == 24 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
			Tubal = find_npc_near(attachee, 14212)
			Tubal.turn_towards(attachee)
			buff_list = [14344, 14195, 14343] # Werewolf, Oohlgrist, Hydra
			mang1 = buffee( attachee.location, 20, buff_list, [] )
			if mang1 == OBJ_HANDLE_NULL:
				game.global_vars[713] = game.global_vars[713] + 1
				return RUN_DEFAULT
			attachee.cast_spell(spell_magic_circle_against_good, mang1)
			attachee.spells_pending_to_memorized()

		if (game.global_vars[713] == 28 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
			buff_list = [14344, 14195, 14343] # Werewolf, Oohlgrist, Hydra
			mang1 = buffee( attachee.location, 20, buff_list, [] )
			mang2 = buffee( attachee.location, 20, buff_list, [mang1] )
			if mang2 == OBJ_HANDLE_NULL:
				game.global_vars[713] = game.global_vars[713] + 1
				return RUN_DEFAULT
			attachee.cast_spell(spell_endure_elements, mang2)
			attachee.spells_pending_to_memorized()

		if (game.global_vars[713] == 32 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
			Antonio = find_npc_near(attachee, 14211)
			if Antonio != OBJ_HANDLE_NULL:
				attachee.turn_towards(Antonio)

	#########################################################
	# End of section					#
	#########################################################

	game.global_vars[713] = game.global_vars[713] + 1
	return RUN_DEFAULT


def escort_below( attachee, triggerer ):
	# game.global_flags[144] = 1
	game.global_vars[691] = 3
	game.fade_and_teleport(0,0,0,5080,478,451)
	return RUN_DEFAULT


def talk_Ashrem( attachee, triggerer, line):
	ashrem = find_npc_near(attachee,8040)
	if (ashrem != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(ashrem,line)
		ashrem.turn_towards(attachee)
		attachee.turn_towards(ashrem)
	return SKIP_DEFAULT