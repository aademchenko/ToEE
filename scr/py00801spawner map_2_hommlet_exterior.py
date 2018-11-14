from utilities import *
from toee import *
from combat_standard_routines import *


def san_heartbeat( attachee, triggerer ):
	if (attachee.map == 5001):
		if (game.random_range(1,3) == 1):
			barrel = game.obj_create( 1049, location_from_axis (641L, 387L) )
			if (game.random_range(1,3) <= 2):
				create_item_in_inventory( 5007, barrel )
		if (game.random_range(1,3) == 1):
			barrel = game.obj_create( 1049, location_from_axis (714L, 381L) )
			if (game.random_range(1,3) <= 2):
				create_item_in_inventory( 5007, barrel )
		if (game.random_range(1,3) == 1):
			barrel = game.obj_create( 1049, location_from_axis (573L, 424L) )
			if (game.random_range(1,3) <= 2):
				create_item_in_inventory( 5007, barrel )
		if (game.random_range(1,3) == 1):
			barrel = game.obj_create( 1049, location_from_axis (617L, 460L) )
			if (game.random_range(1,3) <= 2):
				create_item_in_inventory( 5007, barrel )
		if (game.random_range(1,3) == 1):
			barrel = game.obj_create( 1049, location_from_axis (592L, 485L) )
			if (game.random_range(1,3) <= 2):
				create_item_in_inventory( 5007, barrel )
		if (game.random_range(1,3) == 1):
			barrel = game.obj_create( 1049, location_from_axis (454L, 442L) )
			if (game.random_range(1,3) <= 2):
				create_item_in_inventory( 5007, barrel )
		if (game.random_range(1,3) == 1):
			barrel = game.obj_create( 1049, location_from_axis (472L, 313L) )
			if (game.random_range(1,3) <= 2):
				create_item_in_inventory( 5007, barrel )
		if (game.random_range(1,3) == 1):
			barrel = game.obj_create( 1049, location_from_axis (418L, 378L) )
			if (game.random_range(1,3) <= 2):
				create_item_in_inventory( 5007, barrel )
		if (game.random_range(1,3) == 1):
			barrel = game.obj_create( 1049, location_from_axis (364L, 406L) )
			if (game.random_range(1,3) <= 2):
				create_item_in_inventory( 5007, barrel )
		game.global_vars[766] = game.random_range(1,20)
		attachee.destroy()
	return RUN_DEFAULT

