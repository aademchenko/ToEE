from toee import *

def OnBeginSpellCast( spell ):
	print "Sanctuary OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Sanctuary OnSpellEffect"

	spell.duration = 1 * spell.caster_level
	target_item = spell.target_list[0]

	target_item.obj.condition_add_with_args( 'sp-Sanctuary', spell.id, spell.duration, 0 )
	target_item.partsys_id = game.particles( 'sp-Sanctuary', target_item.obj )

	#spell.target_list.remove_target( target_item.obj )
	#spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Sanctuary OnBeginRound"

def OnEndSpellCast( spell ):
	print "Sanctuary OnEndSpellCast"