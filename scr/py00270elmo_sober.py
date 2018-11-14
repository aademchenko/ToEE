from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (game.global_vars[900] == 32):
		triggerer.begin_dialog( attachee, 190 )			## have attacked 3 or more farm animals with elmo in party
	elif (attachee.has_met(triggerer)):
		if (attachee.leader_get() == OBJ_HANDLE_NULL):
			triggerer.begin_dialog( attachee, 90 )		## have met and elmo not in party
		triggerer.begin_dialog( attachee, 200 )			## elmo in party
	else:
		triggerer.begin_dialog( attachee, 1 )			## have not met
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)
	game.global_flags[934] = 1
	if (game.global_flags[236] == 0):
		game.global_vars[23] = game.global_vars[23] + 1
		if (game.global_vars[23] >= 2):
			game.party[0].reputation_add( 92 )
	else:
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (triggerer.type == obj_t_pc):
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
	game.global_flags[934] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (game.global_vars[900] >= 3):
			if (attachee != OBJ_HANDLE_NULL):
				leader = attachee.leader_get()
				if (leader != OBJ_HANDLE_NULL):
					leader.follower_remove(attachee)
					attachee.float_line(22000,triggerer)
		else:
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_safe_to_talk(attachee,obj)):
					if (not attachee.has_met(obj)):
						obj.begin_dialog(attachee,1)
#						game.new_sid = 0
	return RUN_DEFAULT


def san_join(attachee, triggerer):
	game.global_flags[236] = 1
	print "elmo joins"
	return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	game.global_flags[236] = 0
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
		attachee.reaction_set( pc, 50 )
	return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	randy1 = game.random_range(1,16)
	if ((attachee.map == 5052 or attachee.map == 5007) and randy1 >= 15):
		leader = attachee.leader_get()
		if (leader != OBJ_HANDLE_NULL):
			if (game.global_flags[934] == 0):
				attachee.float_line(12200,triggerer)
	return RUN_DEFAULT


def make_otis_talk( attachee, triggerer, line):
	npc = find_npc_near(attachee,8014)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,320)
	return SKIP_DEFAULT


def make_lila_talk( attachee, triggerer, line):
	npc = find_npc_near(attachee,14001)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,320)
	return SKIP_DEFAULT


def make_Fruella_talk( attachee, triggerer, line):
	npc = find_npc_near(attachee,14037)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	return SKIP_DEFAULT


def make_saduj_talk( attachee, triggerer, line):
	npc = find_npc_near(attachee,14689)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	return SKIP_DEFAULT


def switch_to_thrommel( attachee, triggerer):
	npc = find_npc_near(attachee,8031)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,40)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,570)
	return SKIP_DEFAULT


def elmo_joins_first_time( attachee, triggerer, sober ):	#edited by darmagon for sober elmo
	if sober:
		loc = attachee.location
		rot = attachee.rotation		
		attachee.destroy()
		new_elmo = game.obj_create(14723, loc)
	else:
		new_elmo = attachee
	triggerer.money_adj(-20000)	
	rchain = create_item_in_inventory( 6049, new_elmo )
	rchain.item_flag_set(OIF_NO_TRANSFER)
	mshield = create_item_in_inventory( 6051, new_elmo)
	mshield.item_flag_set(OIF_NO_TRANSFER)
	maxe = create_item_in_inventory( 4098, new_elmo )
	maxe.item_flag_set(OIF_NO_TRANSFER)
	magd = attachee.item_find( 4058 )
	if magd != OBJ_HANDLE_NULL:
		magd.item_flag_set(OIF_NO_TRANSFER)
	new_elmo.item_wield_best_all()
	if sober:
		triggerer.begin_dialog(new_elmo, 70)
	return SKIP_DEFAULT


def equip_transfer( attachee, triggerer ):
	rchain = attachee.item_find( 6049 )
	if rchain != OBJ_HANDLE_NULL:
		rchain.item_flag_unset(OIF_NO_TRANSFER)
	mshield = attachee.item_find( 6051 )
	if mshield != OBJ_HANDLE_NULL:
		mshield.item_flag_unset(OIF_NO_TRANSFER)
	maxe = attachee.item_find( 4098 )
	if maxe != OBJ_HANDLE_NULL:
		maxe.item_flag_unset(OIF_NO_TRANSFER)
	return


def san_join(attachee, triggerer):
	print "elmo joins"
	return RUN_DEFAULT