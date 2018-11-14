from toee import *

def OnBeginSpellCast( spell ):
	print "Animate Dead OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Animate Dead OnSpellEffect"

	spell.duration = 0

	target_item = spell.target_list[0]
	cast = spell.caster

	if cast.name == 8042:	
		for npc in game.obj_list_vicinity(cast.location, OLC_NPC):
			if npc not in game.party:
				if npc.stat_level_get(stat_hp_current) <= -10:
					target_item.obj = npc
					target_item.obj.condition_add_with_args( 'sp-Animate Dead', spell.id, spell.duration, 3 )
					target_item.partsys_id = game.particles( 'sp-Iuz Making Zombies', target_item.obj )
					zombie = game.obj_create( 14123, npc.location )

	if cast.name == 14425:	
		game.global_flags[811] = 0
		for obj in game.obj_list_vicinity(cast.location, OLC_CRITTERS):
			curr = obj.stat_level_get( stat_hp_current )
			if (curr <= -10 and obj.distance_to(cast) <= 10 and obj not in game.party and game.global_flags[811] == 0):
				if (obj.is_category_type( mc_type_humanoid ) or obj.is_category_type( mc_type_fey ) or obj.is_category_type( mc_type_giant ) or obj.is_category_type( mc_type_monstrous_humanoid )):
					target_item.obj = obj
					game.global_flags[811] = 1	

	# debit money (?)

	## Solves Radial menu problem for Wands/NPCs
	spell_arg = spell.spell_get_menu_arg( RADIAL_MENU_PARAM_MIN_SETTING )
	if spell_arg != 1 and spell_arg != 2:
		spell_arg = game.random_range(1,2)

	# make sure target is not already an undead
	if target_item.obj.stat_level_get( stat_hp_current ) >= -9:
		# not a animate-able
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30016 )
		game.particles( 'Fizzle', target_item.obj )

	elif target_item.obj.is_category_type( mc_type_humanoid ) or target_item.obj.is_category_type( mc_type_fey ) or target_item.obj.is_category_type( mc_type_giant ) or target_item.obj.is_category_type( mc_type_monstrous_humanoid ):
		if cast.name != 8042 and cast.name != 14425:
			target_item.obj.condition_add_with_args( 'sp-Animate Dead', spell.id, spell.duration, spell_arg )
			target_item.partsys_id = game.particles( 'sp-Animate Dead', target_item.obj )

		if cast.name == 14425:				
			target_item.obj.condition_add_with_args( 'sp-Animate Dead', spell.id, spell.duration, 3 )
			target_item.partsys_id = game.particles( 'sp-Animate Dead', target_item.obj )
			zombie = game.obj_create( 14619, target_item.obj.location )

	else:
		# not a animate-able
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31009 )
		game.particles( 'Fizzle', target_item.obj )

	spell.target_list.remove_target( target_item.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Animate Dead OnBeginRound"

def OnEndSpellCast( spell ):
	print "Animate Dead OnEndSpellCast"