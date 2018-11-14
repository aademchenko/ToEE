from toee import *

def OnBeginSpellCast( spell ):
	print "Meld Into Stone OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Meld Into Stone OnSpellEffect"

	spell.duration = 100 * spell.caster_level

	target = spell.target_list[0]

	print "MELD INTO STONE: need func() to sink player into ground"

	target.obj.condition_add_with_args( 'sp-Meld Into Stone', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Meld Into Stone', target.obj )

def OnBeginRound( spell ):
	print "Meld Into Stone OnBeginRound"

def OnEndSpellCast( spell ):
	print "Meld Into Stone OnEndSpellCast"