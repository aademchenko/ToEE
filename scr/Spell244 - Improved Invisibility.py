from toee import *

def OnBeginSpellCast( spell ):
	print "Improved Invisibility OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-illusion-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Improved Invisibility OnSpellEffect"

	target = spell.target_list[0]

	spell.duration = 1 * spell.caster_level

	npc = spell.caster			##  added so NPC's can use wand/potion/scroll
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL and spell.duration <= 0:
		spell.duration = 10
		spell.caster_level = 10

	# check if target is friendly (willing target)
	if target.obj.is_friendly( spell.caster ):

		# HTN - apply condition INVISIBLE
		if (target.obj.type == obj_t_pc) or (target.obj.type == obj_t_npc):
			target.obj.condition_add_with_args( 'sp-Improved Invisibility', spell.id, spell.duration, 0 )
			target.partsys_id = game.particles( 'sp-Improved Invisibility', target.obj )
		else:
			# invalid target
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
			target.obj.float_mesfile_line( 'mes\\spell.mes', 31001 )

			game.particles( 'Fizzle', target.obj )
			spell.target_list.remove_target( target.obj )

	else:

		# HTN - apply condition INVISIBLE
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

				target.obj.condition_add_with_args( 'sp-Improved Invisibility', spell.id, spell.duration, 0 )
				target.partsys_id = game.particles( 'sp-Improved Invisibility', target.obj )
		else:
			# invalid target
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
			target.obj.float_mesfile_line( 'mes\\spell.mes', 31001 )

			game.particles( 'Fizzle', target.obj )
			spell.target_list.remove_target( target.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Improved Invisibility OnBeginRound"

def OnEndSpellCast( spell ):
	print "Improved Invisibility OnEndSpellCast"