from toee import *
from utilities import find_npc_near
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.leader.reputation_has(32) == 1 or game.leader.reputation_has(30) == 1 or game.leader.reputation_has(29) == 1):
		attachee.float_line(11002,triggerer)
	else:
		if (triggerer.stat_level_get(stat_charisma) >= 8 and triggerer.stat_level_get( stat_gender ) == gender_female):
			if (attachee.has_met(triggerer)):
				triggerer.begin_dialog( attachee, 70 )
			else:
				triggerer.begin_dialog( attachee, 1 )
		else:
			triggerer.begin_dialog( attachee, 80 )
	return SKIP_DEFAULT

def argue( attachee, triggerer, line):
	npc = find_npc_near(attachee,8006)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,10)
	return SKIP_DEFAULT
