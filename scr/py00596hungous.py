from toee import *
from utilities import *
from scripts import *
from Co8 import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(1000,triggerer)
	game.global_vars[986] = 3
	game.global_flags[560] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	return SKIP_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.map == 5115):
		if (not game.combat_is_active()):
			if (game.global_vars[570] == 1):
				attachee.unconceal()
				attachee.standpoint_set( STANDPOINT_NIGHT, 738 )
				attachee.standpoint_set( STANDPOINT_DAY, 738 )
				game.global_vars[570] = 2
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (is_better_to_talk(attachee, obj)):
						game.timevent_add( start_talking, ( attachee, triggerer ), 4000 )
						game.global_vars[570] = 3
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 40):
			return 1
	return 0


def start_talking( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 1 )
	return RUN_DEFAULT


def increment_rep( attachee, triggerer ):
	if (game.party[0].reputation_has(81) == 1):
		game.party[0].reputation_add(82)
		game.party[0].reputation_remove(81)
	elif (game.party[0].reputation_has(82) == 1):
		game.party[0].reputation_add(83)
		game.party[0].reputation_remove(82)
	elif (game.party[0].reputation_has(83) == 1):
		game.party[0].reputation_add(84)
		game.party[0].reputation_remove(83)
	elif (game.party[0].reputation_has(84) == 1):
		game.party[0].reputation_add(85)
		game.party[0].reputation_remove(84)
	elif (game.party[0].reputation_has(85) == 1):
		game.party[0].reputation_add(86)
		game.party[0].reputation_remove(85)
	elif (game.party[0].reputation_has(86) == 1):
		game.party[0].reputation_add(87)
		game.party[0].reputation_remove(86)
	elif (game.party[0].reputation_has(87) == 1):
		game.party[0].reputation_add(88)
		game.party[0].reputation_remove(87)
	elif (game.party[0].reputation_has(88) == 1):
		game.party[0].reputation_add(89)
		game.party[0].reputation_remove(88)
	else:
		game.party[0].reputation_add(81)
	return RUN_DEFAULT


def buff_1( attachee, triggerer ):
	witch = find_npc_near( attachee, 8627 )
	witch.cast_spell(spell_greater_heroism, attachee)
	return


def buff_2( attachee, triggerer ):
	witch = find_npc_near( attachee, 8627 )
	krunch = find_npc_near( attachee, 8802 )
	witch.cast_spell(spell_greater_heroism, krunch)
	return


def buff_3( attachee, triggerer ):
	warlock = find_npc_near( attachee, 8626 )
	warlock.cast_spell(spell_protection_from_good, attachee)
	return


def buff_4( attachee, triggerer ):
	warlock = find_npc_near( attachee, 8626 )
	krunch = find_npc_near( attachee, 8802 )
	warlock.cast_spell(spell_protection_from_good, krunch)
	return