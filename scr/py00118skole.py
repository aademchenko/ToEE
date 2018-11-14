from utilities import *
from InventoryRespawn import *
from toee import *
from combat_standard_routines import *
from py00439script_daemon import get_f, set_f, get_v, set_v, tpsts, record_time_stamp


def san_dialog( attachee, triggerer ):
	if (( game.global_flags[202] == 1 ) and ( game.quests[42].state != qs_completed )):
		triggerer.begin_dialog( attachee, 360 )
	elif (game.party[0].reputation_has( 23 ) == 1 and game.global_flags[94] == 1 and game.global_flags[851] == 0 and attachee.has_met(triggerer)): 
		triggerer.begin_dialog( attachee, 400 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[201] == 1):
		attachee.object_flag_set(OF_OFF)
		game.global_flags[202] = 0
	if (game.global_flags[913] == 0):
		game.timevent_add(respawn, (attachee), 604800000 ) #604800000ms is 1 week
		game.global_flags[913] = 1
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[202] = 0
	set_f('skole_dead')
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[202] = 1
	set_f('skole_dead', 0)
	return RUN_DEFAULT


def prepare_goons( attachee ):
	# This script schedules Skole's Goons
	# Reworked to use global timing system
	game.timevent_add( goons_attack, ( attachee, ), 259200000 )
	record_time_stamp('s_skole_goons')
	return RUN_DEFAULT	


def goons_attack( attachee ):
	if game.quests[42].state != qs_completed and get_f('s_skole_goons_scheduled') == 0 and get_f('skole_dead') == 0:
		set_f('s_skole_goons_scheduled')
		game.quests[42].state = qs_botched
		game.global_flags[202] = 1
		game.encounter_queue.append(3004)
	return RUN_DEFAULT


def respawn(attachee):
	box = find_container_near(attachee,1001)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 604800000 ) #604800000ms is 1 week
	return