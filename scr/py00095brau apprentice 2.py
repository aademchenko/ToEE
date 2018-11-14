from toee import *
from utilities import find_npc_near
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.leader.reputation_has(32) == 1 or game.leader.reputation_has(30) == 1 or game.leader.reputation_has(29) == 1):
		attachee.float_line(11004,triggerer)
	else:
		if (attachee.map == 5007):
			if (game.quests[19].state == qs_unknown):
				triggerer.begin_dialog( attachee, 1 )
			elif (game.quests[19].state == qs_mentioned):
				triggerer.begin_dialog( attachee, 40 )
			elif (game.quests[19].state == qs_accepted or game.quests[19].state == qs_botched):
				triggerer.begin_dialog( attachee, 50 )
			else:
				triggerer.begin_dialog( attachee, 60 )
		else:
			triggerer.begin_dialog( attachee, 90 )
	return SKIP_DEFAULT


def find_ostler( attachee, triggerer):
	npc = find_npc_near(attachee,8008)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,230)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,80)
	return SKIP_DEFAULT
