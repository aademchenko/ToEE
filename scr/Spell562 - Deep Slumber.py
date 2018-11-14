from toee import *

def OnBeginSpellCast( spell ):
	print "Deep Slumber OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

	# HTN - sort the list by hitdice
	spell.spell_target_list_sort( SORT_TARGET_LIST_BY_HIT_DICE_THEN_DIST, SORT_TARGET_LIST_ORDER_ASCENDING )
	print "target_list sorted by hitdice and dist from target_Loc (least to greatest): ", spell.target_list

def OnSpellEffect( spell ):
	print "Deep Slumber OnSpellEffect"

	remove_list = []

	spell.duration = 10 * spell.caster_level
	hit_dice_max = 10

	#print "Deep Slumber, can affect a total of (", hit_dice_max, ") HD"

	game.particles( 'sp-Deep Slumber', spell.target_loc )

	# get all targets in a 15ft radius
	for target_item in spell.target_list:

		# check critter_hit_dice
		obj_hit_dice = target_item.obj.hit_dice_num

		if (obj_hit_dice < 11) and (hit_dice_max >= obj_hit_dice):

			# subtract the obj.hit_dice from the max
			hit_dice_max = hit_dice_max - obj_hit_dice

			# allow Will saving throw to negate
			if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
	
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
	
				game.particles( 'Fizzle', target_item.obj )
				remove_list.append( target_item.obj )
	
			else:
	
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
				target_item.obj.condition_add_with_args( 'sp-Sleep', spell.id, spell.duration, 0 )

		else:

			game.particles( 'Fizzle', target_item.obj )
			remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Deep Slumber OnBeginRound"

def OnEndSpellCast( spell ):
	print "Deep Slumber OnEndSpellCast"