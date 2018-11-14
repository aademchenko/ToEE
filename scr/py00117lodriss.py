from utilities import *
from InventoryRespawn import *
from toee import *
from combat_standard_routines import *
from py00439script_daemon import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	# Respawn 
	if (game.global_flags[912] == 0):
		game.timevent_add(respawn, (attachee), 604800000 ) #604800000ms is 1 week
		game.global_flags[912] = 1

	# The 'evac' routine
	if get_f('boatmens_tavern_evac_on') and game.leader.map == 5052:
		game.timevent_add(set_f, ('boatmens_tavern_evac_on', 0), 300 )
		if attachee.name == 14133 and get_f('lodriss_killed_outside') == 0: # For Lodriss
			attachee.object_flag_unset(OF_OFF)
		else : # For the others
			attachee.object_flag_unset(OF_OFF)
	#game.new_sid = 0
	if attachee.name == 14152 and game.leader.map == 5051: # Tolub, outside
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[369] = 1
	if game.quests[42].state >= qs_mentioned:
		game.quests[42].state = qs_completed
		triggerer.reputation_add( 21 )
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	if game.quests[42].state == qs_completed:
		game.quests[42].state = qs_botched
		triggerer.reputation_remove( 21 )
	game.global_flags[369] = 0
	return RUN_DEFAULT


def kill_lodriss( attachee ):
	attachee.object_flag_set(OF_OFF)
	set_f('lodriss_killed_outside')
	return RUN_DEFAULT


def kill_skole( attachee ):
	game.timevent_add( skole_dead, ( attachee, ), 86400000 )
	return RUN_DEFAULT


def skole_dead( attachee ):
	game.global_flags[201] = 1
	return RUN_DEFAULT


def get_rep( attachee, triggerer ):
	if triggerer.reputation_has( 7 ) == 0:
		triggerer.reputation_add( 7 )
	game.global_vars[25] = game.global_vars[25] + 1
	if ( game.global_vars[25] >= 3 and triggerer.reputation_has( 8 ) == 0):
		triggerer.reputation_add( 8 )
	return RUN_DEFAULT

def make_like( attachee, triggerer ):
	if ( attachee.reaction_get( triggerer ) <= 71 ):
		attachee.reaction_set( triggerer, 71 )
	return SKIP_DEFAULT


def check_skole( attachee ):
	skole = find_npc_near(attachee, 14134)
	if ( skole == OBJ_HANDLE_NULL ):
		return 0

	skole_whacked = 0
	if (skole.stat_level_get(stat_subdual_damage) > 0 or obj_percent_hp(skole) < 100 or skole.leader_get() != OBJ_HANDLE_NULL):
		skole_whacked = 1
	if ( skole_whacked == 0  and ( game.global_flags[202] == 1 or game.global_flags[102] == 1)):
		return 1
	return 0


def evac_partial( attachee ):
	set_f('boatmens_tavern_evac_on')
	attachee.scripts[10] = 117
	attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def evac( attachee ):
	set_f('boatmens_tavern_evac_on')
	attachee.scripts[10] = 117 # san_first_heartbeat
	for obj in game.obj_list_vicinity( attachee.location, OLC_NPC):
		if (obj.leader_get() == OBJ_HANDLE_NULL):
			if (obj.name == 14133 or obj.name == 8020 or obj.name == 8057 or obj.name == 14374 or obj.name == 14290 or obj.name == 14372 or obj.name == 14152):
				obj.scripts[10] = 117
				obj.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def respawn(attachee):
	box = find_container_near(attachee,1004)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 604800000 ) #604800000ms is 1 week
	return