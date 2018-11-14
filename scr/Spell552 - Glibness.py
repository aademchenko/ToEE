from toee import *

def OnBeginSpellCast( spell ):
	print "Glibness OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Glibness OnSpellEffect"

	spell.duration = 100 * spell.caster_level
	target_item = spell.target_list[0]

	target_item.obj.condition_add_with_args( 'sp-Glibness', spell.id, spell.duration, 0 )
	target_item.partsys_id = game.particles( 'sp-Glibness', target_item.obj )

def OnBeginRound( spell ):
	print "Glibness OnBeginRound"

def OnEndSpellCast( spell ):
	print "Glibness OnEndSpellCast"