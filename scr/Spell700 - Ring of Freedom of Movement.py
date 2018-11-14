from toee import *

def OnBeginSpellCast( spell ):
	print "Ring of Freedom of Movement OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Ring of Freedom of Movement OnSpellEffect"

	spell.duration = 0

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Ring of Freedom of Movement', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Freedom of Movement', target.obj )

def OnBeginRound( spell ):
	print "Ring of Freedom of Movement OnBeginRound"

def OnEndSpellCast( spell ):
	print "Ring of Freedom of Movement OnEndSpellCast"