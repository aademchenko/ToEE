from toee import *

def OnBeginSpellCast( spell ):
	print "Vampiric Touch OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Vampiric Touch OnSpellEffect"

	spell.duration = 60
	target_item = spell.target_list[0]

	target_item.obj.condition_add_with_args( 'sp-Vampiric Touch', spell.id, spell.duration, 0 )
	target_item.partsys_id = game.particles( 'sp-Vampiric Touch', target_item.obj )

def OnBeginRound( spell ):
	print "Vampiric Touch OnBeginRound"

def OnEndSpellCast( spell ):
	print "Vampiric Touch OnEndSpellCast"