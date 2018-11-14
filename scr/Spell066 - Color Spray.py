from toee import *

def OnBeginSpellCast( spell ):
	print "Color Spray OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-illusion-conjure", spell.caster )

	dice = dice_new( '1d6' )
	num_targets_affected = dice.roll()
	print "num_of_targets_affected=", num_targets_affected

	# HTN - sort the list by distance from caster
	spell.spell_target_list_sort( SORT_TARGET_LIST_BY_DIST_FROM_CASTER, SORT_TARGET_LIST_ORDER_ASCENDING )
	print "target_list sorted by dist from [", spell.caster, "] (closest to farthest): ", spell.target_list

	# remove targets greater than num_affected
	if spell.num_of_targets > num_targets_affected:
		remove_list = []
		index = 0

		for target_item in spell.target_list:
			if index >= num_targets_affected:
				remove_list.append( target_item.obj )
			index = index + 1

		spell.target_list.remove_list( remove_list )

	print "target_list after pruning: ", spell.target_list

def OnSpellEffect( spell ):
	print "Color Spray OnSpellEffect"

	remove_list = []

	spell.duration = 0

	game.particles( 'sp-Color Spray', spell.caster )

	for target_item in spell.target_list:
		if target_item.obj.d20_query( Q_Critter_Is_Blinded ) == 0:
			if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
				game.particles( 'Fizzle', target_item.obj )
				remove_list.append( target_item.obj )

			else:
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

				if target_item.obj.hit_dice_num >= 5:
					target_item.obj.condition_add_with_args( 'sp-Color Spray Stun', spell.id, spell.duration, 0 )

				elif target_item.obj.hit_dice_num >= 3:
					target_item.obj.condition_add_with_args( 'sp-Color Spray Blind', spell.id, spell.duration, 0 )

				else:
					target_item.obj.condition_add_with_args( 'sp-Color Spray Unconscious', spell.id, spell.duration, 0 )

		else:
			game.particles( 'Fizzle', target_item.obj )
			remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Color Spray OnBeginRound"

def OnEndSpellCast( spell ):
	print "Color Spray OnEndSpellCast"