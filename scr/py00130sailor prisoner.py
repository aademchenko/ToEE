from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.area != 3):
		if (attachee.leader_get() != OBJ_HANDLE_NULL):
			triggerer.begin_dialog( attachee, 90 )		## morgan in party
		if (game.global_vars[910] == 32):
			triggerer.begin_dialog( attachee, 130 )		## have attacked 3 or more farm animals with morgan in party
		elif (attachee.has_met(triggerer)):
			triggerer.begin_dialog( attachee, 80 )		## have met
		else:
			triggerer.begin_dialog( attachee, 1 )		## none of the above
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[291] == 1):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
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
	attachee.float_line(12057,triggerer)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (game.global_vars[910] >= 3):
			if (attachee != OBJ_HANDLE_NULL):
				leader = attachee.leader_get()
				if (leader != OBJ_HANDLE_NULL):
					leader.follower_remove(attachee)
					attachee.float_line(22000,triggerer)
	return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	if (attachee.area == 3):
		obj = attachee.leader_get()
		if (obj != OBJ_HANDLE_NULL):
			obj.begin_dialog(attachee, 110)
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	game.global_flags[291] = 1
	return RUN_DEFAULT


def get_rep( attachee, triggerer ):
	if triggerer.reputation_has( 16 ) == 0:
		triggerer.reputation_add( 16 )
	game.global_vars[26] = game.global_vars[26] + 1
	if ( game.global_vars[26] >= 3 and triggerer.reputation_has( 17 ) == 0):
		triggerer.reputation_add( 17 )
	return RUN_DEFAULT