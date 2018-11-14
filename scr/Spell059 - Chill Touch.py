from toee import *

def OnBeginSpellCast( spell ):
	print "Chill Touch OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Chill Touch OnSpellEffect"

	spell.duration = 1 * spell.caster_level

	#print "number of charges: ", spell.duration

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Chill Touch', spell.id, spell.duration, spell.duration )
	target.partsys_id = game.particles( 'sp-Chill Touch', target.obj )

def OnBeginRound( spell ):
	print "Chill Touch OnBeginRound"

def OnEndSpellCast( spell ):
	print "Chill Touch OnEndSpellCast"