from toee import *

def OnBeginSpellCast( spell ):
	print "Guidance OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Guidance OnSpellEffect"

	spell.duration = 10
	target_item = spell.target_list[0]

	target_item.obj.condition_add_with_args( 'sp-Guidance', spell.id, spell.duration, 0 )
	target_item.partsys_id = game.particles( 'sp-Guidance', target_item.obj )

def OnBeginRound( spell ):
	print "Guidance OnBeginRound"

def OnEndSpellCast( spell ):
	print "Guidance OnEndSpellCast"