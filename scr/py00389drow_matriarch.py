from utilities import *
from toee import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	if (game.party_alignment == LAWFUL_GOOD or game.party_alignment == NEUTRAL_GOOD or game.party_alignment == CHAOTIC_GOOD):
		attachee.cast_spell(spell_magic_circle_against_good, attachee)
	else:
		attachee.cast_spell(spell_divine_power, attachee)
	return RUN_DEFAULT