from toee import *

def OnBeginSpellCast( spell ):
	print "Hold Monster OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Hold Monster OnSpellEffect"

	npc = spell.caster		
	if npc.name == 14359:	## Glabrezu Guardian 	
		spell.dc = 20

	spell.duration = 1 * spell.caster_level

	target = spell.target_list[0]

	if (target.obj.type == obj_t_pc) or (target.obj.type == obj_t_npc):

		# allow Will saving throw to negate
		if target.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
			# saving throw successful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			game.particles( 'Fizzle', target.obj )
			spell.target_list.remove_target( target.obj )
		else:
			# saving throw unsuccessful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			# HTN - apply condition HOLD (paralyzed)
			target.obj.condition_add_with_args( 'sp-Hold Monster', spell.id, spell.duration, 0 )
			target.partsys_id = game.particles( 'sp-Hold Monster', target.obj )

	else:
		# not a critter
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 31001 )

		game.particles( 'Fizzle', target.obj )
		spell.target_list.remove_target( target.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Hold Monster OnBeginRound"

def OnEndSpellCast( spell ):
	print "Hold Monster OnEndSpellCast"