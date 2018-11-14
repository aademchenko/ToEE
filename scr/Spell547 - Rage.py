from toee import *

def OnBeginSpellCast( spell ):
	print "Rage OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Rage OnSpellEffect"

	remove_list = []

	spell.duration = 0

	for target_item in spell.target_list:

		if target_item.obj.is_friendly( spell.caster ):

			target_item.obj.condition_add_with_args( 'sp-Rage', spell.id, spell.duration, 0 )
			target_item.partsys_id = game.particles( 'sp-Rage', target_item.obj )

		else:

			game.particles( 'Fizzle', target_item.obj )
			remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Rage OnBeginRound"

def OnEndSpellCast( spell ):
	print "Rage OnEndSpellCast"