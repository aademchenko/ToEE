from toee import *

def OnBeginSpellCast( spell ):
	print "Find Traps OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-divination-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Find Traps OnSpellEffect"

	spell.duration = 10 * spell.caster_level

	target_item = spell.target_list[0]

	target_item.obj.condition_add_with_args( 'sp-Find Traps', spell.id, spell.duration, 0 )
	target_item.partsys_id = game.particles( 'sp-Find Traps', target_item.obj )

	if (target_item.obj.d20_query( Q_Critter_Can_Find_Traps ) == 1):
		print target_item.obj, " can detect traps as rogue!"

def OnBeginRound( spell ):
	print "Find Traps OnBeginRound"

def OnEndSpellCast( spell ):
	print "Find Traps OnEndSpellCast"