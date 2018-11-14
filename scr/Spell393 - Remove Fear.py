from toee import *

def OnBeginSpellCast( spell ):
	print "Remove Fear OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Remove Fear OnSpellEffect"

	remove_list = []

	spell.duration = 0

	for target_item in spell.target_list:

		game.particles( 'sp-Remove Fear', target_item.obj )

		return_val = target_item.partsys_id = game.particles( 'sp-Remove Fear', target_item.obj )
		if return_val == 1:
			target_item.obj.condition_add_with_args( 'sp-Remove Fear', spell.id, spell.duration, 0 )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Remove Fear OnBeginRound"

def OnEndSpellCast( spell ):
	print "Remove Fear OnEndSpellCast"