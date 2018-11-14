from toee import *

def OnBeginSpellCast( spell ):
	print "Identify OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-divination-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Identify OnSpellEffect"

	spell.duration = 0

	target_item = spell.target_list[0]

	game.particles( 'sp-Identify', spell.caster )
	target_item.obj.item_flag_set( OIF_IDENTIFIED )

	spell.target_list.remove_target( target_item.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Identify OnBeginRound"

def OnEndSpellCast( spell ):
	print "Identify OnEndSpellCast"