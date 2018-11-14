from toee import *

def OnBeginSpellCast( spell ):
	print "Polar Ray OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Polar Ray OnSpellEffect"

def OnBeginRound( spell ):
	print "Polar Ray OnBeginRound"

def OnBeginProjectile( spell, projectile, index_of_target ):
	print "Polar Ray OnBeginProjectile"

	#spell.proj_partsys_id = game.particles( 'sp-Ray of Frost', projectile )
	projectile.obj_set_int( obj_f_projectile_part_sys_id, game.particles( 'sp-Ray of Frost', projectile ) )

def OnEndProjectile( spell, projectile, index_of_target ):
	print "Polar Ray OnEndProjectile"

	damage_dice = dice_new( '1d6' )
	damage_dice.num = min(25, spell.caster_level)

	spell.duration = 0

	game.particles_end( projectile.obj_get_int( obj_f_projectile_part_sys_id ) )
	target_item = spell.target_list[0]

	####################################################
	# WF Ray fix added by Shiningted (& two lines below)
	####################################################

	has_it = 0
	x = 0
	y = 0

	if spell.caster.has_feat(feat_weapon_focus_ray):
		# game.particles( "sp-summon monster I", game.party[0] )
		has_it = 1
		x = spell.caster.stat_level_get(stat_dexterity)
		y = x + 2
		if spell.caster.has_feat(feat_greater_weapon_focus_ray):
			y = y + 2
		spell.caster.stat_base_set(stat_dexterity, y)

	####################################################

	return_val = spell.caster.perform_touch_attack( target_item.obj )
	if return_val == 1:

		game.particles( 'sp-Ray of Frost-Hit', target_item.obj )

		# hit
		target_item.obj.spell_damage( spell.caster, D20DT_COLD, damage_dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

	elif return_val == 2:

		game.particles( 'sp-Ray of Frost-Hit', target_item.obj )

		# critical hit
		damage_dice.num = damage_dice.num * 2
		target_item.obj.spell_damage( spell.caster, D20DT_COLD, damage_dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

	else:

		# missed
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30007 )

		game.particles( 'Fizzle', target_item.obj )

	if has_it == 1:
		spell.caster.stat_base_set(stat_dexterity, x)

	spell.target_list.remove_target( target_item.obj )
	spell.spell_end( spell.id )

def OnEndSpellCast( spell ):
	print "Polar Ray OnEndSpellCast"
