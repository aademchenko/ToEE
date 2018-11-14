from toee import *
from combat_standard_routines import *


def san_enter_combat( attachee, triggerer ):
	for statue in game.obj_list_vicinity( attachee.location, OLC_SCENERY ):
		if (statue.name == 1618):
			loc = statue.location
			rot = statue.rotation
			statue.destroy()
			juggernaut = game.obj_create( 14426, loc )
			juggernaut.rotation = rot
			game.particles( "ef-MinoCloud", juggernaut )
			attachee.destroy()
			return SKIP_DEFAULT
	return SKIP_DEFAULT
