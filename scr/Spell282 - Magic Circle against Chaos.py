from toee import *
from utilities import  * 

def OnBeginSpellCast( spell ):
	print "Magic Circle against Chaos OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def OnSpellEffect ( spell ):
	print "Magic Circle against Chaos OnSpellEffect"

	spell.duration = 100 * spell.caster_level
	target_item = spell.target_list[0]

	if target_item.obj.is_friendly( spell.caster ):

		target_item.obj.condition_add_with_args( 'sp-Magic Circle Outward', spell.id, spell.duration, 2 )
		target_item.partsys_id = game.particles( 'sp-Magic Circle against Chaos-OUT', target_item.obj )

	else:

		target_item.obj.condition_add_with_args( 'sp-Magic Circle Inward', spell.id, spell.duration, 2 )
		target_item.partsys_id = game.particles( 'sp-Magic Circle against Chaos-IN', target_item.obj )
	

def OnBeginRound( spell ):
	print "Magic Circle against Chaos OnBeginRound"

def OnEndSpellCast( spell ):
	print "Magic Circle against Chaos OnEndSpellCast"