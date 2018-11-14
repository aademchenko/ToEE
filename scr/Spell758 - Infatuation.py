from toee import *

def OnBeginSpellCast( spell ):
	print "Infatuation OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Infatuation OnSpellEffect"
	
	for target_item in spell.target_list:
		if not target_item.obj.is_friendly( spell.caster ) and target_item.obj.name != 14455:
			if (target_item.obj.type == obj_t_pc) or (target_item.obj.type == obj_t_npc):
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
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Infatuation OnBeginRound"

def OnEndSpellCast( spell ):
	print "Infatuation OnEndSpellCast"