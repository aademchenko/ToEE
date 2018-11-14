from toee import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT

def make_like( attachee, triggerer ):
	if ( attachee.reaction_get( triggerer ) <= 71 ):
		attachee.reaction_set( triggerer, 71 )
	return SKIP_DEFAULT
