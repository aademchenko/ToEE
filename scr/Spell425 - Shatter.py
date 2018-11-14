from toee import *

def OnBeginSpellCast( spell ):
	print "Shatter OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Shatter OnSpellEffect"

	spell.duration = 0
	target_item = spell.target_list[0]

	damage_dice = dice_new( '1d6' )
	damage_dice.number = min( spell.caster_level, 10 )

	target_item.partsys_id = game.particles( 'sp-Shatter', target_item.obj )

	if target_item.obj.is_category_subtype( mc_subtype_earth ):
		if not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):

			# saving throw unsuccessful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			# full damage
			target_item.obj.spell_damage( spell.caster, D20DT_SONIC, damage_dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

		else:

			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			# half damage
			target_item.obj.spell_damage_with_reduction( spell.caster, D20DT_SONIC, damage_dice, D20DAP_UNSPECIFIED, DAMAGE_REDUCTION_HALF, D20A_CAST_SPELL, spell.id )

	else:
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31011 )
		game.particles( 'Fizzle', target_item.obj )

	spell.target_list.remove_target( target_item.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Shatter OnBeginRound"

def OnEndSpellCast( spell ):
	print "Shatter OnEndSpellCast"