from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.critter_flag_unset(OCF_MUTE)
	if (game.global_flags[105] == 1):
		attachee.attack(triggerer)
	elif (find_npc_near(attachee,8027) == OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 1 )
	elif (game.quests[46].state == qs_unknown):
		triggerer.begin_dialog( attachee, 20 )
	else:
		triggerer.begin_dialog( attachee, 40 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	for statue in game.obj_list_vicinity( attachee.location, OLC_SCENERY ):
		if (statue.name == 1618):
			loc = statue.location
	spell_obj = game.obj_create( OBJECT_SPELL_GENERIC, loc )
	game.particles( 'sp-Fog Cloud', spell_obj )
	loc = location_from_axis( 543, 539 )
	spell_obj = game.obj_create( OBJECT_SPELL_GENERIC, loc )
	game.particles( 'sp-Fog Cloud', spell_obj )
	loc = location_from_axis( 528, 538 )
	spell_obj = game.obj_create( OBJECT_SPELL_GENERIC, loc )
	game.particles( 'sp-Fog Cloud', spell_obj )
	game.new_sid = 0
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[132] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[132] = 0
	return RUN_DEFAULT


def san_will_kos( attachee, triggerer ):
	if (game.global_flags[105] == 0):
		return SKIP_DEFAULT
	else:
		return RUN_DEFAULT


def switch_dialog( attachee, triggerer, line):
	npc = find_npc_near(attachee,8027)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,1)
	return SKIP_DEFAULT