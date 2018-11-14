from toee import *
from combat_standard_routines import *


def san_heartbeat( attachee, triggerer ):
	if (attachee.name == 14416):
		# Minotaur controller.
		for obj in game.obj_list_vicinity(attachee.location,OLC_CRITTERS):
			if (obj != attachee):
				if (attachee.distance_to(obj) <= 15):
					for statue in game.obj_list_vicinity( obj.location, OLC_SCENERY ):
						if (statue.name == 1615):
							loc = statue.location
							rot = statue.rotation
							statue.destroy()
							minotaur = game.obj_create( 14241, loc )
							minotaur.rotation = rot
							game.particles( "ef-MinoCloud", minotaur )
							attachee.destroy()
							return SKIP_DEFAULT
		return SKIP_DEFAULT

	elif (attachee.name == 14241):
		# Minotaur.
		print "Minotaur heartbeat, casting stoneskin."
		attachee.cast_spell(spell_stoneskin, attachee)
		game.new_sid = 0
		return SKIP_DEFAULT