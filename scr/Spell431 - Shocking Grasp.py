from toee import *

def OnBeginSpellCast( spell ):
	print "Shocking Grasp OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Shocking Grasp OnSpellEffect"

	spell.duration = 0

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Shocking Grasp', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Shocking Grasp', target.obj )

def OnBeginRound( spell ):
	print "Shocking Grasp OnBeginRound"

def OnEndSpellCast( spell ):
	print "Shocking Grasp OnEndSpellCast"