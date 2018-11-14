from toee import *

def OnBeginSpellCast( spell ):
	print "Good Hope OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Good Hope OnSpellEffect"

	spell.duration = 10 * spell.caster_level

	for target_item in spell.target_list:

		# apply despair
		return_val = target_item.obj.condition_add_with_args( 'sp-Emotion Hope', spell.id, spell.duration, 0 )
		if return_val == 1:
			target_item.partsys_id = game.particles( 'sp-Emotion-Hope-Hit', target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Good Hope OnBeginRound"

def OnEndSpellCast( spell ):
	print "Good Hope OnEndSpellCast"