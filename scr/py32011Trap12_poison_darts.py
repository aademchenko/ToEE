from toee import *
from Co8 import D20CO8_F_POISON

def san_trap( trap, triggerer ):
	# numP = 210 / (game.party_npc_size() + game.party_pc_size())
	# for obj in game.obj_list_vicinity( triggerer.location, OLC_CRITTERS ):
		# obj.stat_base_set(stat_experience, (obj.stat_level_get(stat_experience) - numP))
	game.particles( trap.partsys, trap.obj )
	game.sound(4023,1)
	for obj in game.obj_list_vicinity( triggerer.location, OLC_CRITTERS ):
		if (obj.distance_to(trap.obj) <= 10):
			if (obj.has_los(trap.obj)):
				result = trap.attack( triggerer, 15, 20, 1 )
				if (result & D20CAF_HIT):
					for dmg in trap.damage:
						if (dmg.type == D20DT_POISON):
							if (obj.saving_throw( 11, D20_Save_Fortitude, D20CO8_F_POISON, trap.obj ) == 0):
								obj.condition_add_with_args("Poisoned",dmg.damage.bonus,0)
						else:
							d = dmg.damage.clone()
							if (result & D20CAF_CRITICAL):
								d.n = d.n * 2
								d.bonus = d.bonus * 2
							obj.damage( trap.obj, dmg.type, d )
	game.new_sid = 0
	return SKIP_DEFAULT
