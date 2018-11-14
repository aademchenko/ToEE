from toee import *
from utilities import *
from Co8 import *

def OnBeginSpellCast( spell ):
	print "Analyze Dweomer OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-divination-conjure", spell.caster )

def OnSpellEffect ( spell ):
	print "Analyze Dweomer OnSpellEffect"
	remove_list = []
	spell.duration = spell.caster_level * 10
	if len(spell.target_list) == 1 and spell.target_list[0]== spell.caster:
		pass
	else:	
		if spell.caster.money_get()>= 150000:
			for t in spell.target_list:
				game.particles( 'sp-Identify', t.obj)
				t.obj.identify_all()
		else: 
			spell.caster.float_mesfile_line('mes\\spell.mes', 16009)	
	for target_item in spell.target_list:
		remove_list.append(target_item.obj)
	spell.target_list.remove_list(remove_list)
	if find_spell_obj_with_flag(spell.caster, 6400, OSF_IS_ANALYZE_DWEOMER) == OBJ_HANDLE_NULL:
		spell_obj = game.obj_create( 6400, spell.caster.location)
		set_spell_flag(spell_obj, OSF_IS_ANALYZE_DWEOMER)
		spell_obj.item_condition_add_with_args('Skill Circumstance Bonus', skill_spellcraft, 20)
		spell.caster.item_get(spell_obj)		
		spell.num_of_targets = 1
		spell.target_list[0].obj = spell.caster
		spell.caster.condition_add_with_args('sp-Endurance', spell.id, spell.duration, 0)
	else:
		spell.caster.float_mesfile_line('mes\\spell.mes', 16007)
		spell.spell_end(spell.id)	
	
	
	

def OnBeginRound( spell ):
	print "Analyze Dweomer OnBeginRound"
		
def OnEndSpellCast( spell ):
	print "Analyze Dweomer OnEndSpellCast"
	destroy_spell_obj_with_flag(spell.caster, 6400,OSF_IS_ANALYZE_DWEOMER)
