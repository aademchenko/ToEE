from toee import *

def OnBeginSpellCast( spell ):
	print "Lesser Restoration OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Lesser Restoration OnSpellEffect"

	spell.duration = 0
	target_item = spell.target_list[0]

	abilityRestored = 1
	oldAbility = 0

	# get the ability type (from radial menu, -1 to offset index and D20Strength == 0)
	ability_type = (spell.spell_get_menu_arg( RADIAL_MENU_PARAM_MIN_SETTING ) - 1)

	## Solves Radial menu problem for Wands/NPCs
	#if ability_type != 0 and ability_type != 1 and ability_type != 2 and ability_type != 3 and ability_type != 4 and ability_type != 5:
	#	ability_type = game.random_range(1,6)
	#	ability_type = ability_type - 1

	if ability_type != 0 and ability_type != 1 and ability_type != 2 and ability_type != 3 and ability_type != 4 and ability_type != 5:
		ability_type = 0
		abilityRestored = 0

	# If no ability_type was selected, then that means that the spell used an item.  In this case, rather than picking a random item,
	# we cycle through all abilities until we find one that is actually healed.
	if target_item.obj.is_friendly( spell.caster ):
		target_item.partsys_id = game.particles( 'sp-Lesser Restoration', target_item.obj )
		if abilityRestored == 1:
			target_item.obj.condition_add_with_args( 'sp-Lesser Restoration', spell.id, spell.duration, ability_type )
		else:
			if abilityRestored == 0:
				ability_type = 0
				oldAbility = target_item.obj.stat_level_get(stat_strength)
				target_item.obj.condition_add_with_args( 'sp-Lesser Restoration', spell.id, spell.duration, ability_type )
				if target_item.obj.stat_level_get(stat_strength) > oldAbility:
					abilityRestored = 1
			if abilityRestored == 0:
				ability_type = 1
				oldAbility = target_item.obj.stat_level_get(stat_dexterity)
				target_item.obj.condition_add_with_args( 'sp-Lesser Restoration', spell.id, spell.duration, ability_type )
				if target_item.obj.stat_level_get(stat_dexterity) > oldAbility:
					abilityRestored = 1
			if abilityRestored == 0:
				ability_type = 2
				oldAbility = target_item.obj.stat_level_get(stat_constitution)
				target_item.obj.condition_add_with_args( 'sp-Lesser Restoration', spell.id, spell.duration, ability_type )
				if target_item.obj.stat_level_get(stat_constitution) > oldAbility:
					abilityRestored = 1
			if abilityRestored == 0:
				ability_type = 3
				oldAbility = target_item.obj.stat_level_get(stat_intelligence)
				target_item.obj.condition_add_with_args( 'sp-Lesser Restoration', spell.id, spell.duration, ability_type )
				if target_item.obj.stat_level_get(stat_intelligence) > oldAbility:
					abilityRestored = 1
			if abilityRestored == 0:
				ability_type = 4
				oldAbility = target_item.obj.stat_level_get(stat_wisdom)
				target_item.obj.condition_add_with_args( 'sp-Lesser Restoration', spell.id, spell.duration, ability_type )
				if target_item.obj.stat_level_get(stat_wisdom) > oldAbility:
					abilityRestored = 1
			if abilityRestored == 0:
				ability_type = 5
				oldAbility = target_item.obj.stat_level_get(stat_charisma)
				target_item.obj.condition_add_with_args( 'sp-Lesser Restoration', spell.id, spell.duration, ability_type )
				if target_item.obj.stat_level_get(stat_charisma) > oldAbility:
					abilityRestored = 1

	elif not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

		# saving throw unsuccesful
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

		target_item.obj.condition_add_with_args( 'sp-Lesser Restoration', spell.id, spell.duration, ability_type )
		target_item.partsys_id = game.particles( 'sp-Lesser Restoration', target_item.obj )

	else:

		# saving throw successful
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

		game.particles( 'Fizzle', target_item.obj )

	spell.target_list.remove_target( target_item.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Lesser Restoration OnBeginRound"

def OnEndSpellCast( spell ):
	print "Lesser Restoration OnEndSpellCast"