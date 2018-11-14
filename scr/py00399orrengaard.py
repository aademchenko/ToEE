from toee import *
from utilities import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 7 )
	if (attachee.has_met( triggerer ) or game.global_vars[938] == 1):
		triggerer.begin_dialog( attachee, 4 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.timevent_add( new_orrengaard, ( attachee ), 86400000 )	#1 day
	boots = attachee.item_find( 6011 )
	boots.object_flag_set(OF_OFF)
	gloves = attachee.item_find( 6012 )
	gloves.object_flag_set(OF_OFF)
	clothes = attachee.item_find( 6344 )
	clothes.object_flag_set(OF_OFF)
	staff = attachee.item_find( 4214 )
	staff.object_flag_set(OF_OFF)
	robe = attachee.item_find( 6333 )
	robe.object_flag_set(OF_OFF)
	circlet = attachee.item_find( 6335 )
	circlet.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_first_heartbeat( attachee, triggerer ):		#used by an NPC cabbage to respawn orrengaard
	if (game.global_vars[938] == 2):
		orrengaard = game.obj_create( 14570, location_from_axis (555L, 572L) )
		orrengaard.rotation = 3.0
		game.global_vars[938] = 1
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	return SKIP_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[938] != 1):
		if (not game.combat_is_active()):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_better_to_talk(attachee,obj)):
					attachee.turn_towards(obj)
					obj.begin_dialog( attachee, 1 )
					game.new_sid = 0
	return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	if (attachee.map == 5163):
		game.leader.begin_dialog( attachee, 340 )
	elif (attachee.map != 5184 and attachee.map != 5163):
		triggerer.follower_remove(attachee)
		attachee.object_flag_set(OF_OFF)
	return SKIP_DEFAULT


def new_orrengaard( attachee ):
	game.global_vars[938] = 2
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 10):
			return 1
	return 0


