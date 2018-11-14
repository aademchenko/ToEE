from toee import *

from Co8 import *

def OnBeginSpellCast( spell ):
	print "Enslavement OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Enslavement OnSpellEffect"
	
	npc = spell.caster
	target_item = spell.target_list[0]
	
	if not target_item.obj.is_friendly( spell.caster ) and target_item.obj.name != 14455:
		if (target_item.obj.type == obj_t_pc) or (target_item.obj.type == obj_t_npc):
			if not ( spell.caster.follower_atmax() ):
				spell.caster.follower_add( target_item.obj )
			else:
				spell.caster.ai_follower_add( target_item.obj )
			# add target to initiative, just in case
			target_item.obj.add_to_initiative()
			game.update_combat_ui()
		else:
			# not a person
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31001 )
			game.particles( 'Fizzle', target_item.obj )
			spell.target_list.remove_target( target_item.obj )
	else:
		# can't target friendlies
		game.particles( 'Fizzle', target_item.obj )
		spell.target_list.remove_target( target_item.obj )
		
	End_Spell(spell)
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Enslavement OnBeginRound"

def OnEndSpellCast( spell ):
	print "Enslavement OnEndSpellCast"