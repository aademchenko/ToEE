from toee import *
from utilities import  * 

def OnBeginSpellCast( spell ):
	print "Summoning Surge OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def OnSpellEffect ( spell ):
	print "Summoning Surge OnSpellEffect"

	str_amount = 4
	spell.duration = 1 * spell.caster_level
	

#	game.particles( 'sp-Mass Bulls Strength', spell.target_loc )

	for target_item in spell.target_list:
		
		if target_item.obj.is_friendly( spell.caster ):
#			target_item.obj.float_mesfile_line('mes\\spell.mes', 25005, tf_red)
			if target_item.obj.d20_query_has_spell_condition( sp_Summoned ):
#				target_item.obj.float_mesfile_line('mes\\spell.mes', 25007, tf_red)
				target_item.obj.condition_add_with_args( 'sp-Bulls Strength', spell.id, spell.duration, str_amount )
				target_item.partsys_id = game.particles( 'sp-Bullstrength', target_item.obj )

	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Summoning Surge OnBeginRound"

def OnEndSpellCast( spell ):
	print "Summoning Surge OnEndSpellCast"