from toee import *

def OnBeginSpellCast( spell ):
	print "Ooze You Lose OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Ooze You Lose OnSpellEffect"

	game.particles( 'sp-Fireball-conjure', spell.caster )

def OnBeginRound( spell ):
	print "Ooze You Lose OnBeginRound"

def OnBeginProjectile( spell, projectile, index_of_target ):
	print "Spore No More OnBeginProjectile"

	projectile.obj_set_int( obj_f_projectile_part_sys_id, game.particles( 'sp-Melfs Acid Arrow Projectile', projectile ) )

def OnEndProjectile( spell, projectile, index_of_target ):
	print "Ooze You Lose OnEndProjectile"

	remove_list = []

	spell.duration = 0
	dam = dice_new( '1d6' )
	dam.number = 3

	npc = spell.caster
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL and npc.obj_get_int( obj_f_npc_pad_i_5) >= 1000:
		xyx = npc.obj_get_int( obj_f_npc_pad_i_5) - 1000
		loc = game.party[xyx].location

		game.particles_end( projectile.obj_get_int( obj_f_projectile_part_sys_id ) )
	
	else:
		game.particles_end( projectile.obj_get_int( obj_f_projectile_part_sys_id ) )

	for target_item in spell.target_list:	

		if target_item.obj.is_category_type( mc_type_ooze ) or target_item.obj.name == 14955:

			if (target_item.obj.distance_to(spell.target_list[0].obj) <= 10):
				dam.number = 3
				target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_NEGATIVE_ENERGY, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
				game.particles( 'sp-Blight', target_item.obj )
			else:
				dam.number = 2
				target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_NEGATIVE_ENERGY, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
				game.particles( 'sp-Blight', target_item.obj )

		else:

			dam.number = 1
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31015 )
			game.particles( 'Fizzle', target_item.obj )
			target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_ACID, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

		remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnEndSpellCast( spell ):
	print "Ooze You Lose OnEndSpellCast"