from toee import *

def OnBeginSpellCast( spell ):
	print "Hold Animal OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Hold Animal OnSpellEffect"

	spell.duration = 1 * spell.caster_level

	target = spell.target_list[0]

	if target.obj.is_category_type( mc_type_animal ):

		# allow Will saving throw to negate
		if target.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
			# saving throw successful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			game.particles( 'Fizzle', target.obj )
			spell.target_list.remove_target( target.obj )
		else:
			# saving throw unsuccessful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			# HTN - apply condition HOLD (paralyzed)
			target.obj.condition_add_with_args( 'sp-Hold Animal', spell.id, spell.duration, 0 )
			target.partsys_id = game.particles( 'sp-Hold Animal', target.obj )

	else:
		# not an animal
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 31002 )

		game.particles( 'Fizzle', target.obj )
		spell.target_list.remove_target( target.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Hold Animal OnBeginRound"

def OnEndSpellCast( spell ):
	print "Hold Animal OnEndSpellCast"