from toee import *

def OnBeginSpellCast( spell ):
	print "Chill Metal OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Chill Metal OnSpellEffect"

	remove_list = []

	spell.duration = 7

	for target_item in spell.target_list:

		armor_obj = target_item.obj.item_worn_at( item_wear_armor )

		if (armor_obj != OBJ_HANDLE_NULL) and (armor_obj.obj_get_int( obj_f_material ) == mat_metal):
			# wearing metal armor
			return_val = target_item.obj.condition_add_with_args( 'sp-Chill Metal', spell.id, spell.duration, 0 )
			if return_val == 1:
				target_item.partsys_id = game.particles( 'sp-Chill Metal', target_item.obj )
		else:
			# no metal armor
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31010 )
			remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Chill Metal OnBeginRound"

def OnEndSpellCast( spell ):
	print "Chill Metal OnEndSpellCast"