from toee import *

def OnBeginSpellCast( spell ):
	print "Clairaudience/Clairvoyance OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-divination-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Clairaudience/Clairvoyance OnSpellEffect"

	spell.duration = 10 * spell.caster_level

	# HTN - WIP! temporary until we have a func() that clears up a section of fog
	partsys_id = game.particles( 'sp-Clairaudience-Clairvoyance', spell.caster )
	spell.caster.condition_add_with_args( 'sp-Clairaudience Clairvoyance', spell.id, spell.duration, partsys_id )

def OnBeginRound( spell ):
	print "Clairaudience/Clairvoyance OnBeginRound"

def OnEndSpellCast( spell ):
	print "Clairaudience/Clairvoyance OnEndSpellCast"