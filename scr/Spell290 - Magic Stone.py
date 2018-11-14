from toee import *

def OnBeginSpellCast( spell ):
	print "Magic Stone OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Magic Stone OnSpellEffect"

	game.particles( "sp-Magic Stone", spell.caster )

def OnBeginRound( spell ):
	print "Magic Stone OnBeginRound"

def OnBeginProjectile( spell, projectile, index_of_target ):
	print "Magic Stone OnBeginProjectile"

	projectile.obj_set_int( obj_f_projectile_part_sys_id, game.particles( 'sp-Melfs Acid Arrow Projectile', projectile ) )

def OnEndProjectile( spell, projectile, index_of_target ):
	print "Magic Stone OnEndProjectile"

	game.particles_end( projectile.obj_get_int( obj_f_projectile_part_sys_id ) )

	dice = dice_new( "1d6" )
	dice.bonus = 1
	target = spell.target_list[0]

	attack_successful = spell.caster.perform_touch_attack( target.obj )

	# perform ranged touch attack
	if attack_successful == 1:

		# hit
		game.particles( 'Fizzle', target.obj )

		# check if target is undead
		if target.obj.is_category_type( mc_type_undead ):
			dice.num = 2
			dice.bonus = 2
			target.obj.spell_damage( spell.caster, D20DT_FORCE, dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
		else:
			target.obj.spell_damage( spell.caster, D20DT_FORCE, dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

	elif attack_successful == 2:

		# critical hit
		game.particles( 'Fizzle', target.obj )
		dice.num = 2

		# check if target is undead
		if target.obj.is_category_type( mc_type_undead ):
			dice.num = 4
			dice.bonus = 4
			target.obj.spell_damage( spell.caster, D20DT_MAGIC, dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
		else:
			target.obj.spell_damage( spell.caster, D20DT_MAGIC, dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

	else:

		# missed
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30007 )

		game.particles( 'Fizzle', target.obj )

	spell.target_list.remove_target( target.obj )
	spell.spell_end( spell.id )

def OnEndSpellCast( spell ):
	print "Magic Stone OnEndSpellCast"