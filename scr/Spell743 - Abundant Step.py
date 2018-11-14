from toee import *

def OnBeginSpellCast(spell):
#	print "Abundant Step OnBeginSpellCast"
#	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level


def	OnSpellEffect(spell):
#	print "Abundant Step OnSpellEffect"

	target = spell.caster
	item = target.item_worn_at(15)
	if (item != OBJ_HANDLE_NULL and item.name == 12420):
		monkLevel = target.stat_level_get(stat_level_monk)
		print "wearing belt, monk level= ", monkLevel
		
		if (monkLevel >= 12):
			if target.d20_query_has_spell_condition(sp_Dimensional_Anchor) == 0:
				game.particles('sp-Dimension Door', spell.caster)
				target.fade_to(0, 10, 40)
				game.timeevent_add(fade_back_in, (target, spell.target_loc, spell), 750, 1)
			else:
				target.float_mesfile_line('mes\\spell.mes', 30011)
				game.particles('Fizzle', target)
				spell.target_list.remove_target(target)
				spell.spell_end(spell.id)
		
		else:
			target.float_mesfile_line('mes\\spell.mes', 30020)
			
	spell.target_list.remove_target(target)
	spell.spell_end(spell.id)
	return	
			

def OnBeginRound(spell):
	print "Abundant Step OnBeginRound"

def OnEndSpellCast(spell):
	print "Abundant Step OnEndSpellCast"

def fade_back_in(target, loc, spell):
	target.move(loc, 0.0, 0.0)
	game.particles('sp-Dimension Door', target)
	target.fade_to(255, 10, 5)
	spell.target_list.remove_target(target)
	spell.spell_end(spell.id)
