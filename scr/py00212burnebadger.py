from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6):
		attachee.float_line( 23000, triggerer )
	elif (game.global_flags[835] == 1 and game.global_flags[37] == 0 and game.global_flags[842] == 0 and game.global_flags[839] == 0):
		triggerer.begin_dialog(attachee,300)
	elif (game.party[0].reputation_has( 27 ) == 1): 
		triggerer.begin_dialog( attachee,120)
	elif (attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee,130)
	else:
		triggerer.begin_dialog(attachee,1)
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5007 or attachee.map == 5016 or attachee.map == 5017 or attachee.map == 5018):
		if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
			attachee.object_flag_set(OF_OFF)
		else:
			attachee.object_flag_unset(OF_OFF)
	elif (attachee.map == 5006 or attachee.map == 5014 or attachee.map == 5015):
		if (game.global_vars[510] != 2):
			if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6):
				attachee.object_flag_unset(OF_OFF)
		else:
			attachee.object_flag_set(OF_OFF)
	elif (attachee.map == 5042):
		if (game.global_vars[510] == 2):
			attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (game.party[0].reputation_has(92) == 1):
		attachee.float_line(1000,triggerer)
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
			paida.attack(triggerer)
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
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.map == 5001):
		if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
			attachee.object_flag_set(OF_OFF)
		else:
			attachee.object_flag_unset(OF_OFF)
	if (attachee.map == 5014 or attachee.map == 5015 or attachee.map == 5016 or attachee.map == 5017 or attachee.map == 5018 or attachee.map == 5019):
		for obj in game.obj_list_vicinity(attachee.location,OLC_CRITTERS):
			if (obj.name == 14614 and attachee.can_see(obj)):
				attachee.attack(obj)
				return RUN_DEFAULT
	if (attachee.map == 5015 and game.global_flags[845] == 0 and game.global_flags[846] == 0):
		if (attachee.can_see(game.party[0])):
			game.party[0].begin_dialog( attachee, 200 )
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (attachee.can_see(obj)):
				obj.begin_dialog( attachee, 200 )
	return RUN_DEFAULT


def san_will_kos( attachee, triggerer ):
	if (game.party[0].reputation_has(92) == 0):
		return SKIP_DEFAULT
	return RUN_DEFAULT