from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if ( (anyone(triggerer.group_list(),"has_wielded",3017) ) or ( game.quests[52].state >= qs_mentioned ) ):
		if (not attachee.has_met(triggerer)):
			triggerer.begin_dialog( attachee, 30 )
		else:
			triggerer.begin_dialog( attachee, 50 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
		game.global_vars[718] = 0
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[139] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[139] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active() and game.global_flags[874] == 1):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			obj.begin_dialog( attachee, 60 )
	if (attachee.map == 5067 and game.global_flags[873] == 0):
		goaway = find_container_near( attachee, 1027 )
		rot = goaway.rotation
		loc = goaway.location
		goaway.destroy()
#		chest = game.obj_create( 1056, loc)
#		chest = game.obj_create( 1056, location_from_axis (434L, 585L))
#		chest = game.obj_create( 1056, location_from_axis (427L, 590L))
#		chest = game.obj_create( 1056, location_from_axis (436L, 586L))
##		chest = game.obj_create( 1056, location_from_axis (436L, 590L))
		chest = game.obj_create( 1056, location_from_axis (436L, 586L))
		chest.rotation = rot
		create_item_in_inventory( 8020, chest )
		create_item_in_inventory( 8020, chest )
		create_item_in_inventory( 6101, chest )
		create_item_in_inventory( 4136, chest )
		game.global_flags[873] = 1
	if (attachee.leader_get() == OBJ_HANDLE_NULL and game.global_vars[718] == 0 and not game.combat_is_active()):
		attachee.cast_spell(spell_protection_from_elements, attachee)
		attachee.spells_pending_to_memorized()
	game.global_vars[718] = game.global_vars[718] + 1
	if (not game.combat_is_active() and game.global_flags[853] == 0):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_safe_to_talk(attachee,obj)):
				if ( (anyone(obj.group_list(),"has_wielded",3017) ) or ( game.quests[52].state >= qs_mentioned ) ):
					if (not attachee.has_met(obj)):
						obj.begin_dialog( attachee, 30 )
					else:
						obj.begin_dialog( attachee, 50 )
				else:
					obj.begin_dialog( attachee, 1 )
				game.global_flags[853] = 1
#				game.new_sid = 0		#	removed by Livonya
	return RUN_DEFAULT