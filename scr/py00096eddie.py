from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.leader.reputation_has(32) == 1 or game.leader.reputation_has(30) == 1 or game.leader.reputation_has(29) == 1):
		attachee.float_line(11004,triggerer)
	else:
		if (game.global_vars[9] >= 2 and triggerer.stat_level_get( stat_gender ) == gender_female): 
			game.global_vars[9] = 2 + game.story_state
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT

