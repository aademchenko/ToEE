from toee import *

def OnBeginSpellCast( spell ):
	print "Blur OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-illusion-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Blur OnSpellEffect"

	concealment_bonus = 20
	spell.duration = 10 * spell.caster_level
	target_item = spell.target_list[0]

	if target_item.obj.is_friendly( spell.caster ):

		target_item.obj.condition_add_with_args( 'sp-Blur', spell.id, spell.duration, concealment_bonus )
		target_item.partsys_id = game.particles( 'sp-Blur', target_item.obj )

	else:

		if (target_item.obj.type == obj_t_pc) or (target_item.obj.type == obj_t_npc):

			# allow Will saving throw to negate
			if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

				game.particles( 'Fizzle', target_item.obj )
				spell.target_list.remove_target( target_item.obj )
			else:
				# saving throw unsuccessful
				target_item.obj.condition_add_with_args( 'sp-Blur', spell.id, spell.duration, concealment_bonus )
				target_item.partsys_id = game.particles( 'sp-Blur', target_item.obj )
		else:
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31001 )

			game.particles( 'Fizzle', target_item.obj )
			spell.target_list.remove_target( target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Blur OnBeginRound"

def OnEndSpellCast( spell ):
	print "Blur OnEndSpellCast"