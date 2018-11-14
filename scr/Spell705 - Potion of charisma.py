from toee import *

def OnBeginSpellCast( spell ):
	print "Potion of charisma OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Potion of charisma OnSpellEffect"

	spell.duration = 1800
	target = spell.target_list[0]

	dice = dice_new( '1d4' )
	dice.bonus = 1
	bonus = dice.roll()

	target.obj.condition_add_with_args( 'sp-Potion of charisma', spell.id, bonus, spell.duration )
	#target.partsys_id = game.particles( 'sp-Potion of charisma', spell.caster )

	#spell.target_list.remove_target( target.obj )
	#spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Potion of charisma OnBeginRound"

def OnEndSpellCast( spell ):
	print "Potion of charisma OnEndSpellCast"