from toee import *

def OnBeginSpellCast( spell ):
	print "Snowball Swarm OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Snowball Swarm OnSpellEffect"

	game.particles( 'sp-evocation-conjure', spell.caster )

def OnBeginRound( spell ):
	print "Snowball Swarm OnBeginRound"

def OnBeginProjectile( spell, projectile, index_of_target ):
	print "Snowball Swarm OnBeginProjectile"

	#spell.proj_partsys_id = game.particles( 'sp-Snowball Swarm-proj', projectile )
	projectile.obj_set_int( obj_f_projectile_part_sys_id, game.particles( 'sp-Snowball Swarm-proj', projectile ) )

def OnEndProjectile( spell, projectile, index_of_target ):
	print "Snowball Swarm OnEndProjectile"

	remove_list = []

	spell.duration = 0
	dam = dice_new( '1d6' )
	# calculate dice rolled
	if (spell.caster_level >= 3) and (spell.caster_level <= 4):
		dam.number =  2 
	elif (spell.caster_level >=5) and (spell.caster_level <= 6):
		dam.number =  3
	elif (spell.caster_level >=7) and (spell.caster_level <= 8):
		dam.number =  4
	elif (spell.caster_level >=9) and (spell.caster_level <= 20):
		dam.number =  5
	game.particles_end( projectile.obj_get_int( obj_f_projectile_part_sys_id ) )
	game.particles( 'sp-Snowball Swarm-Hit', spell.target_loc )

	for target_item in spell.target_list:

		if target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_COLD, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ):
			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
		else:
			# saving throw unsuccessful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

		remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnEndSpellCast( spell ):
	print "Snowball Swarm OnEndSpellCast"