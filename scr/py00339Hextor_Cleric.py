from toee import *
from utilities import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (game.global_vars[928] == 1):
		triggerer.begin_dialog( attachee, 300 )
	elif (attachee.has_met(triggerer)): 
		if (game.quests[78].state == qs_accepted and game.global_vars[929] == 0):
			triggerer.begin_dialog( attachee, 90 )
		else:
			triggerer.begin_dialog( attachee, 40 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5140):
		if (game.global_vars[949] == 2 or game.party[0].reputation_has(47) == 1):
			attachee.object_flag_set(OF_OFF)
		elif (game.global_flags[937] == 1):
			attachee.object_flag_unset(OF_OFF)
	elif (attachee.map == 5064):
		if (game.global_vars[949] == 1):
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if (attachee.name == 14654 and attachee.map == 5064):
		game.global_vars[949] = 2
	elif (attachee.name == 14717 and attachee.map == 5140):
		game.global_flags[973] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	if (attachee.name == 14717 and attachee.map == 5140):
		game.global_flags[973] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_better_to_talk(attachee, obj)):
				attachee.cast_spell(spell_death_ward, attachee)
				attachee.spells_pending_to_memorized()
				game.timevent_add( next_spell, ( attachee, triggerer ), 5000 )
				game.new_sid = 0
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 200):
		return 1
	return 0


def next_spell( attachee, triggerer ):
	attachee.cast_spell(spell_spell_resistance, attachee)
	attachee.spells_pending_to_memorized()
	return RUN_DEFAULT


def thaddeus_countdown( attachee, triggerer ):
	game.timevent_add( stop_watch, (), 172800000 )	## 2 days
	return RUN_DEFAULT


def stop_watch():
	game.global_vars[960] = 2
	return RUN_DEFAULT