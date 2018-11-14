from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if ((game.global_flags[5] == true) or (game.global_flags[7] == true)):
		triggerer.begin_dialog( attachee, 120 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT

def make_hate( attachee, triggerer ):
	if ( attachee.reaction_get( triggerer ) >= 20 ):
		attachee.reaction_set( triggerer, 20 )
	return SKIP_DEFAULT

def make_worry( attachee, triggerer ):
	if ( attachee.reaction_get( triggerer ) >= 40 ):
		attachee.reaction_set( triggerer, 40 )
	return SKIP_DEFAULT