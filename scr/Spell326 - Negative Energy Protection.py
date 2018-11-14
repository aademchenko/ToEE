from toee import *

def OnBeginSpellCast( spell ):
	print "Negative Energy Protection OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Negative Energy Protection OnSpellEffect"

	spell.duration = 1 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Negative Energy Protection', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Negative Energy Protection', target.obj )

def OnBeginRound( spell ):
	print "Negative Energy Protection OnBeginRound"

def OnEndSpellCast( spell ):
	print "Negative Energy Protection OnEndSpellCast"