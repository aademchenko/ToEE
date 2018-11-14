from utilities import *
from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5093 and game.global_vars[960] == 3):
		attachee.object_flag_unset(OF_OFF)
		game.timevent_add( go_boom, ( attachee, triggerer ), 3000 )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (attachee.map == 5093):
			if (is_cool_to_talk(attachee, game.party[0])):
				if (game.global_vars[960] == 3):
					game.party[0].turn_towards(attachee)
					game.party[0].begin_dialog(attachee,1)
					game.global_vars[960] = 4
	return RUN_DEFAULT


def is_cool_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 20):
		return 1
	return 0


def run_off_gang( attachee, triggerer ):
	game.sound( 4031, 1 )
	game.particles( "sp-Invisibility", attachee )
	attachee.object_flag_set(OF_OFF)
	sb = find_npc_near(attachee,14720)
	game.particles( "sp-Invisibility", sb )
	sb.object_flag_set(OF_OFF)
	sb = find_npc_near(attachee,14720)
	game.particles( "sp-Invisibility", sb )
	sb.object_flag_set(OF_OFF)
	sb = find_npc_near(attachee,14720)
	game.particles( "sp-Invisibility", sb )
	sb.object_flag_set(OF_OFF)
	sb = find_npc_near(attachee,14720)
	game.particles( "sp-Invisibility", sb )
	sb.object_flag_set(OF_OFF)
	sb = find_npc_near(attachee,14720)
	game.particles( "sp-Invisibility", sb )
	sb.object_flag_set(OF_OFF)
	sb = find_npc_near(attachee,14720)
	game.particles( "sp-Invisibility", sb )
	sb.object_flag_set(OF_OFF)
	sb = find_npc_near(attachee,14720)
	game.particles( "sp-Invisibility", sb )
	sb.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def go_boom( attachee, triggerer ):
	game.particles( "sp-Fireball-Hit", location_from_axis( 484, 468 ) )
	game.particles( "ef-fire-lazy", location_from_axis( 484, 468 ) )
	game.particles( "ef-Embers Small", location_from_axis( 484, 468 ) )
	game.particles( "sp-Fireball-Hit", location_from_axis( 468, 452 ) )
	game.particles( "ef-fire-lazy", location_from_axis( 468, 452 ) )
	game.particles( "ef-Embers Small", location_from_axis( 468, 452 ) )
	game.particles( "ef-fire-lazy", location_from_axis( 468, 485 ) )
	game.particles( "ef-Embers Small", location_from_axis( 468, 485 ) )
	game.particles( "ef-fire-lazy", location_from_axis( 468, 464 ) )
	game.particles( "ef-Embers Small", location_from_axis( 468, 464 ) )
	game.sound( 4111, 1 )
	return RUN_DEFAULT