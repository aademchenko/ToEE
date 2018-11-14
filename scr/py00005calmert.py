from utilities import *
from InventoryRespawn import *
from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if ( game.global_flags[28] == 1 and triggerer.reputation_has( 2 ) == 0 ):
		triggerer.reputation_add( 2 )
	if (attachee.map == 5013):
		attachee.float_line( 23000, triggerer )
	elif (attachee.has_met(triggerer)):
		if (game.global_vars[5] <= 7):
			attachee.turn_towards(triggerer)	## added by Livonya
			triggerer.begin_dialog( attachee, 10 )
		else:
			attachee.turn_towards(triggerer)	## added by Livonya
			triggerer.begin_dialog( attachee, 450 )
	else:
		attachee.turn_towards(triggerer)	## added by Livonya
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5012):
		if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
			attachee.object_flag_set(OF_OFF)
		else:
			attachee.object_flag_unset(OF_OFF)
			if (game.global_flags[817] == 1):
				attachee.object_flag_set(OF_OFF)
				return RUN_DEFAULT
			if (not game.combat_is_active()):
				game.global_vars[724] = 0
			if (game.global_flags[902] == 0):
				game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
				game.global_flags[902] = 1
	elif (attachee.map == 5013):
		if (game.global_vars[510] != 2):
			if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6):
				attachee.object_flag_unset(OF_OFF)
		else:
			attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[817] = 1
	game.global_vars[23] = game.global_vars[23] + 1
	if (game.global_vars[23] >= 2):
		game.party[0].reputation_add( 92 )
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if anyone( game.leader.group_list(), "has_follower", 8730 ):
		ron = find_npc_near(game.leader,8730)
		if ron != OBJ_HANDLE_NULL:
			game.leader.follower_remove( ron )
	if (game.global_flags[816] == 0 and game.global_flags[818] == 0):
		game.global_flags[818] = 1
		for target in game.party[0].group_list():
			if (target.name != 8072 and attachee.distance_to(target) <= 20 and target.type == obj_t_pc):
				attachee.turn_towards(target)
				target.begin_dialog(attachee,2000)
				return SKIP_DEFAULT
		attachee.float_line(2010,triggerer)
		terjon = game.obj_create( 14007, attachee.location-4 )
		game.particles( "sp-Dimension Door", terjon )
		terjon.turn_towards(attachee)	
		calmert = attachee.get_initiative()
		terjon.add_to_initiative()
		terjon.set_initiative( calmert )
		game.update_combat_ui()	
		terjon.attack(triggerer)
	for npc in game.party[0].group_list():
		if (npc.name == 8072 and npc.leader_get() != OBJ_HANDLE_NULL and game.global_flags[819] == 0):
			curr = npc.stat_level_get( stat_hp_current )
			if (curr >= 1): 
				for target in game.party[0].group_list():
					if (target.name != 8072 and npc.distance_to(target) <= 20 and target.type == obj_t_pc):
						npc.turn_towards(target)
						target.begin_dialog(npc,1000)
						return SKIP_DEFAULT
	if anyone( triggerer.group_list(), "has_follower", 8000 ):
		elmo = find_npc_near( triggerer, 8000 )
		if (elmo != OBJ_HANDLE_NULL):
			triggerer.follower_remove(elmo)
			elmo.float_line( 12021,triggerer )
			elmo.attack(triggerer)
	if anyone( triggerer.group_list(), "has_follower", 8001 ):
		paida = find_npc_near( triggerer, 8001 )
		if (paida != OBJ_HANDLE_NULL):
			triggerer.follower_remove(paida)
			paida.float_line( 12021,triggerer )
			paida.attack(triggerer)
	if anyone( triggerer.group_list(), "has_follower", 8014 ):
		otis = find_npc_near( triggerer, 8014 )
		if (otis != OBJ_HANDLE_NULL):
			triggerer.follower_remove(otis)
			otis.float_line( 12021,triggerer )
			otis.attack(triggerer)
	if anyone( triggerer.group_list(), "has_follower", 8015 ):
		meleny = find_npc_near( triggerer, 8015 )
		if (meleny != OBJ_HANDLE_NULL):
			triggerer.follower_remove(meleny)
			meleny.float_line( 12021,triggerer )
			meleny.attack(triggerer)
	if anyone( triggerer.group_list(), "has_follower", 8021 ):
		ydey = find_npc_near( triggerer, 8021 )
		if (ydey != OBJ_HANDLE_NULL):
			triggerer.follower_remove(ydey)
			ydey.float_line( 12021,triggerer )
			ydey.attack(triggerer)
	if anyone( triggerer.group_list(), "has_follower", 8022 ):
		murfles = find_npc_near( triggerer, 8022 )
		if (murfles != OBJ_HANDLE_NULL):
			triggerer.follower_remove(murfles)
			murfles.float_line( 12021,triggerer )
			murfles.attack(triggerer)
	if anyone( triggerer.group_list(), "has_follower", 8031 ):
		thrommel = find_npc_near( triggerer, 8031 )
		if (thrommel != OBJ_HANDLE_NULL):
			triggerer.follower_remove(thrommel)
			thrommel.float_line( 12021,triggerer )
			thrommel.attack(triggerer)
	if anyone( triggerer.group_list(), "has_follower", 8039 ):
		taki = find_npc_near( triggerer, 8039 )
		if (taki != OBJ_HANDLE_NULL):
			triggerer.follower_remove(taki)
			taki.float_line( 12021,triggerer )
			taki.attack(triggerer)
	if anyone( triggerer.group_list(), "has_follower", 8054 ):
		burne = find_npc_near( triggerer, 8054 )
		if (burne != OBJ_HANDLE_NULL):
			triggerer.follower_remove(burne)
			burne.float_line( 12021,triggerer )
			burne.attack(triggerer)
	if anyone( triggerer.group_list(), "has_follower", 8060 ):
		morgan = find_npc_near( triggerer, 8060 )
		if (morgan != OBJ_HANDLE_NULL):
			triggerer.follower_remove(morgan)
			morgan.float_line( 12021,triggerer )
			morgan.attack(triggerer)
	if anyone( triggerer.group_list(), "has_follower", 8069 ):
		pishella = find_npc_near( triggerer, 8069 )
		if (pishella != OBJ_HANDLE_NULL):
			triggerer.follower_remove(pishella)
			pishella.float_line( 12021,triggerer )
			pishella.attack(triggerer)
	if anyone( triggerer.group_list(), "has_follower", 8071 ):
		rufus = find_npc_near( triggerer, 8071 )
		if (rufus != OBJ_HANDLE_NULL):
			triggerer.follower_remove(rufus)
			rufus.float_line( 12021,triggerer )
			rufus.attack(triggerer)
	if anyone( triggerer.group_list(), "has_follower", 8714 ):
		holly = find_npc_near( triggerer, 8714 )
		if (holly != OBJ_HANDLE_NULL):
			triggerer.follower_remove(holly)
			holly.float_line( 1000,triggerer )
			holly.attack(triggerer)
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):	
	for npc in game.party[0].group_list():
		if (npc.name == 8072 and npc.leader_get() != OBJ_HANDLE_NULL and game.global_flags[819] == 0):
			curr = npc.stat_level_get( stat_hp_current )
			if (curr >= 1): 
				for target in game.party[0].group_list():
					if (target.name != 8072 and npc.distance_to(target) <= 20 and target.type == obj_t_pc):
						npc.turn_towards(target)
						target.begin_dialog(npc,1000)
						return SKIP_DEFAULT
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[817] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[724] == 0 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()) and game.party_alignment & ALIGNMENT_GOOD == 0:
		attachee.cast_spell(spell_death_ward, attachee)
		attachee.spells_pending_to_memorized()
	if (game.global_vars[724] == 4 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()) and game.party_alignment & ALIGNMENT_GOOD == 0:
		attachee.cast_spell(spell_shield_of_faith, attachee)
		attachee.spells_pending_to_memorized()
	game.global_vars[724] = game.global_vars[724] + 1
	return RUN_DEFAULT


