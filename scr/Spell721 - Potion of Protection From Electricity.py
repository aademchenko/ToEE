from toee import *

def OnBeginSpellCast( spell ):
	print "Protection From Electricity OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Protection From Elements OnSpellEffect"

	element_type = ELECTRICITY
	partsys_type = 'sp-Protection From Elements-electricity'

	#spell.duration = 100 * 2
	#spell.duration = 10

	target_item = spell.target_list[0]

	target_item.obj.condition_add_with_args( 'sp-Protection From Elements', spell.id, spell.duration, element_type )
	target_item.partsys_id = game.particles( partsys_type, target_item.obj )

	#spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Protection From Electricity OnBeginRound"

def OnEndSpellCast( spell ):
	print "Protection From Electricity OnEndSpellCast"