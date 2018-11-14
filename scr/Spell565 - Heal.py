from toee import *
from utilities import  *
from Co8 import *

def OnBeginSpellCast( spell ):
	print "Heal OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect ( spell ):
	print "Heal OnSpellEffect"
	is_tensers = 0
	spell.duration = 0

	target = spell.target_list[0].obj
	print "target = " , target	
	is_tensers = check_for_tensers(target)
	print "is_tensers = ", is_tensers

	npc = spell.caster			##  added so NPC's can use potion
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL and spell.caster_level <= 0:
		spell.caster_level = 10

	game.particles( 'sp-Heal', target )

	# check if target is undead
	if target.is_category_type( mc_type_undead ):
		# Harm target
		target.condition_add_with_args( 'sp-Harm', spell.id, spell.duration, 0 )
	else:
		# Heal undead
		target.condition_add_with_args( 'sp-Heal', spell.id, spell.duration, 0 )
	if is_tensers == 1:
		replace_tensers(target)
		
	spell.target_list.remove_target( target )
	
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Heal OnBeginRound"

def OnEndSpellCast( spell ):
	print "Heal OnEndSpellCast"

def check_for_tensers(target):
	if find_spell_obj_with_flag(target, 6400, OSF_IS_TENSERS_TRANSFORMATION) != OBJ_HANDLE_NULL:
		destroy_spell_obj_with_flag(target, 6400, OSF_IS_TENSERS_TRANSFORMATION)
		return 1
	else:
		return 0
		
def replace_tensers(target):
	spell_obj = game.obj_create(6400, target.location)
	set_spell_flag(spell_obj, OSF_IS_TENSERS_TRANSFORMATION)
	spell_obj.item_condition_add_with_args('sp-Feeblemind', 0,0,0)#yeah it works, you can put spell effects on items and they will affect the holder
	spell_obj.item_condition_add_with_args('Saving Throw Resistance Bonus', 0, 9)
	spell_obj.item_condition_add_with_args('Saving Throw Resistance Bonus', 1, 4)
	spell_obj.item_condition_add_with_args('Saving Throw Resistance Bonus', 2, 4)
	spell_obj.item_condition_add_with_args('Attribute Enhancement Bonus', 0, -2)#divine power gives too much strength bonus
	spell_obj.item_condition_add_with_args('Attribute Enhancement Bonus', 1, 4)
	spell_obj.item_condition_add_with_args('Attribute Enhancement Bonus', 2, 4)
	spell_obj.item_condition_add_with_args('Amulet of Natural Armor', 4, 0)
	target.item_get(spell_obj)
	print "spell_obj = ", spell_obj
