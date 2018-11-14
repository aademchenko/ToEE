from toee import *

def OnBeginSpellCast( spell ):
	print "False Life OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "False Life OnSpellEffect"

	spell.duration = 600 * spell.caster_level
	target_item = spell.target_list[0]

	target_item.obj.condition_add_with_args( 'sp-False Life', spell.id, spell.duration, 0 )
	target_item.partsys_id = game.particles( 'sp-False Life', target_item.obj )

def OnBeginRound( spell ):
	print "False Life OnBeginRound"

def OnEndSpellCast( spell ):
	print "False Life OnEndSpellCast"