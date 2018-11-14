from toee import *
from utilities import *
from Co8 import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_start_combat( attachee, triggerer ):
	leader = game.party[0]
	StopCombat(attachee, 0)
	leader.begin_dialog( attachee, 4000 )
	return RUN_DEFAULT