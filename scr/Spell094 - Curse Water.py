from toee import *

def OnBeginSpellCast( spell ):
	print "Curse Water OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Curse Water OnSpellEffect"

	spell.duration = 0
	target_item = spell.target_list[0]
	unholy_water_proto_id = 4226

	game.particles( 'sp-Curse Water', target_item.obj )
	item_obj = game.obj_create( unholy_water_proto_id, spell.target_loc )
	spell.caster.item_get( item_obj )

	spell.target_list.remove_target( target_item.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Curse Water OnBeginRound"

def OnEndSpellCast( spell ):
	print "Curse Water OnEndSpellCast"