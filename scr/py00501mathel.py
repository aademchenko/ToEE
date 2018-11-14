from toee import *
from utilities import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.has_met(triggerer)):
		triggerer.turn_towards(attachee)
		triggerer.begin_dialog( attachee, 30 )	
	else:
		triggerer.turn_towards(attachee)
		triggerer.begin_dialog( attachee, 1 )	
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[976] = 1
	attachee.object_flag_set(OF_OFF)
	game.particles( "ef-MinoCloud", attachee )
	game.particles( "Brasier", attachee )
	game.sound( 4038, 1 )
	cloak = attachee.item_find( 6427 )
	cloak.object_flag_set(OF_OFF)
	armor = attachee.item_find( 6475 )
	armor.object_flag_set(OF_OFF)
	boots = attachee.item_find( 6045 )
	boots.object_flag_set(OF_OFF)
	gloves = attachee.item_find( 6046 )
	gloves.object_flag_set(OF_OFF)
	helm = attachee.item_find( 6209 )
	helm.object_flag_set(OF_OFF)
	ring = attachee.item_find( 6083 )
	ring.object_flag_set(OF_OFF)
	weapon = attachee.item_find( 4185 )
	weapon.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (is_better_to_talk(attachee, game.party[0])):
			attachee.turn_towards(game.party[0])
			game.party[0].begin_dialog( attachee, 1 )
			game.new_sid = 0
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 30):
			return 1
	return 0


def run_off( attachee, triggerer ):
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT