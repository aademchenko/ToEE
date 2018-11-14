from toee import *
from utilities import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.name == 8857):
		if (game.global_vars[558] == 1):
			attachee.object_flag_unset(OF_OFF)
	elif (attachee.name == 8858):
		if (game.global_vars[558] == 2):
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.name == 8857):
		if (game.global_vars[558] == 1):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (sight_distance(attachee, obj)):
						game.timevent_add( run_out, ( attachee, obj ), 1000 )
						game.global_vars[558] = 4
	elif (attachee.name == 8858):
		if (game.global_vars[558] == 2):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (sight_distance(attachee, obj)):
						game.timevent_add( drop_out, ( attachee, obj ), 1000 )
						game.global_vars[558] = 4


def san_start_combat( attachee, triggerer ):
	if (attachee.name == 8857):
		attachee.object_flag_set(OF_OFF)
		game.sound( 4163, 1 )
		game.sound( 4161, 1 )
		game.particles( 'ef-splash', attachee )
		game.particles( 'ef-ripples-huge', attachee )
	elif (attachee.name == 8858):
		attachee.object_flag_set(OF_OFF)
		game.sound( 4164, 1 )
		game.sound( 4161, 1 )
		game.particles( 'ef-splash', attachee )
		game.particles( 'ef-ripples-huge', attachee )
	return RUN_DEFAULT


def sight_distance(speaker,listener):
	if (speaker.distance_to(listener) <= 50):
		return 1
	return 0


def run_out( attachee, triggerer ):
	attachee.object_flag_set(OF_OFF)
	game.sound( 4164, 1 )
	game.sound( 4161, 1 )
	game.sound( 4163, 1 )
	game.particles( "ef-splash", attachee )
	game.particles( "ef-MinoCloud", attachee )
	return RUN_DEFAULT


def drop_out( attachee, triggerer ):
	attachee.object_flag_set(OF_OFF)
	game.sound( 4164, 1 )
	game.sound( 4161, 1 )
	game.sound( 4163, 1 )
	game.particles( "ef-splash", attachee )
	game.particles( "ef-MinoCloud", attachee )
	return RUN_DEFAULT