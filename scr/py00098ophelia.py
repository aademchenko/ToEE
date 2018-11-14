from toee import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (not attachee.has_met(triggerer)):
		if (game.quests[35].state <= qs_accepted):
####		if (game.quests[34].state <= qs_accepted):
			triggerer.begin_dialog( attachee, 1 )
		else:
			triggerer.begin_dialog( attachee, 430 )
	elif (game.global_flags[75] == 1):
		triggerer.begin_dialog( attachee, 580 )
	elif (game.quests[35].state == qs_completed):
###	elif (game.quests[34].state == qs_completed):
		triggerer.begin_dialog( attachee, 790 )
	else:
		triggerer.begin_dialog( attachee, 700 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[961] == 5):
		if (not game.combat_is_active()):
			if (is_better_to_talk(attachee, game.party[0])):
				game.global_vars[961] = 6
				attachee.turn_towards(game.party[0])
				game.party[0].begin_dialog(attachee,420)
	return RUN_DEFAULT


def buttin( attachee, triggerer, line):
	npc = find_npc_near(attachee,8015)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,760)
	return SKIP_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 15):
		return 1
	return 0