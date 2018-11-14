from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 330 )			## burne in party
	elif (game.global_vars[909] == 32 and attachee.map != 5016 and attachee.map != 5018):
		triggerer.begin_dialog( attachee, 1060 )		## have attacked 3 or more farm animals with burne in party and not in castle main hall or upper hall
	elif (game.global_flags[839] == 1):
		triggerer.begin_dialog(attachee,1160)			## have liberated lareth
	elif (game.global_flags[835] == 1 and game.global_flags[37] == 0 and game.global_flags[842] == 1 and game.global_flags[839] == 0):
		triggerer.begin_dialog(attachee,1000)			## handled tower fight diplomatically and lareth is alive and have heard about prisoner lareth and have not liberated lareth
	elif (game.party[0].reputation_has( 28 ) == 1): 
		triggerer.begin_dialog( attachee, 590 )			## have dominatrix reputation - burne will kiss your ass
	elif (game.party[0].reputation_has( 27 ) == 1): 
		triggerer.begin_dialog( attachee, 11002 )		## have rabble-rouser reputation - burne won't talk to you
	else:
		triggerer.begin_dialog( attachee, 1 )			## none of the above
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		if ((game.global_vars[501] >= 2 and game.quests[97].state != qs_completed and game.quests[96].state != qs_completed) or game.global_vars[510] == 2):
			attachee.object_flag_set(OF_OFF)
		else:
			attachee.object_flag_unset(OF_OFF)
			if (not game.combat_is_active()):
				game.global_vars[730] = 0
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)
	game.global_flags[336] = 1
	game.global_flags[282] = 1
	if (game.global_flags[231] == 0):
		game.global_vars[23] = game.global_vars[23] + 1
		if (game.global_vars[23] >= 2):
			game.party[0].reputation_add( 92 )
	else:
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (triggerer.type == obj_t_pc):
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


def san_resurrect( attachee, triggerer ):
	game.global_flags[336] = 0
	game.global_flags[282] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (game.global_vars[909] >= 3):
			if (attachee != OBJ_HANDLE_NULL):
				leader = attachee.leader_get()
				if (leader != OBJ_HANDLE_NULL):
					leader.follower_remove(attachee)
					attachee.float_line(22000,triggerer)
		if (game.global_vars[730] == 0 and attachee.leader_get() == OBJ_HANDLE_NULL):
			attachee.cast_spell(spell_mage_armor, attachee)
			attachee.spells_pending_to_memorized()
			game.global_vars[730] = 1
	return RUN_DEFAULT


def san_join( attachee, triggerer ):
	game.global_flags[231] = 1
	diamond = attachee.item_find( 12036 )
	diamond.item_flag_set(OIF_NO_TRANSFER)
	amber = attachee.item_find( 12040 )
	amber.item_flag_set(OIF_NO_TRANSFER)
	silver_medallion_necklace = attachee.item_find( 6197 )
	silver_medallion_necklace.item_flag_set(OIF_NO_TRANSFER)
	emerald = attachee.item_find( 12010 )
	emerald.item_flag_set(OIF_NO_TRANSFER)
	silver_necklace = attachee.item_find( 6194 )
	silver_necklace.item_flag_set(OIF_NO_TRANSFER)
	dagger = attachee.item_find( 4058 )
	dagger.item_flag_set(OIF_NO_TRANSFER)
	wand = attachee.item_find( 12007 )
	wand.item_flag_set(OIF_NO_TRANSFER)
	chime = attachee.item_find( 12008 )
	chime.item_flag_set(OIF_NO_TRANSFER)
	ring = attachee.item_find( 6083 )
	ring.item_flag_set(OIF_NO_TRANSFER)
	kit = attachee.item_find( 12848 )
	kit.item_flag_set(OIF_NO_TRANSFER)
	return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	game.global_flags[231] = 0
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
		attachee.reaction_set( pc, 50 )
	diamond = attachee.item_find( 12036 )
	diamond.item_flag_unset(OIF_NO_TRANSFER)
	amber = attachee.item_find( 12040 )
	amber.item_flag_unset(OIF_NO_TRANSFER)
	silver_medallion_necklace = attachee.item_find( 6197 )
	silver_medallion_necklace.item_flag_unset(OIF_NO_TRANSFER)
	emerald = attachee.item_find( 12010 )
	emerald.item_flag_unset(OIF_NO_TRANSFER)
	silver_necklace = attachee.item_find( 6194 )
	silver_necklace.item_flag_unset(OIF_NO_TRANSFER)
	dagger = attachee.item_find( 4058 )
	dagger.item_flag_unset(OIF_NO_TRANSFER)
	wand = attachee.item_find( 12007 )
	wand.item_flag_unset(OIF_NO_TRANSFER)
	chime = attachee.item_find( 12008 )
	chime.item_flag_unset(OIF_NO_TRANSFER)
	ring = attachee.item_find( 6083 )
	ring.item_flag_unset(OIF_NO_TRANSFER)
	kit = attachee.item_find( 12848 )
	kit.item_flag_unset(OIF_NO_TRANSFER)
	return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	if ( game.global_flags[195] == 1 ):
		game.leader.begin_dialog( attachee, 480 )
	return SKIP_DEFAULT