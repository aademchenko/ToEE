from toee import *

def OnBeginSpellCast( spell ):
	print "Entropic Shield OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Entropic Shield OnSpellEffect"

	spell.duration = 60 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Entropic Shield', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Entropic Shield', spell.caster )

def OnBeginRound( spell ):
	print "Entropic Shield OnBeginRound"

def OnEndSpellCast( spell ):
	print "Entropic Shield OnEndSpellCast"