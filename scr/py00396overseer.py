from utilities import *
from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	ditch_belts( attachee, triggerer )
	return RUN_DEFAULT


def ditch_belts( attachee, triggerer ):
	belt = attachee.item_find(6243)
	beld = attachee.item_find(6244)
	circ = attachee.item_find(6335)
	ring = attachee.item_find(6083)
	circ.destroy()
	belt.destroy()
	beld.destroy()
	ring.destroy()
	return