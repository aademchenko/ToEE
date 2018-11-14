from toee import *

def OnBeginSpellCast( spell ):
	print "Potion of protection from fire OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Potion of protection from fire OnSpellEffect"

	spell.duration = spell.caster_level * 100

	if (spell.caster_level < 10):
		protection_pts = spell.caster_level * 12
	else:
		protection_pts = 120

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Potion of protection from energy', spell.id, spell.duration, D20DT_FIRE, protection_pts )
	#target.partsys_id = game.particles( 'sp-Potion of protection from energy', spell.caster )

	#spell.target_list.remove_target( target.obj )
	#spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Potion of protection from fire OnBeginRound"

def OnEndSpellCast( spell ):
	print "Potion of protection from fire OnEndSpellCast"