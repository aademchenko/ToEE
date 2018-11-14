from toee import *

def OnBeginSpellCast( spell ):
	print "Magic Fang OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Magic Fang OnSpellEffect"

	spell.duration = 10 * spell.caster_level
	target_item = spell.target_list[0]

	target_item.obj.condition_add_with_args( 'sp-Magic Fang', spell.id, spell.duration, 0 )
	target_item.partsys_id = game.particles( 'sp-Magic Fang', target_item.obj )

def OnBeginRound( spell ):
	print "Magic Fang OnBeginRound"

def OnEndSpellCast( spell ):
	print "Magic Fang OnEndSpellCast"