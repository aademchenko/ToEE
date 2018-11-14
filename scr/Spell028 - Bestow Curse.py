from toee import *

def OnBeginSpellCast( spell ):
	print "Bestow Curse OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Bestow Curse OnSpellEffect"

	spell.duration = 0
	target_item = spell.target_list[0]

	## Solves Radial menu problem for Wands/NPCs
	spell_arg = spell.spell_get_menu_arg( RADIAL_MENU_PARAM_MIN_SETTING )
	if spell_arg != 1 and spell_arg != 2 and spell_arg != 3 and spell_arg != 4 and spell_arg != 5 and spell_arg != 6 and spell_arg != 7 and spell_arg != 8:
		spell_arg = game.random_range(1,8)

	npc = spell.caster
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL:
		spell_arg = 8

	# allow Willpower saving throw to negate
	if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
		# saving throw successful
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
		game.particles( 'Fizzle', target_item.obj )
		spell.target_list.remove_target( target_item.obj )

	else:
		# saving throw unsuccessful
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
		target_item.partsys_id = game.particles( 'sp-Bestow Curse', target_item.obj )

		if spell_arg == 1:
			#print "str"
			# apply ability damage str
			target_item.obj.condition_add_with_args( 'sp-Bestow Curse Ability', spell.id, spell.duration, 0 )

		elif spell_arg == 2:
			# apply ability damage dex
			target_item.obj.condition_add_with_args( 'sp-Bestow Curse Ability', spell.id, spell.duration, 1 )

		elif spell_arg == 3:
			# apply ability damage con
			target_item.obj.condition_add_with_args( 'sp-Bestow Curse Ability', spell.id, spell.duration, 2 )

		elif spell_arg == 4:
			# apply ability damage int
			target_item.obj.condition_add_with_args( 'sp-Bestow Curse Ability', spell.id, spell.duration, 3 )

		elif spell_arg == 5:
			# apply ability damage wis
			target_item.obj.condition_add_with_args( 'sp-Bestow Curse Ability', spell.id, spell.duration, 4 )

		elif spell_arg == 6:
			# apply ability damage cha
			target_item.obj.condition_add_with_args( 'sp-Bestow Curse Ability', spell.id, spell.duration, 5 )

		elif spell_arg == 7:
			# apply curse rolls/checks
			target_item.obj.condition_add_with_args( 'sp-Bestow Curse Rolls', spell.id, spell.duration, 6 )

		elif spell_arg == 8:
			# apply curse actions
			target_item.obj.condition_add_with_args( 'sp-Bestow Curse Actions', spell.id, spell.duration, 7 )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Bestow Curse OnBeginRound"

def OnEndSpellCast( spell ):
	print "Bestow Curse OnEndSpellCast"