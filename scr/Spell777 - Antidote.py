from toee import *
from utilities import *
from Co8 import *

def OnBeginSpellCast( spell ):
	print "Antidote OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def OnSpellEffect ( spell ):
	print "Antidote OnSpellEffect"

	spell.duration = 600

	if find_spell_obj_with_flag(spell.caster, 12706, OSF_IS_ANALYZE_DWEOMER) == OBJ_HANDLE_NULL:
		spell_obj = game.obj_create( 12706, spell.caster.location)
		set_spell_flag(spell_obj, OSF_IS_ANALYZE_DWEOMER)
		spell_obj.item_condition_add_with_args('Luck Poison Save Bonus', 5, 0)
		spell.caster.item_get(spell_obj)		
		spell.num_of_targets = 1
		spell.target_list[0].obj = spell.caster
		spell.caster.condition_add_with_args('sp-Endurance', spell.id, spell.duration, 0)
	else:
		spell.caster.float_mesfile_line('mes\\spell.mes', 16007)
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Antidote OnBeginRound"
		
def OnEndSpellCast( spell ):
	print "Antidote OnEndSpellCast"
	destroy_spell_obj_with_flag(spell.caster, 12706,OSF_IS_ANALYZE_DWEOMER)