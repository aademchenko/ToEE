from toee import *

def OnBeginSpellCast( spell ):
	print "Faerie Fire OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Faerie Fire OnSpellEffect"

	spell.duration = 10 * spell.caster_level

	for target_item in spell.target_list:
		# no save
		# apply 'faerie fire'
		target_item.obj.condition_add_with_args( 'sp-Faerie Fire', spell.id, spell.duration, 0 )
		target_item.partsys_id = game.particles( 'ef-Faerie Fire', target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Faerie Fire OnBeginRound"

def OnEndSpellCast( spell ):
	print "Faerie Fire OnEndSpellCast"