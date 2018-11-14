from toee import *
from stench import *

def OnBeginSpellCast( spell ):
	print "Hezrou Stench OnBeginSpellCast id= ", spell.id
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster ) # change to stinking cloud?

def	OnSpellEffect( spell ):
	print "Hezrou Stench OnSpellEffect"
	spell.dc = 100
	spell.duration = 100
	processStench(spell.caster, spell.id)
	spell.spell_end(spell.id)

def OnAreaOfEffectHit( spell ):
	print "Hezrou Stench OnAreaOfEffectHit"

def OnBeginRound( spell ):
	print "Hezrou Stench OnBeginRound"

def OnEndSpellCast( spell ):
	print "Hezrou Stench OnEndSpellCast"
	endStench(spell.caster)

