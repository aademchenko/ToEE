from toee import *

def OnBeginSpellCast( spell ):
	print "Greater Magic Fang OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect ( spell ):
	print "Greater Magic Fang OnSpellEffect"

	enhancement_bonus = spell.caster_level / 4

	spell.duration = 600 * spell.caster_level
	target_item = spell.target_list[0]

	target_item.obj.condition_add_with_args( 'sp-Greater Magic Fang', spell.id, spell.duration, enhancement_bonus )
	target_item.partsys_id = game.particles( 'sp-Greater Magic Fang', target_item.obj )

def OnBeginRound( spell ):
	print "Greater Magic Fang OnBeginRound"

def OnEndSpellCast( spell ):
	print "Greater Magic Fang OnEndSpellCast"