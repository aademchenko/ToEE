from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 200 )
	elif (attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 100 )
	elif (anyone(triggerer.group_list(),"has_wielded",3021)):
		triggerer.begin_dialog( attachee, 10 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_start_combat( attachee, triggerer ):
#	attachee.item_transfer_to(triggerer,4130)
	if ( obj_percent_hp(attachee) < 50):
		found_pc = OBJ_HANDLE_NULL
		for pc in game.party:
			if pc.type == obj_t_pc:
				found_pc = pc
				attachee.ai_shitlist_remove( pc )
				worg = find_npc_near(attachee,14352)
				worg.ai_shitlist_remove( pc )
		if found_pc != OBJ_HANDLE_NULL:
			if ( game.global_flags[194] == 0 ):
				game.global_flags[194] = 1
				found_pc.begin_dialog( attachee, 150 )
				game.new_sid = 0
				return SKIP_DEFAULT
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[182] = 1
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[182] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		leader = attachee.leader_get()
		if (leader != OBJ_HANDLE_NULL):
			if (obj_percent_hp(attachee) > 70):
				if (group_percent_hp(leader) < 30):
					attachee.float_line(510,leader)
					attachee.attack(leader)
		else:
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_okay_to_talk(attachee, obj)):
					if (attachee.has_met(obj)):
						obj.begin_dialog( attachee, 100 )
						game.new_sid = 0
					elif (anyone(obj.group_list(),"has_wielded",3021)):
						obj.begin_dialog( attachee, 10 )
						game.new_sid = 0
					else:
						obj.begin_dialog( attachee, 1 )
						game.new_sid = 0
	return RUN_DEFAULT


def is_okay_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 25):
			return 1
	return 0