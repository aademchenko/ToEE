from utilities import *
from toee import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	attachee.cast_spell(spell_shield_of_faith, attachee)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	attachee.cast_spell(spell_shield_of_faith, attachee)
	return RUN_DEFAULT