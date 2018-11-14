from toee import *

def OnBeginSpellCast( spell ):
	print "Protection From Earth OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Protection From Earth OnSpellEffect"

	spell.duration = 10 * spell.caster_level
	target_item = spell.target_list[0]

	if target_item.obj.is_friendly( spell.caster ):

		target_item.obj.condition_add_with_args( 'sp-Protection From Monster', spell.id, spell.duration, 2 )
		target_item.partsys_id = game.particles( 'sp-Protection From Earth', target_item.obj )

	elif not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

		# saving throw unsuccesful
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

		target_item.obj.condition_add_with_args( 'sp-Protection From Monster', spell.id, spell.duration, 2 )
		target_item.partsys_id = game.particles( 'sp-Protection From Earth', target_item.obj )

	else:

		# saving throw successful
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

		game.particles( 'Fizzle', target_item.obj )
		spell.target_list.remove_target( target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Protection From Earth OnBeginRound"

def OnEndSpellCast( spell ):
	print "Protection From Earth OnEndSpellCast"