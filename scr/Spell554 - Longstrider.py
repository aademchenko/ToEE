from toee import *

def OnBeginSpellCast( spell ):
	print "Longstrider OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Longstrider OnSpellEffect"

	spell.duration = 600 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Longstrider', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Longstrider', target.obj )

def OnBeginRound( spell ):
	print "Longstrider OnBeginRound"

def OnEndSpellCast( spell ):
	print "Longstrider OnEndSpellCast"