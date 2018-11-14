from toee import *
from utilities import location_from_axis, location_to_axis

def OnBeginSpellCast( spell ):
	print "Sunburst OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Sunburst OnSpellEffect"

	game.particles( 'sp-Fireball-conjure', spell.caster )

def OnBeginRound( spell ):
	print "Sunburst OnBeginRound"

def OnBeginProjectile( spell, projectile, index_of_target ):
	print "Sunburst OnBeginProjectile"

	projectile.obj_set_int( obj_f_projectile_part_sys_id, game.particles( 'sp-Searing Light', projectile ) )

def OnEndProjectile( spell, projectile, index_of_target ):
	print "Sunburst OnEndProjectile"

	game.particles( 'sp-Sunburst', spell.target_loc )

	remove_list = []

	spell.duration = 100 * spell.caster_level
	dam = dice_new( '1d6' )
	dam2 = dice_new( '6d6' )
	dam.number = min( 25, spell.caster_level )

	# game.particles_end( projectile.obj_get_int( obj_f_projectile_part_sys_id ) )

	for target_item in spell.target_list:

		game.particles( 'sp-Searing Light-Hit', target_item.obj )
		if target_item.obj.is_category_type( mc_type_undead ) or target_item.obj.is_category_type( mc_type_plant ) or target_item.obj.is_category_type( mc_type_ooze ):

			if target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_POSITIVE_ENERGY, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ):
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
			else:
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
				target_item.obj.condition_add_with_args( 'sp-Glitterdust Blindness', spell.id, spell.duration, 0 )

				# destruction of any undead creature specifically harmed by bright light if it fails its save
				# vulnerability to sunlight: Bodak	aversion to daylight: Nightwalker	sunlight or daylight powerlessness: none
				undead_list = [14328, 14958]
				for undead in undead_list:
					if undead == target_item.obj.name:
						target_item.obj.float_mesfile_line( 'mes\\combat.mes', 7000 )
						target_item.obj.critter_kill_by_effect()

		else:

			light_sensitive = 0
			# a creature to which sunlight is harmful or unnatural takes double damage
			# light sensitivity: orcs, half-orcs and kobolds	light blindness: drow (and that drow ranger too!)
			if target_item.obj.is_category_subtype( mc_subtype_orc ) or target_item.obj.is_category_subtype( mc_subtype_half_orc ) or (is_kobold(target_item.obj) == 1) or (is_drow(target_item.obj) == 1):
				light_damage = dam2.number
				dam2.number = dam2.number * 2
				light_sensitive = 1

			if target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam2, D20DT_MAGIC, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ):
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
			else:
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
				target_item.obj.condition_add_with_args( 'sp-Glitterdust Blindness', spell.id, spell.duration, 0 )

			if light_sensitive == 1:
				dam2.number = light_damage

		remove_list.append( target_item.obj )
	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnEndSpellCast( spell ):
	print "Sunburst OnEndSpellCast"

def is_kobold( target ):
	print "is_kobold"

	# all kobolds are the humanoid type, the reptilian subtype, are small, and have the alertness feat

	if target.is_category_type( mc_type_humanoid ) and target.is_category_subtype( mc_subtype_reptilian ):
		if target.get_size == STAT_SIZE_SMALL:
			if target.has_feat(feat_alertness):
				return 1
	return 0

def is_drow( target ):
	print "is_drow"

	# all drow are elvish npcs with white hair, with spell resistance, that usually worship Lolth, and that usually are evil

	hair_list = [906, 922, 938, 954, 970, 986, 1002, 1018, 898, 914, 930, 946, 962, 978, 994, 1010]		## white hair (for elves)
	hair_style = target.obj_get_int(obj_f_critter_hair_style)
	alignment = target.critter_get_alignment()

	if target.type == obj_t_npc:
		if (target.stat_level_get(stat_race) == 2) or target.is_category_subtype( mc_subtype_elf ):	## that drow ranger does NOT have a subtype of 'mc_subtype_elf'!
			for hair_color in hair_list:
				if hair_color == hair_style:
					if target.stat_level_get(stat_deity) == 23:	## Lolth (but of course!)
						return 1
					elif target.d20_query(Q_Critter_Has_Spell_Resistance) == 1:	## check critter Spell Resistance (drow have 'Monster Spell Resistance')
						if SR_status(target) == 0:		## check if Spell Resistance is from a condition or item (not really necessary for NPCs, but check just in case!)
							return 1
					elif (alignment & ALIGNMENT_EVIL):		## not perfect, but evil elvish npcs with white hair should count for something!
						return 1
	return 0

def SR_status( target ):
	print "SR_status"

	# conditions that give Spell Resistance

	# if target.d20_query_has_spell_condition(sp_Spell_Resistance) == 1:	## check for Spell Resistance spell:  DOES NOT WORK!  Needs a fix.
		# return 1
	# if target.has_feat(feat_diamond_soul):			## check for Diamond Soul feat for monks:  DOES NOT WORK!
		# return 1
	if target.stat_level_get(stat_level_monk) >= 13:		## Monk fix
		return 1
	elif (target.item_worn_at(3).name == 4999) or (target.item_worn_at(4).name == 4999):	## Paladin Holy Sword
		return 1
	elif target.item_worn_at(1).name == 12669:			## Scarab of Protection
		return 1
	elif target.item_worn_at(12) != OBJ_HANDLE_NULL:
		robe_list = [6219, 6401, 6402, 6403]			## Senshock's Robes and Robes of the Archmagi
		robe_name = target.item_worn_at(12).name
		for robe in robe_list:
			if robe == robe_name:
				return 1
	elif target.item_worn_at(10) != OBJ_HANDLE_NULL:
		cape_list = [6286, 6345, 6714, 6715, 6716, 6717]	## Mantles of Spell Resistance
		cape_name = target.item_worn_at(10).name
		for cape in cape_list:
			if cape == cape_name:
				return 1
	# elif target.item_worn_at(5) != OBJ_HANDLE_NULL:		## Need help to add armor crafted with Spell Resistance!
		# armor_worn = target.item_worn_at(5)
		# return 1
	return 0
