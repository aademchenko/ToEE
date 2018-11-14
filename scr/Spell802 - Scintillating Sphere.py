from toee import *

def OnBeginSpellCast( spell ):
	print "Scintillating Sphere OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Scintillating Sphere OnSpellEffect"

	game.particles( 'sp-evocation-conjure', spell.caster )

def OnBeginRound( spell ):
	print "Scintillating Sphere OnBeginRound"

def OnBeginProjectile( spell, projectile, index_of_target ):
	print "Scintillating Sphere OnBeginProjectile"

	#spell.proj_partsys_id = game.particles( 'sp-Scintillating Sphere-proj', projectile )
	projectile.obj_set_int( obj_f_projectile_part_sys_id, game.particles( 'sp-Scintillating Sphere-proj', projectile ) )

def OnEndProjectile( spell, projectile, index_of_target ):
	print "Scintillating Sphere OnEndProjectile"

	remove_list = []

	spell.duration = 0
	dam = dice_new( '1d6' )
	dam.number = min( 10, spell.caster_level )

	game.particles_end( projectile.obj_get_int( obj_f_projectile_part_sys_id ) )
	game.particles( 'sp-Scintillating Sphere-Hit', spell.target_loc )

	for target_item in spell.target_list:

		if target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_ELECTRICITY, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ):
			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
		else:
			# saving throw unsuccessful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

		remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnEndSpellCast( spell ):
	print "Scintillating Sphere OnEndSpellCast"