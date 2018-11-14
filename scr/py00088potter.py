from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.global_flags[64] == 1):
		triggerer.begin_dialog( attachee, 130 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT

def make_hate( attachee, triggerer ):
	if ( attachee.reaction_get( triggerer ) >= 20 ):
		attachee.reaction_set( triggerer, 20 )
	return SKIP_DEFAULT