from toee import *

def OnBeginSpellCast( spell ):
	print "Mass Hold Monster OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Mass Hold Monster OnSpellEffect"

	spell.duration = 1 * spell.caster_level

	for target_item in spell.target_list:

		if (target_item.obj.type == obj_t_pc) or (target_item.obj.type == obj_t_npc):

			# allow Will saving throw to negate
			if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

				game.particles( 'Fizzle', target_item.obj )
				spell.target_list.remove_target( target_item.obj )
			else:
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

				# HTN - apply condition HOLD (paralyzed)
				target_item.obj.condition_add_with_args( 'sp-Hold Monster', spell.id, spell.duration, 0 )
				target_item.partsys_id = game.particles( 'sp-Hold Monster', target_item.obj )

		else:
			# not a critter
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31001 )

			game.particles( 'Fizzle', target_item.obj )
			spell.target_list.remove_target( target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Mass Hold Monster OnBeginRound"

def OnEndSpellCast( spell ):
	print "Mass Hold Monster OnEndSpellCast"