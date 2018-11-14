from toee import *

def OnBeginSpellCast( spell ):
	print "Invisibility to Undead OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Invisibility to Undead OnSpellEffect"

	spell.duration = 100 * spell.caster_level

	for target_item in spell.target_list:

		target_item.obj.condition_add_with_args( 'sp-Invisibility to Undead', spell.id, spell.duration, 0 )
		target_item.partsys_id = game.particles( 'sp-Invisibility to Undead', target_item.obj )

def OnBeginRound( spell ):
	print "Invisibility to Undead OnBeginRound"

def OnEndSpellCast( spell ):
	print "Invisibility to Undead OnEndSpellCast"