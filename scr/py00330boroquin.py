from toee import *
from utilities import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.quests[109].state == qs_completed):
		triggerer.begin_dialog( attachee, 430 )
	elif (game.global_flags[538] == 1):
		triggerer.begin_dialog( attachee, 400 )
	elif (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 180 )
	elif (game.global_flags[535] == 1):
		triggerer.begin_dialog( attachee, 420 )
	elif (attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 110 )
	else:
		triggerer.begin_dialog( attachee, 10 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5169 and game.global_vars[549] == 1):
		if (attachee.leader_get() == OBJ_HANDLE_NULL):
			attachee.object_flag_set(OF_OFF)
	elif (attachee.map == 5172 and game.global_vars[549] == 1):
		if (attachee.leader_get() == OBJ_HANDLE_NULL):
			attachee.object_flag_unset(OF_OFF)	
	elif (attachee.map == 5141):
		if (game.quests[109].state == qs_completed and game.global_vars[542] == 1):
			attachee.object_flag_set(OF_OFF)
		elif (is_daytime() == 1):
			attachee.object_flag_unset(OF_OFF)
		elif (is_daytime() == 0):
			attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	game.global_flags[540] = 1
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (triggerer.type == obj_t_pc):
		if (game.quests[109].state == qs_unknown or game.quests[109].state == qs_completed or game.quests[109].state == qs_botched):
			if anyone( triggerer.group_list(), "has_follower", 8000 ):
				elmo = find_npc_near( triggerer, 8000 )
				if (elmo != OBJ_HANDLE_NULL):
					triggerer.follower_remove(elmo)
					elmo.float_line( 20000,triggerer )
					elmo.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8001 ):
				paida = find_npc_near( triggerer, 8001 )
				if (paida != OBJ_HANDLE_NULL):
					triggerer.follower_remove(paida)
					paida.float_line( 20000,triggerer )
					paida.runoff(paida.location-3)
			if anyone( triggerer.group_list(), "has_follower", 8014 ):
				otis = find_npc_near( triggerer, 8014 )
				if (otis != OBJ_HANDLE_NULL):
					triggerer.follower_remove(otis)
					otis.float_line( 20000,triggerer )
					otis.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8015 ):
				meleny = find_npc_near( triggerer, 8015 )
				if (meleny != OBJ_HANDLE_NULL):
					triggerer.follower_remove(meleny)
					meleny.float_line( 20000,triggerer )
					meleny.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8021 ):
				ydey = find_npc_near( triggerer, 8021 )
				if (ydey != OBJ_HANDLE_NULL):
					triggerer.follower_remove(ydey)
					ydey.float_line( 20000,triggerer )
					ydey.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8022 ):
				murfles = find_npc_near( triggerer, 8022 )
				if (murfles != OBJ_HANDLE_NULL):
					triggerer.follower_remove(murfles)
					murfles.float_line( 20000,triggerer )
					murfles.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8031 ):
				thrommel = find_npc_near( triggerer, 8031 )
				if (thrommel != OBJ_HANDLE_NULL):
					triggerer.follower_remove(thrommel)
					thrommel.float_line( 20000,triggerer )
					thrommel.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8039 ):
				taki = find_npc_near( triggerer, 8039 )
				if (taki != OBJ_HANDLE_NULL):
					triggerer.follower_remove(taki)
					taki.float_line( 20000,triggerer )
					taki.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8054 ):
				burne = find_npc_near( triggerer, 8054 )
				if (burne != OBJ_HANDLE_NULL):
					triggerer.follower_remove(burne)
					burne.float_line( 20000,triggerer )
					burne.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8060 ):
				morgan = find_npc_near( triggerer, 8060 )
				if (morgan != OBJ_HANDLE_NULL):
					triggerer.follower_remove(morgan)
					morgan.float_line( 20000,triggerer )
					morgan.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8069 ):
				pishella = find_npc_near( triggerer, 8069 )
				if (pishella != OBJ_HANDLE_NULL):
					triggerer.follower_remove(pishella)
					pishella.float_line( 20000,triggerer )
					pishella.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8071 ):
				rufus = find_npc_near( triggerer, 8071 )
				if (rufus != OBJ_HANDLE_NULL):
					triggerer.follower_remove(rufus)
					rufus.float_line( 20000,triggerer )
					rufus.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8072 ):
				spugnoir = find_npc_near( triggerer, 8072 )
				if (spugnoir != OBJ_HANDLE_NULL):
					triggerer.follower_remove(spugnoir)
					spugnoir.float_line( 20000,triggerer )
					spugnoir.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8714 ):
				holly = find_npc_near( triggerer, 8714 )
				if (holly != OBJ_HANDLE_NULL):
					triggerer.follower_remove(holly)
					holly.float_line( 20000,triggerer )
					holly.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8730 ):
				ronald = find_npc_near( triggerer, 8730 )
				if (ronald != OBJ_HANDLE_NULL):
					triggerer.follower_remove(ronald)
					ronald.float_line( 20000,triggerer )
					ronald.attack(triggerer)
			if anyone( triggerer.group_list(), "has_follower", 8731 ):
				ariakas = find_npc_near( triggerer, 8731 )
				if (ariakas != OBJ_HANDLE_NULL):
					triggerer.follower_remove(ariakas)
					ariakas.float_line( 20000,triggerer )
					ariakas.attack(triggerer)
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	return SKIP_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[540] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (game.global_flags[538] == 1):
			triggerer.follower_remove(attachee)
			game.new_sid = 0
		else:
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_better_to_talk(attachee,obj)):
					if (game.global_flags[545] == 0):
						game.timevent_add( howdy_ho, ( attachee, triggerer ), 2000 )
						game.global_flags[545] = 1
	return RUN_DEFAULT


