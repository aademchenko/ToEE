from toee import *
from utilities import *
from scripts import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	attachee.condition_add_with_args( 'sp-Animate Dead', 127, 10, 3 )
	game.particles( "sp-summon monster I", game.party[0] )
	return RUN_DEFAULT

def san_start_combat( attachee, triggerer ):
	return RUN_DEFAULT

def san_unlock_attempt( attachee, triggerer ):
	game.timeevent_add( get_rid_of_it, ( attachee ), 20000 )
	return RUN_DEFAULT

def san_remove_item( attachee, triggerer ):
	game.timeevent_add( get_rid_of_it, ( attachee ), 20000 )
	return RUN_DEFAULT

def get_rid_of_it(attachee):
	attachee.destroy()
	# game.particles( "sp-summon monster I", game.party[0] )
	return