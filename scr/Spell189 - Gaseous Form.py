from toee import *

def OnBeginSpellCast( spell ):
	print "Gaseous Form OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Gaseous Form OnSpellEffect"

	spell.duration = 120 * spell.caster_level
	target_item = spell.target_list[0]

	if target_item.obj.is_friendly( spell.caster ):

		target_item.obj.condition_add_with_args( 'sp-Gaseous Form', spell.id, spell.duration, 0 )
		target_item.partsys_id = game.particles( 'sp-Gaseous Form', target_item.obj )

	else:

		game.particles( 'Fizzle', target_item.obj )
		spell.target_list.remove_target( target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Gaseous Form OnBeginRound"

def OnEndSpellCast( spell ):
	print "Gaseous Form OnEndSpellCast"