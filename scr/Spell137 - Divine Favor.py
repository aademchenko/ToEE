from toee import *

def OnBeginSpellCast( spell ):
	print "Divine Favor OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Divine Favor OnSpellEffect"

	if spell.caster_level >= 9:
		bonus = 3
	elif spell.caster_level >= 6:
		bonus = 2
	else:
		bonus = 1

	spell.duration = 10

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Divine Favor', spell.id, spell.duration, bonus )
	target.partsys_id = game.particles( 'sp-Divine Favor', target.obj )

def OnBeginRound( spell ):
	print "Divine Favor OnBeginRound"

def OnEndSpellCast( spell ):
	print "Divine Favor OnEndSpellCast"