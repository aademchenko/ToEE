from utilities import *
from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5093 and game.global_vars[960] == 3):
		attachee.object_flag_unset(OF_OFF)
		attachee.cast_spell(spell_death_ward, attachee)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	game.global_flags[844] = 1
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	if (game.global_vars[956] == 1):
		attachee.obj_set_int(obj_f_critter_strategy, 409)
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[844] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		if ( (attachee.map == 5093) and (game.global_vars[960] == 4) ):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_better_to_talk(attachee, obj)):
					attachee.turn_towards(obj)
					obj.begin_dialog( attachee, 1 )
					game.global_vars[960] = 5
	elif (game.combat_is_active()):
		if ( (attachee.map == 5093) and (game.global_vars[957] >= 8) ):
			attachee.float_line(1000,triggerer)
			game.global_vars[956] = 1
			game.global_vars[957] = 0
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 60):
		return 1
	return 0