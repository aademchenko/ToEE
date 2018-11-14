from toee import *
from utilities import location_from_axis, location_to_axis

def OnBeginSpellCast( spell ):
	print "Fireball OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Fireball OnSpellEffect"

	game.particles( 'sp-Fireball-conjure', spell.caster )

def OnBeginRound( spell ):
	print "Fireball OnBeginRound"

def OnBeginProjectile( spell, projectile, index_of_target ):
	print "Fireball OnBeginProjectile"

	#spell.proj_partsys_id = game.particles( 'sp-Fireball-proj', projectile )
	projectile.obj_set_int( obj_f_projectile_part_sys_id, game.particles( 'sp-Fireball-proj', projectile ) )

def OnEndProjectile( spell, projectile, index_of_target ):
	print "Fireball OnEndProjectile"

	remove_list = []

	spell.duration = 0
	dam = dice_new( '1d6' )
	dam.number = min( 10, spell.caster_level )
	if game.global_vars[451] & 2**1 != 0:
		if game.leader.map == 5083:   ## Fire node - fire spells do double damage
			dam.number = dam.number * 2
		elif game.leader.map == 5084: ## Water node - fire spells do half damage
			dam.number = dam.number / 2


	game.particles_end( projectile.obj_get_int( obj_f_projectile_part_sys_id ) )
	xx,yy = location_to_axis(spell.target_loc)
	if game.leader.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
	# Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
	# This is for the projectile hitting inside the chamber - total fizzle
		tro = game.obj_create(14070, spell.target_loc)
		game.particles( 'swirled gas', spell.target_loc)
		tro.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1)
		tro.destroy()
		game.sound(7581,1)
		game.sound(7581,1)
		for target_item in spell.target_list:
			remove_list.append( target_item.obj )

	else: # suppose the fireball projectile lands outside the chamber, check individual targets
		game.particles( 'sp-Fireball-Hit', spell.target_loc )

		soundfizzle = 0
		for target_item in spell.target_list:
			xx,yy = location_to_axis(target_item.obj.location)
			if target_item.obj.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
				# Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
				game.particles( 'swirled gas', target_item.obj.location )
				target_item.obj.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1)

				soundfizzle = 1
				spell.target_list.remove_target( target_item.obj )
			else:
				if target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_FIRE, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ):
					# saving throw successful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
				else:
					# saving throw unsuccessful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			remove_list.append( target_item.obj )
		if soundfizzle == 1:
			game.sound(7581,1)
			game.sound(7581,1)
	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnEndSpellCast( spell ):
	print "Fireball OnEndSpellCast"