from toee import *

def OnBeginSpellCast( spell ):
	print "Tree Shape OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect ( spell ):
	print "Tree Shape OnSpellEffect"

	spell.duration = 60 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Tree Shape', spell.id, spell.duration, 10 )
	target.partsys_id = game.particles( 'sp-Tree Shape', spell.caster )

def OnBeginRound( spell ):
	print "Tree Shape OnBeginRound"

def OnEndSpellCast( spell ):
	print "Tree Shape OnEndSpellCast"