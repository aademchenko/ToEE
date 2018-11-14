from toee import *

def OnBeginSpellCast( spell ):
	print "Dispel Earth OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Dispel Earth OnSpellEffect"

	spell.duration = 1 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Dispel Earth', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Dispel Earth', target.obj )

def OnBeginRound( spell ):
	print "Dispel Earth OnBeginRound"

def OnEndSpellCast( spell ):
	print "Dispel Earth OnEndSpellCast"