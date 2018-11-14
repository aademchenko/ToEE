from toee import *

def OnBeginSpellCast( spell ):
	print "Feeblemind OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Feeblemind OnSpellEffect"

	target = spell.target_list[0]

	if (target.obj.type == obj_t_pc) or (target.obj.type == obj_t_npc):

		if target.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

			# saving throw successful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			game.particles( 'Fizzle', target.obj )
			print "obj=", target.obj
			spell.target_list.remove_target( target.obj )

		else:

			# saving throw unsuccessful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			target.obj.float_mesfile_line( 'mes\\spell.mes', 20022 )
			target.obj.condition_add_with_args( 'sp-Feeblemind', spell.id, 0, 0 )
			target.partsys_id = game.particles( 'sp-Feeblemind', target.obj )

	else:

		spell.target.float_mesfile_line( 'mes\\spell.mes', 30000 )
		spell.target.float_mesfile_line( 'mes\\spell.mes', 31001 )

		game.particles( 'Fizzle', target.obj )
		spell.target_list.remove_target( target.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Feeblemind OnBeginRound"

def OnEndSpellCast( spell ):
	print "Feeblemind OnEndSpellCast"