from toee import *

def OnBeginSpellCast( spell ):
	print "Remove Disease OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect ( spell ):
	print "Remove Disease OnSpellEffect"

	spell.duration = 0

	target = spell.target_list[0]

	game.particles( 'sp-Remove Disease', target.obj )

	target.partsys_id = game.particles( 'sp-Remove Disease', target.obj )
	target.obj.condition_add_with_args( 'sp-Remove Disease', spell.id, spell.duration, 0 )

	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Remove Disease OnBeginRound"

def OnEndSpellCast( spell ):
	print "Remove Disease OnEndSpellCast"