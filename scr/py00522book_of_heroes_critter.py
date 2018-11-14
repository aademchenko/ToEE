from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.map == 5119):
		triggerer.begin_dialog( attachee, 60 )
	elif (game.global_vars[994] != 0):
		if (game.quests[65].state != qs_completed):
			triggerer.begin_dialog( attachee, 40 )
		else:
			triggerer.begin_dialog ( attachee, 50)
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT