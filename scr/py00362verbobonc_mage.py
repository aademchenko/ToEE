from utilities import *
from toee import *
from Co8 import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	return RUN_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5093 and game.global_vars[960] == 3):
		attachee.object_flag_unset(OF_OFF)
		attachee.cast_spell(spell_shield, attachee)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	if (attachee.map == 5093):
		ditch_rings( attachee, triggerer )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	if (game.global_vars[704] == 8):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			StopCombat(attachee, 0)
			wilfrick = find_npc_near(attachee,8703)
			attachee.turn_towards(wilfrick)
			obj.begin_dialog( attachee, 1 )
			game.global_vars[704] = 9
			return RUN_DEFAULT
	return RUN_DEFAULT


def ass_out( attachee, triggerer ):
	wilfrick = find_npc_near(attachee,8703)
	game.particles( "sp-Teleport", attachee )
	game.particles( "sp-Teleport", wilfrick )
	game.sound( 4035, 1 )
	attachee.object_flag_set(OF_OFF)
	wilfrick.object_flag_set(OF_OFF)
	game.party[0].reputation_add( 42 )
	resume_fighting( attachee, triggerer )
	return RUN_DEFAULT


def resume_fighting( attachee, triggerer ):
	samson = find_npc_near(attachee, 8724)
	goliath = find_npc_near(attachee, 8725)
	bathsheba = find_npc_near(attachee, 8726)
	mage = find_npc_near(attachee, 14658)
	priest = find_npc_near(attachee, 14471)
	guard1 = find_npc_near(attachee, 14716)
	guard2 = find_npc_near(attachee, 14719)
	samson.attack(triggerer)
	goliath.attack(triggerer)
	bathsheba.attack(triggerer)
	mage.attack(triggerer)
	priest.attack(triggerer)
	guard1.attack(triggerer)
	guard2.attack(triggerer)
	return