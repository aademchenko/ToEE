from toee import *

def OnBeginSpellCast( spell ):
	print "Remove Paralysis OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Remove Paralysis OnSpellEffect"

	remove_list = []

	spell.duration = 0

	for target_item in spell.target_list:

		game.particles( 'sp-Remove Paralysis', target_item.obj )

		target_item.partsys_id = game.particles( 'sp-Remove Paralysis', target_item.obj )
		target_item.obj.condition_add_with_args( 'sp-Remove Paralysis', spell.id, spell.duration, 0 )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Remove Paralysis OnBeginRound"

def OnEndSpellCast( spell ):
	print "Remove Paralysis OnEndSpellCast"