def create_terjon( attachee, triggerer ):
	terjon = game.obj_create( 14007, attachee.location-4 )
	terjon.turn_towards(attachee)
	game.particles( "sp-Dimension Door", terjon )		
	return RUN_DEFAULT


def switch_to_terjon( npc, pc ):
	terjon = find_npc_near(npc,20003)
	for target in game.obj_list_vicinity(npc.location,OLC_PC):
		if (terjon.distance_to(target) <= 20 and target.type == obj_t_pc):
			terjon.turn_towards(target)
			target.begin_dialog(terjon,2020)
			return SKIP_DEFAULT
	terjon.float_line(2020,triggerer)
	terjon.attack(pc)
	return RUN_DEFAULT


def look_spugnoir( attachee, triggerer ):
	for npc in game.party[0].group_list():
		if (npc.name == 8072 and npc.leader_get() != OBJ_HANDLE_NULL and game.global_flags[819] == 0):
			curr = npc.stat_level_get( stat_hp_current )
			if (curr >= 1): 
				for target in game.party[0].group_list():
					if (npc.distance_to(target) <= 20 and target.type == obj_t_pc and npc.name != 8072):
						npc.turn_towards(target)
						target.begin_dialog(npc,1000)
						return SKIP_DEFAULT
	attachee.attack(triggerer)		
	return RUN_DEFAULT


def beggar_cavanaugh( attachee, triggerer ):
	game.timevent_add( beggar_now, ( attachee, triggerer ), 86400000 )
	return RUN_DEFAULT


def beggar_now( attachee, triggerer ):
	game.global_flags[205] = 1
	game.global_vars[24] = game.global_vars[24] + 1
	if (triggerer.reputation_has( 5 ) == 0):
		triggerer.reputation_add( 5 )
	if ( game.global_vars[24] >= 3 and triggerer.reputation_has( 6 ) == 0 ):
		triggerer.reputation_add( 6 )
	return RUN_DEFAULT


def respawn(attachee):
	box = find_container_near(attachee,1001)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
	return