def san_spell_cast( attachee, triggerer, spell ):
	if ( spell.spell == spell_charm_person or spell.spell == spell_charm_monster ):
		game.global_flags[538] = 1
		game.timevent_add( revert_ggf_538, ( attachee, triggerer ), 3600000 )
	return RUN_DEFAULT


def increment_var_536( attachee, triggerer ):
	if (not attachee.has_met(triggerer)):
		game.global_vars[536] = game.global_vars[536] + 1
	return


def increment_var_543( attachee, triggerer ):
	game.global_vars[543] = game.global_vars[543] + 1
	return


def increment_var_544( attachee, triggerer ):
	game.global_vars[544] = game.global_vars[544] + 1
	return


def increment_var_545( attachee, triggerer ):
	game.global_vars[545] = game.global_vars[545] + 1
	return


def increment_var_555( attachee, triggerer ):
	game.global_vars[555] = game.global_vars[555] + 1
	game.new_sid = 0
	return


def increment_var_557( attachee, triggerer ):
	game.global_vars[557] = game.global_vars[557] + 1
	game.new_sid = 0
	return


def is_better_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 40):
			return 1
	return 0


def howdy_ho( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 10 )
	return RUN_DEFAULT


def gen_panathaes_loc( attachee, triggerer ):
	if (game.global_vars[539] == 0):
		chooser = game.random_range(1,8)
		if (chooser == 1):
			game.global_vars[539] = 1
		elif (chooser == 2):
			game.global_vars[539] = 2
		elif (chooser == 3):
			game.global_vars[539] = 3
		elif (chooser == 4):
			game.global_vars[539] = 4
		elif (chooser == 5):
			game.global_vars[539] = 5
		elif (chooser == 6):
			game.global_vars[539] = 6
		elif (chooser == 7):
			game.global_vars[539] = 7
		elif (chooser == 8):
			game.global_vars[539] = 8
	return


def pick_kidnapper( attachee, triggerer ):
	if (game.global_vars[542] == 0):
		picker = game.random_range(1,4)
		if (picker == 1):
			game.global_vars[542] = 1
			# boroquin is kidnapper
		elif (picker == 2 or picker == 3):
			game.global_vars[542] = 2
			# panathaes is kidnapper
		elif (picker == 4):
			game.global_vars[542] = 3
			# rakham is kidnapper
	return


def gen_kids_loc( attachee, triggerer ):
	if (game.global_vars[540] == 0 and game.global_vars[541] == 0):
		chooser = game.random_range(1,4)
		if (chooser == 1):
			game.global_vars[540] = 1
			game.global_vars[541] = 1
		elif (chooser == 2):
			game.global_vars[540] = 2
			game.global_vars[541] = 2
		elif (chooser == 3):
			game.global_vars[540] = 3
			game.global_vars[541] = 3
		elif (chooser == 4):
			game.global_vars[540] = 4
			game.global_vars[541] = 4
	return


def check_for_locket( attachee, triggerer ):
	if (game.global_vars[542] == 1):
		create_item_in_inventory(11060,attachee)
	return


def check_evidence_rep_bor( attachee, triggerer ):
	if (game.party[0].reputation_has(72)==1):
		game.party[0].reputation_add(75)
		game.party[0].reputation_remove(72)
	elif (game.party[0].reputation_has(69)==1):
		game.party[0].reputation_add(72)
		game.party[0].reputation_remove(69)
	elif (game.party[0].reputation_has(69)==0):
		if (game.party[0].reputation_has(72)==0):
			if (game.party[0].reputation_has(75)==0):
				game.party[0].reputation_add(69)
	return


def check_evidence_rep_pan( attachee, triggerer ):
	if (game.party[0].reputation_has(73)==1):
		game.party[0].reputation_add(76)
		game.party[0].reputation_remove(73)
	elif (game.party[0].reputation_has(70)==1):
		game.party[0].reputation_add(73)
		game.party[0].reputation_remove(70)
	elif (game.party[0].reputation_has(70)==0):
		if (game.party[0].reputation_has(73)==0):
			if (game.party[0].reputation_has(76)==0):
				game.party[0].reputation_add(70)
	return


def check_evidence_rep_rak( attachee, triggerer ):
	if (game.party[0].reputation_has(74)==1):
		game.party[0].reputation_add(77)
		game.party[0].reputation_remove(74)
	elif (game.party[0].reputation_has(71)==1):
		game.party[0].reputation_add(74)
		game.party[0].reputation_remove(71)
	elif (game.party[0].reputation_has(71)==0):
		if (game.party[0].reputation_has(74)==0):
			if (game.party[0].reputation_has(77)==0):
				game.party[0].reputation_add(71)
	return


def revert_ggf_538( attachee, triggerer ):
	game.global_flags[538] = 0
	return RUN_DEFAULT