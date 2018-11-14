from toee import *

def san_trap( trap, triggerer ):
	# numP = 210 / (game.party_npc_size() + game.party_pc_size())
	# for obj in game.obj_list_vicinity( triggerer.location, OLC_CRITTERS ):
		# obj.stat_base_set(stat_experience, (obj.stat_level_get(stat_experience) - numP))
	game.particles( trap.partsys, trap.obj )
	game.sound(4021,1)
	for obj in game.obj_list_vicinity( triggerer.location, OLC_CRITTERS ):
		obj.condition_add_with_args("Poisoned",5,0)
	game.new_sid = 0
	return SKIP_DEFAULT
