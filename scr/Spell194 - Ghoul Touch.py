from toee import *

def OnBeginSpellCast( spell ):
	print "Ghoul Touch OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Ghoul Touch OnSpellEffect"

	spell.duration = 0
	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Ghoul Touch', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Ghoul Touch', target.obj )

def OnBeginRound( spell ):
	print "Ghoul Touch OnBeginRound"

def OnEndSpellCast( spell ):
	print "Ghoul Touch OnEndSpellCast"

def OnAreaOfEffectHit( spell ):
	print "Ghoul Touch OnAreaOfEffectHit"

def OnSpellStruck( spell ):
	print "Ghoul Touch OnSpellStruck"