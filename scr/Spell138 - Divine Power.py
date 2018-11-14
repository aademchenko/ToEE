from toee import *

def OnBeginSpellCast( spell ):
	print "Divine Power OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Divine Power OnSpellEffect"

	spell.duration = 1 * spell.caster_level

	target_item = spell.target_list[0]

	target_item.obj.condition_add_with_args( 'sp-Divine Power', spell.id, spell.duration, 0 )
	target_item.partsys_id = game.particles( 'sp-Divine Power', target_item.obj )

def OnBeginRound( spell ):
	print "Divine Power OnBeginRound"

def OnEndSpellCast( spell ):
	print "Divine Power OnEndSpellCast"