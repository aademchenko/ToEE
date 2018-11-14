from toee import *

def OnBeginSpellCast( spell ):
	print "Displacement OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-illusion-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Displacement OnSpellEffect"

	spell.duration = 1 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Displacement', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Displacement', target.obj )

def OnBeginRound( spell ):
	print "Displacement OnBeginRound"

def OnEndSpellCast( spell ):
	print "Displacement OnEndSpellCast"