from toee import *

def OnBeginSpellCast( spell ):
	print "Shillelagh OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Shillelagh OnSpellEffect"

	spell.duration = 10 * spell.caster_level
	target_item = spell.target_list[0]
	holy_water_proto_id = 4223

	game.particles( 'sp-Shillelagh', target_item.obj )
	item_obj = game.obj_create( holy_water_proto_id, spell.target_loc )
	item_obj.d20_status_init()

	# save item obj in target_list
	spell.target_list[0].obj = item_obj
	spell.caster.item_get( item_obj )
	spell.caster.condition_add_with_args( 'sp-Shillelagh', spell.id, spell.duration, 0 )

	# add magic_stone condition to stones
	#item_obj.condition_add_with_args( 'sp-Shillelagh', spell.id, spell.duration, 0 )
	#item_obj.set_initiative( spell.caster.get_initiative() )

	#spell.target_list.remove_target( target_item.obj )
	#spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Shillelagh OnBeginRound"

def OnEndSpellCast( spell ):
	print "Shillelagh OnEndSpellCast"