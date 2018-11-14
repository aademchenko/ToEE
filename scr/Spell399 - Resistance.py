from toee import *

def OnBeginSpellCast( spell ):
	print "Resistance OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Resistance OnSpellEffect"

	spell.duration = 10

	target = spell.target_list[0]

	# check if target is friendly (willing target)
	if not target.obj.is_friendly( spell.caster ):
		if target.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
			# saving throw successful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
			game.particles( 'Fizzle', target.obj )
			spell.target_list.remove_target( target.obj )

		else:
			# saving throw unsuccessful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
			target.obj.condition_add_with_args( 'sp-Resistance', spell.id, spell.duration, 0 )
			target.partsys_id = game.particles( 'sp-Resistance', target.obj )

	else:
		target.obj.condition_add_with_args( 'sp-Resistance', spell.id, spell.duration, 0 )
		target.partsys_id = game.particles( 'sp-Resistance', target.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Resistance OnBeginRound"

def OnEndSpellCast( spell ):
	print "Resistance OnEndSpellCast"