from toee import *
from utilities import *

def OnBeginSpellCast( spell ):
	print "Heat Metal OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Heat Metal OnSpellEffect"

	remove_list = []

	spell.duration = 7
	soundfizzle = 0

	for target_item in spell.target_list:
		xx,yy = location_to_axis(target_item.obj.location)
		if target_item.obj.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
			# Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
			target_item.obj.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1 )
			game.particles( 'swirled gas', target_item.obj )
			soundfizzle = 1
			remove_list.append( target_item.obj )
		else:

			armor_obj = target_item.obj.item_worn_at( item_wear_armor )

			if (armor_obj != OBJ_HANDLE_NULL) and (armor_obj.obj_get_int( obj_f_material ) == mat_metal):
				# wearing metal armor
				return_val = target_item.obj.condition_add_with_args( 'sp-Heat Metal', spell.id, spell.duration, 0 )
				if return_val == 1:
					target_item.partsys_id = game.particles( 'sp-Heat Metal', target_item.obj )
			else:
				# no metal armor
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31010 )
				remove_list.append( target_item.obj )
	if soundfizzle == 1:
		game.sound(7581,1)
		game.sound(7581,1)

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Heat Metal OnBeginRound"

def OnEndSpellCast( spell ):
	print "Heat Metal OnEndSpellCast"