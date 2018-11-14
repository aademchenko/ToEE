from toee import *

def OnBeginSpellCast( spell ):
	print "Bless Water OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Bless Water OnSpellEffect"

	spell.duration = 0
	target_item = spell.target_list[0]
	holy_water_proto_id = 4224

	game.particles( 'sp-Bless Water', target_item.obj )
	item_obj = game.obj_create( holy_water_proto_id, spell.target_loc )
	spell.caster.item_get( item_obj )

	spell.target_list.remove_target( target_item.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Bless Water OnBeginRound"

def OnEndSpellCast( spell ):
	print "Bless Water OnEndSpellCast"
