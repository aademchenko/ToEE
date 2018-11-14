from toee import *

def OnBeginSpellCast( spell ):
	print "Animal Trance OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

	# HTN - sort the list by distance from caster
	spell.spell_target_list_sort( SORT_TARGET_LIST_BY_DIST_FROM_CASTER, SORT_TARGET_LIST_ORDER_ASCENDING )
	print "target_list sorted by dist from [", spell.caster, "] (closest to farthest): ", spell.target_list

def OnSpellEffect( spell ):
	print "Animal Trance OnSpellEffect"

	remove_list = []

	dice = dice_new( '2d6' )
	hd_remaining = dice.roll()
	spell.duration = 0

	# dire animal list includes 2 Dire Rats, Dire Bat, Dire Wolf, 2 Dire Lizards, 2 Dire Bears, 2 Dire Boars
	dire_list = [14056, 14390, 14391, 14450, 14506, 14507, 14978, 14979, 14981, 14998]
	dire_animal = 0

	spell.caster_partsys_id = game.particles( 'sp-Animal Trance', spell.caster )

	for target_item in spell.target_list:
		# check for dire animals
		for target in dire_list:
			if target == target_item.obj.name:
				dire_animal = 1

		obj_hit_dice = target_item.obj.hit_dice_num

		if (obj_hit_dice <= hd_remaining) and (target_item.obj.is_category_type( mc_type_animal ) or target_item.obj.is_category_type( mc_type_magical_beast )) and ((target_item.obj.stat_level_get( stat_intelligence ) == 1) or (target_item.obj.stat_level_get( stat_intelligence ) == 2)):
			hd_remaining = hd_remaining - obj_hit_dice

			# magical beasts and dire animals are allowed a saving throw; other animals are not
			if target_item.obj.is_category_type( mc_type_magical_beast ) or (dire_animal == 1):
				if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
					# saving throw successful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
					game.particles( 'Fizzle', target_item.obj )
					remove_list.append( target_item.obj )

				else:
					# saving throw unsuccessful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
					target_item.obj.condition_add_with_args( 'sp-Animal Trance', spell.id, spell.duration, 0 )
					game.particles( 'sp-Animal Trance-END', target_item.obj )

			else:
				# not a magical beast or a dire animal
				target_item.obj.condition_add_with_args( 'sp-Animal Trance', spell.id, spell.duration, 0 )
				game.particles( 'sp-Animal Trance-END', target_item.obj )

		else:
			game.particles( 'Fizzle', target_item.obj )
			remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Animal Trance OnBeginRound"

def OnEndSpellCast( spell ):
	print "Animal Trance OnEndSpellCast"