from toee import *
from utilities import *
from py00439script_daemon import within_rect_by_corners
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[568] == 1):
		game.global_vars[569] = game.global_vars[569] + 1
		if (game.global_vars[569] == 4):
			game.sound( 4180, 1 )
		elif (game.global_vars[569] == 7):
			spawn_hydra( attachee, triggerer )
		elif (game.global_vars[569] == 10):
			spawn_others( attachee, triggerer )
			game.global_vars[569] = 0
	for obj in game.obj_list_vicinity( attachee.location, OLC_CRITTERS ):
		if (within_rect_by_corners(obj, 538, 394, 531, 408)):
			attachee.object_flag_unset(OF_OFF)
			obj.condition_add_with_args("Prone",1,0)
			game.particles( "ef-splash", obj )
			game.sound( 4177, 1 )
			game.timevent_add( relocate_west, ( attachee, obj ), 300 )
			obj.begin_dialog( attachee, 1 )
		if (within_rect_by_corners(obj, 487, 398, 481, 412)):
			attachee.object_flag_unset(OF_OFF)
			obj.condition_add_with_args("Prone",1,0)
			game.particles( "ef-splash", obj )
			game.sound( 4177, 1 )
			game.timevent_add( relocate_east, ( attachee, obj ), 300 )
			obj.begin_dialog( attachee, 1 )
	return RUN_DEFAULT


def spawn_hydra( attachee, triggerer ):
	hydra = game.obj_create( 14982, location_from_axis (511L, 423L) )
	hydra.move(location_from_axis (511L, 424L))
	hydra.rotation = 5.49778714378
	hydra.concealed_set(1)
	hydra.unconceal()
	hydra.npc_flag_unset(ONF_KOS)
	game.particles( "Mon-YellowMold-60", hydra )
	game.sound( 4179, 1 )
	return


def spawn_others( attachee, triggerer ):
	picker1 = game.random_range(14978,14981)
	animal1 = game.obj_create( picker1, location_from_axis (511L, 423L) )
	animal1.move(location_from_axis (515L, 424L))
	animal1.rotation = 5.39778714378
	animal1.concealed_set(1)
	animal1.unconceal()
	game.particles( "Mon-YellowMold-20", animal1 )
	picker2 = game.random_range(14978,14981)
	animal2 = game.obj_create( picker2, location_from_axis (511L, 423L) )
	animal2.move(location_from_axis (507L, 424L))
	animal2.rotation = 5.59778714378
	animal2.concealed_set(1)
	animal2.unconceal()
	game.particles( "Mon-YellowMold-30", animal2 )
	picker3 = game.random_range(14978,14981)
	animal3 = game.obj_create( picker3, location_from_axis (511L, 423L) )
	animal3.move(location_from_axis (519L, 424L))
	animal3.rotation = 5.29778714378
	animal3.concealed_set(1)
	animal3.unconceal()
	game.particles( "Mon-YellowMold-40", animal3 )
	picker4 = game.random_range(14978,14981)
	animal4 = game.obj_create( picker4, location_from_axis (511L, 423L) )
	animal4.move(location_from_axis (503L, 424L))
	animal4.rotation = 5.69778714378
	animal4.concealed_set(1)
	animal4.unconceal()
	game.particles( "Mon-YellowMold-60", animal4 )
	picker5 = game.random_range(14978,14981)
	animal5 = game.obj_create( picker5, location_from_axis (511L, 423L) )
	animal5.move(location_from_axis (523L, 424L))
	animal5.rotation = 5.19778714378
	animal5.concealed_set(1)
	animal5.unconceal()
	game.particles( "Mon-YellowMold-30", animal5 )
	picker6 = game.random_range(14978,14981)
	animal6 = game.obj_create( picker6, location_from_axis (511L, 423L) )
	animal6.move(location_from_axis (499L, 424L))
	animal6.rotation = 5.79778714378
	animal6.concealed_set(1)
	animal6.unconceal()
	game.particles( "Mon-YellowMold-20", animal6 )
	game.sound( 4181, 1 )
	game.global_vars[568] = 9
	return


def relocate_west( attachee, obj ):
	attachee.object_flag_set(OF_OFF)
	coord_x = game.random_range(522,526)
	coord_y = game.random_range(405,409)
	obj.move(location_from_axis (coord_x, coord_y))
	game.particles( "Mon-Phycomid-10", obj )
	game.sound( 4186, 1 )
	obj.float_mesfile_line( 'mes\\float.mes', 2 )
	game.global_flags[557] = 1
	if (game.global_vars[568] == 0):
		game.global_vars[568] = 1
	return


def relocate_east( attachee, obj ):
	attachee.object_flag_set(OF_OFF)
	coord_x = game.random_range(499,503)
	coord_y = game.random_range(405,409)
	obj.move(location_from_axis (coord_x, coord_y))
	game.particles( "Mon-Phycomid-10", obj )
	game.sound( 4186, 1 )
	obj.float_mesfile_line( 'mes\\float.mes', 2 )
	game.global_flags[557] = 1
	if (game.global_vars[568] == 0):
		game.global_vars[568] = 1
	return