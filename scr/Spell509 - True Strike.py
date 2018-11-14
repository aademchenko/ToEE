from toee import *

def OnBeginSpellCast( spell ):
	print "True Strike OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-divination-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "True Strike OnSpellEffect"

	spell.duration = 1

	target_item = spell.target_list[0]

	target_item.obj.condition_add_with_args( 'sp-True Strike', spell.id, spell.duration, 0 )
	target_item.partsys_id = game.particles( 'sp-True Strike', target_item.obj )

def OnBeginRound( spell ):
	print "True Strike OnBeginRound"

def OnEndSpellCast( spell ):
	print "True Strike OnEndSpellCast"