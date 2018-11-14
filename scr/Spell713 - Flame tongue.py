from toee import *

def OnBeginSpellCast( spell ):
	print "Flame tongue OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Flame tongue OnSpellEffect"

def OnBeginRound( spell ):
	print "Flame tongue OnBeginRound"

def OnBeginProjectile( spell, projectile, index_of_target ):
	print "Flame tongue OnBeginProjectile"

	#spell.proj_partsys_id = game.particles( 'sp-Flame Tongue-proj', projectile )
	projectile.obj_set_int( obj_f_projectile_part_sys_id, game.particles( 'sp-Flame Tongue-proj', projectile ) )

def OnEndProjectile( spell, projectile, index_of_target ):
	print "Flame tongue OnEndProjectile"

	damage_dice = dice_new( '4d6' )

	spell.duration = 0

	game.particles_end( projectile.obj_get_int( obj_f_projectile_part_sys_id ) )
	target_item = spell.target_list[0]

	return_val = spell.caster.perform_touch_attack( target_item.obj )
	if return_val == 1:

		game.particles( 'sp-Flame Tongue-Hit', target_item.obj )

		# hit
		target_item.obj.spell_damage( spell.caster, D20DT_FIRE, damage_dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

	elif return_val == 2:

		game.particles( 'sp-Flame Tongue-Hit', target_item.obj )

		# critical hit
		damage_dice.num = 8
		target_item.obj.spell_damage( spell.caster, D20DT_FIRE, damage_dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

	else:

		# missed
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30007 )

		game.particles( 'Fizzle', target_item.obj )

	spell.target_list.remove_target( target_item.obj )
	spell.spell_end( spell.id )

def OnEndSpellCast( spell ):
	print "Flame tongue OnEndSpellCast"