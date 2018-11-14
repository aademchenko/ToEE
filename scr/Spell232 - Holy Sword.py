from toee import *
from utilities import *

def OnBeginSpellCast( spell ):
	print "Holy Sword OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )
	

def OnSpellEffect ( spell ):
	print "Holy Sword OnSpellEffect"
	#game.particles("sp-Raise Dead", spell.caster)
	spell.duration = spell.caster_level
		
	y =spell.caster.item_find_by_proto(4999)
	if spell.spell_level > 3 and y == OBJ_HANDLE_NULL:
		game.particles( 'sp-Shillelagh', spell.caster )	
		create_item_in_inventory(4999, spell.caster)		
		spell.num_of_targets =1
		spell.target_list[0].obj = spell.caster
		spell.caster.condition_add_with_args( 'sp-Magic Circle Outward', spell.id, spell.duration, 2 )
	else:
		if spell.spell_level < 4:
			spell.caster.float_mesfile_line('mes\\spell.mes', 16008)
		if y != OBJ_HANDLE_NULL:
			spell.caster.float_mesfile_line('mes\\spell.mes', 16007)	
		spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Holy Sword OnBeginRound"

def OnEndSpellCast( spell ):
	print "Holy Sword OnEndSpellCast"
	x = spell.caster.item_find_by_proto(4999)
	if x != OBJ_HANDLE_NULL:
		x.destroy()	
		
		