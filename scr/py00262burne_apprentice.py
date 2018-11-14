from utilities import *
from toee import *
import _include
from co8Util.TimedEvent import *
from combat_standard_routines import *
from py00439script_daemon import get_f, set_f, get_v, set_v, tpsts, record_time_stamp


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 250 )			## pishella in party
	elif (attachee.map == 5014):
		triggerer.begin_dialog( attachee, 330 )			## WotGS Hommlet under attack
	elif (game.global_vars[911] == 32 and attachee.map != 5016 and attachee.map != 5019):
		triggerer.begin_dialog( attachee, 350 )			## have attacked 3 or more farm animals with pishella in party and not in castle main hall or parapet interior
	elif (game.leader.reputation_has(32) == 1 or game.leader.reputation_has(30) == 1 or game.leader.reputation_has(29) == 1):
		attachee.float_line(12014,triggerer)			## have lawbreaker or convict or banished from hommlet reps
	elif (game.global_flags[694] == 1):
		triggerer.begin_dialog( attachee, 400 )			## declined to share information on who is altering construction orders
	elif (game.party[0].reputation_has( 27 ) == 1): 
		triggerer.begin_dialog( attachee, 180 )			## have rabble-rouser reputation
	else:
		triggerer.begin_dialog( attachee, 1 )			## none of the above
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		if (attachee.map == 5016 or attachee.map == 5019):
			if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
				attachee.object_flag_set(OF_OFF)
			else:
				attachee.object_flag_unset(OF_OFF)
		elif (attachee.map == 5014):
			if (game.global_vars[510] != 2):
				if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6):
					attachee.object_flag_unset(OF_OFF)
			else:
				attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)
	if (game.global_flags[239] == 0):
		game.global_vars[23] = game.global_vars[23] + 1
		if game.global_vars[23] >= 2:
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
		if (game.global_vars[911] >= 3):
			if (attachee != OBJ_HANDLE_NULL):
				leader = attachee.leader_get()
				if (leader != OBJ_HANDLE_NULL):
					leader.follower_remove(attachee)
					attachee.float_line(22000,triggerer)
	return RUN_DEFAULT


def san_join( attachee, triggerer ):
	game.global_flags[239] = 1
	return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	game.global_flags[239] = 0
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
		attachee.reaction_set( pc, 50 )
	return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	randy1 = game.random_range(1,16)
	if ((attachee.map == 5012) and randy1 >= 14):
		attachee.float_line(500,triggerer)
	elif ((attachee.map == 5058) and randy1 >= 13):
		attachee.float_line(510,triggerer)
	return RUN_DEFAULT


def destroy_orb( attachee, triggerer ):
	game.global_flags[326] = 1
	# set timer for 4 days and then end game or go to verbo
	game.timevent_add( return_Zuggtmoy, ( attachee, triggerer ), 345600000 )
	record_time_stamp('s_zuggtmoy_banishment_initiate')
	return RUN_DEFAULT

def pishella_destroy_skull_while_party_npc(pc,npc):
	pisha = game.obj_create( 14447, npc.location )
	pisha.object_flag_set(OF_DONTDRAW)
	party_transfer_to( pisha, 2208 )
	party_transfer_to( pisha, 4003 )
	party_transfer_to( pisha, 4004 )
	party_transfer_to( pisha, 3603 )
	party_transfer_to( pisha, 2203 )
	pisha.object_flag_set(OF_OFF)
	
	
def play_effect( attachee, triggerer ):
	# play particle effect to destroy the orb
	game.particles( 'orb-destroy', attachee )
	game.sound(4036,1)
	return RUN_DEFAULT


def return_Zuggtmoy( attachee, triggerer):
	if (game.global_flags[188] == 0 and game.global_flags[189] == 0):
		set_f('s_zuggtmoy_gone')
		# play banishment movie
		game.fade(0,0,301,0)
		# play slides and end game or go to verbo
		if (game.global_flags[500] == 1):
			set_end_slides_nc( attachee, triggerer )
			game.moviequeue_play()
			game.areas[14] = 1
			game.timevent_add( game.fade_and_teleport, (0,0,0,5121,228,507), 1500 )
			return RUN_DEFAULT
		else:
			set_end_slides( attachee, triggerer )
			game.moviequeue_play_end_game()
			return SKIP_DEFAULT


def switch_to_tarah( attachee, triggerer, line):
	npc = find_npc_near(attachee,8805)
	pishella = find_npc_near(attachee,8069)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
		npc.turn_towards(pishella)
		pishella.turn_towards(npc)
	return SKIP_DEFAULT