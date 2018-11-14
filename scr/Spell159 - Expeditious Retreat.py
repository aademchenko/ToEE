from toee import *

def OnBeginSpellCast( spell ):
	print "Expeditious Retreat OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Expeditious Retreat OnSpellEffect"

	spell.duration = 10 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Expeditious Retreat', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Expeditious Retreat', target.obj )

def OnBeginRound( spell ):
	print "Expeditious Retreat OnBeginRound"

def OnEndSpellCast( spell ):
	print "Expeditious Retreat OnEndSpellCast"