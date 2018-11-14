from toee import *

def OnBeginSpellCast( spell ):
	print "Invisibility to Animals OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Invisibility to Animals OnSpellEffect"

	spell.duration = 100 * spell.caster_level

	for target_item in spell.target_list:

		target_item.obj.condition_add_with_args( 'sp-Invisibility to Animals', spell.id, spell.duration, 0 )
		target_item.partsys_id = game.particles( 'sp-Invisibility to Animals', target_item.obj )

def OnBeginRound( spell ):
	print "Invisibility to Animals OnBeginRound"

def OnEndSpellCast( spell ):
	print "Invisibility to Animals OnEndSpellCast"