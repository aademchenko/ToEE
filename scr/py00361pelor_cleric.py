from utilities import *
from toee import *
from InventoryRespawn import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.has_met(triggerer)):
		triggerer.begin_dialog(attachee,10)
	else:
		triggerer.begin_dialog(attachee,1)
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5093 and game.global_vars[960] == 3):
		attachee.object_flag_unset(OF_OFF)
		attachee.cast_spell(spell_shield_of_faith, attachee)
	elif (attachee.map == 5156 and game.global_vars[704] == 3 and is_daytime() == 1 and game.quests[76].state != qs_accepted):
		attachee.object_flag_unset(OF_OFF)
		attachee.cast_spell(spell_spell_resistance, attachee)
	elif (attachee.map == 5137 and game.global_flags[922] == 0):
		game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
		game.global_flags[922] = 1
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	for pc in game.party:
		pc.condition_add('fallen_paladin')
	if (attachee.map == 5093):
		ditch_rings( attachee, triggerer )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	if (game.global_vars[956] == 1):
		attachee.obj_set_int(obj_f_critter_strategy, 411)
	return RUN_DEFAULT


def respawn(attachee):
	box = find_container_near(attachee,1001)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
	return


def ditch_rings( attachee, triggerer ):
	acid_major = attachee.item_find(12635)
	cold_major = attachee.item_find(12634)
	electricity_major = attachee.item_find(12632)
	fire_major = attachee.item_find(12631)
	sonic_major = attachee.item_find(12633)
	acid_major.destroy()
	cold_major.destroy()
	electricity_major.destroy()
	fire_major.destroy()
	sonic_major.destroy()
	return