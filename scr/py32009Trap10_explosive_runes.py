from toee import *
from Co8 import D20CO8_F_POISON

def san_trap( trap, triggerer ):
	# numP = 210 / (game.party_npc_size() + game.party_pc_size())
	# for obj in game.obj_list_vicinity( triggerer.location, OLC_CRITTERS ):
		# obj.stat_base_set(stat_experience, (obj.stat_level_get(stat_experience) - numP))
	game.particles( trap.partsys, trap.obj )
	game.sound(4024,1)
	for obj in game.obj_list_vicinity( triggerer.location, OLC_CRITTERS ):
		if (obj.distance_to(trap.obj) <= 10):
			if (obj.has_los(trap.obj)):
				for dmg in trap.damage:
					if (dmg.type == D20DT_POISON):
						if (obj.saving_throw( 15, D20_Save_Fortitude, D20CO8_F_POISON, trap.obj ) == 0):
							obj.condition_add_with_args("Poisoned",dmg.damage.bonus,0)
					else if (obj == triggerer):
						obj.damage( trap.obj, dmg.type, dmg.damage )
					else:
						obj.reflex_save_and_damage( trap.obj, 15, D20_Save_Reduction_Half, D20STD_F_SPELL_DESCRIPTOR_FORCE, dmg.damage, dmg.type, D20DAP_NORMAL )

	game.new_sid = 0
	return SKIP_DEFAULT
