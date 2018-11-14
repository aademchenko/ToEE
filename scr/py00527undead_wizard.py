from toee import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_vars[987] = game.global_vars[987] + 1
	if game.global_vars[987] == 1:
		spawn_undead_backup( attachee, triggerer )
	elif game.global_vars[987] == 3:
		game.global_flags[945] = 1
		game.global_vars[994] = 4
	return RUN_DEFAULT


def spawn_undead_backup( attachee, triggerer ):
	game.sound( 4045, 1 )
	ga1 = game.obj_create(14135, location_from_axis(504, 458))
	ga1.rotation = 2.5
	ga1.concealed_set(1)
	ga1.unconceal()
	ga2 = game.obj_create(14135, location_from_axis(501, 458))
	ga2.rotation = 2.5
	ga2.concealed_set(1)
	ga2.unconceal()
	ga3 = game.obj_create(14135, location_from_axis(498, 458))
	ga3.rotation = 2.5
	ga3.concealed_set(1)
	ga3.unconceal()
	ga4 = game.obj_create(14135, location_from_axis(495, 458))
	ga4.rotation = 2.5
	ga4.concealed_set(1)
	ga4.unconceal()
	sh1 = game.obj_create(14596, location_from_axis(503, 455))
	sh1.rotation = 2.5
	sh1.concealed_set(1)
	sh1.unconceal()
	sh2 = game.obj_create(14596, location_from_axis(496, 455))
	sh2.rotation = 2.5
	sh2.concealed_set(1)
	sh2.unconceal()
	uw3 = game.obj_create(14597, location_from_axis(499, 455))
	uw3.rotation = 2.5
	uw3.concealed_set(1)
	uw3.unconceal()
	return RUN_DEFAULT