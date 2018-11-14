from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	return RUN_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[993] == 2):
		attachee.object_flag_unset(OF_OFF)
	elif (game.global_vars[993] == 3):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[952] = 1
	if (game.global_flags[948] == 1 and game.global_flags[949] == 1 and game.global_flags[950] == 1 and game.global_flags[951] == 1 and game.global_flags[953] == 1 and game.global_flags[954] == 1):
		game.party[0].reputation_add(40)
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[952] = 0
	game.party[0].reputation_remove(40)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[703] == 0):
		if (not game.combat_is_active()):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_better_to_talk(attachee, obj)):
					attachee.cast_spell(spell_prayer, attachee)
					game.global_vars[703] = 1
	elif (game.global_vars[703] == 2):
		if (not game.combat_is_active()):
			if (is_better_to_talk(attachee, game.party[0])):
				game.timevent_add( all_done, ( attachee, triggerer ), 5000 )
				game.global_vars[703] = 3
	return RUN_DEFAULT


def all_done( attachee, triggerer ):
	game.party[0].begin_dialog( attachee, 70 )
	return


def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 55):
		return 1
	return 0


def switch_to_tarah( attachee, triggerer, line):
	npc = find_npc_near(attachee,8805)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
	return SKIP_DEFAULT


def ward_tarah( attachee, triggerer ):
	tarah = find_npc_near(attachee,8805)
	attachee.cast_spell(spell_death_ward, tarah)
	game.timevent_add( ward_kenan, ( attachee, triggerer ), 5000 )
	return RUN_DEFAULT


def ward_kenan( attachee, triggerer ):
	kenan = find_npc_near(attachee,8804)
	attachee.cast_spell(spell_death_ward, kenan)
	game.timevent_add( ward_sharar, ( attachee, triggerer ), 5000 )
	return RUN_DEFAULT


def ward_sharar( attachee, triggerer ):
	sharar = find_npc_near(attachee,8806)
	attachee.cast_spell(spell_death_ward, sharar)
	game.timevent_add( ward_abaddon, ( attachee, triggerer ), 5000 )
	return RUN_DEFAULT


def ward_gadham( attachee, triggerer ):
	gadham = find_npc_near(attachee,8807)
	attachee.cast_spell(spell_death_ward, gadham)
	return RUN_DEFAULT


def ward_abaddon( attachee, triggerer ):
	attachee.cast_spell(spell_death_ward, attachee)
	game.global_vars[703] = 2
	return RUN_DEFAULT