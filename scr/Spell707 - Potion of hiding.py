from toee import *

def OnBeginSpellCast( spell ):
	print "Potion of hiding OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Potion of hiding OnSpellEffect"

	spell.duration = 600
	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Potion of hiding', spell.id, effect_duration, 0 )
	#target.partsys_id = game.particles( 'sp-Potion of hiding', spell.caster )

	#spell.target_list.remove_target( target.obj )
	#spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Potion of hiding OnBeginRound"

def OnEndSpellCast( spell ):
	print "Potion of hiding OnEndSpellCast"