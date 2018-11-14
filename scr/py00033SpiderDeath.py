from toee import *
from utilities import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if (attachee.map == 5069):
		game.global_vars[3] = game.global_vars[3] + 1
		if (game.party_alignment == LAWFUL_NEUTRAL or game.party_alignment == CHAOTIC_NEUTRAL or game.party_alignment == TRUE_NEUTRAL or game.party_alignment == LAWFUL_EVIL or game.party_alignment == CHAOTIC_EVIL or game.party_alignment == NEUTRAL_EVIL):
			ring = attachee.item_find( 3000 )
			ring.destroy()
	elif (attachee.map == 5002):
		if (game.party_alignment == LAWFUL_GOOD or game.party_alignment == CHAOTIC_GOOD or game.party_alignment == NEUTRAL_GOOD or game.party_alignment == LAWFUL_EVIL or game.party_alignment == CHAOTIC_EVIL or game.party_alignment == NEUTRAL_EVIL):
			ring = attachee.item_find( 3000 )
			ring.destroy()
	elif (attachee.map == 5003):
		if (game.party_alignment == LAWFUL_GOOD or game.party_alignment == CHAOTIC_GOOD or game.party_alignment == NEUTRAL_GOOD or game.party_alignment == LAWFUL_NEUTRAL or game.party_alignment == CHAOTIC_NEUTRAL or game.party_alignment == TRUE_NEUTRAL):
			ring = attachee.item_find( 3000 )
			ring.destroy()
	return RUN_DEFAULT
