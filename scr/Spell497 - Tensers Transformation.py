from toee import *
from utilities import *
from Co8 import *

def OnBeginSpellCast( spell ):
	print "Tensers Transformation OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Tensers Transformation OnSpellEffect"

	spell.duration = 1 * spell.caster_level
	dam = dice_new( "1d1" )
	dam.num = spell.caster_level
	spell.dc = 0

	if find_spell_obj_with_flag(spell.caster, 6400, OSF_IS_TENSERS_TRANSFORMATION) == OBJ_HANDLE_NULL:
		weapon = spell.caster.item_worn_at(3)
		if weapon != OBJ_HANDLE_NULL:
			set_spell_flag(weapon, OSF_IS_TENSERS_TRANSFORMATION)
			weapon.obj_set_int(obj_f_weapon_type, 12)
			weapon.item_flag_set(OIF_NO_DROP)
			spell.dc = weapon.name								# OKAY I am trying to avoid stuff like this but I need a variable, not otherwise used,and unique to this spell that I know will still be alive in OnEndSpellcast

		spell_obj = game.obj_create(6400, spell.caster.location)
		set_spell_flag(spell_obj, OSF_IS_TENSERS_TRANSFORMATION)
		spell_obj.item_condition_add_with_args('sp-Feeblemind', 0, 0, 0)			# yeah it works, you can put spell effects on items and they will affect the holder
		spell_obj.item_condition_add_with_args('Saving Throw Resistance Bonus', 0, 9)
		spell_obj.item_condition_add_with_args('Saving Throw Resistance Bonus', 1, 4)
		spell_obj.item_condition_add_with_args('Saving Throw Resistance Bonus', 2, 4)
		spell_obj.item_condition_add_with_args('Attribute Enhancement Bonus', 0, -2)		# divine power gives too much strength bonus
		spell_obj.item_condition_add_with_args('Attribute Enhancement Bonus', 1, 4)
		spell_obj.item_condition_add_with_args('Attribute Enhancement Bonus', 2, 4)
		spell_obj.item_condition_add_with_args('Amulet of Natural Armor', 4, 0)
		spell.caster.item_get(spell_obj)		
		spell.caster.condition_add_with_args('sp-Divine Power', spell.id, spell.duration, 0)	# to make base attack bonus equal caster level did not put on item in order that a spell marker would appear on casters icon
		spell.caster.damage(OBJ_HANDLE_NULL, D20DT_FORCE, dam, D20DAP_NORMAL) 

	else:
		spell.caster.float_mesfile_line( 'mes\\spell.mes', 16007 )
		spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Tensers Transformation OnBeginRound"
	print spell.target_list
	
def OnEndSpellCast( spell ):
	print "Tensers Transformation OnEndSpellCast"

	destroy_spell_obj_with_flag(spell.caster, 6400, OSF_IS_TENSERS_TRANSFORMATION)
	item_wielded = spell.caster.item_worn_at(3)
	if (item_wielded != OBJ_HANDLE_NULL):
		if (item_wielded.name == spell.dc) and (is_spell_flag_set(item_wielded, OSF_IS_TENSERS_TRANSFORMATION) != 0):
			new_weapon = game.obj_create(spell.dc, spell.caster.location)
			item_wielded.obj_set_int(obj_f_weapon_type, new_weapon.obj_get_int(obj_f_weapon_type))
			unset_spell_flag(item_wielded, OSF_IS_TENSERS_TRANSFORMATION)
			item_wielded.item_flag_unset(OIF_NO_DROP)
			new_weapon.destroy()

	else:
		if spell.dc != 0:	
			weapon = find_spell_obj_with_flag(spell.caster, spell.dc, OSF_IS_TENSERS_TRANSFORMATION)
			if weapon != OBJ_HANDLE_NULL:							## this shouldn't ever happen but better check
				new_weapon = game.obj_create(spell.dc, spell.caster.location)
				weapon.obj_set_int(obj_f_weapon_type, new_weapon.obj_get_int(obj_f_weapon_type))
				unset_spell_flag(weapon, OSF_IS_TENSERS_TRANSFORMATION)
				weapon.item_flag_unset(OIF_NO_DROP)
				new_weapon.destroy()
