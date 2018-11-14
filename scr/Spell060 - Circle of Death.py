from toee import *

def OnBeginSpellCast( spell ):
	print "Circle of Death OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

	# Sorts the targets by hit dice, so lowest hit dice are affected first
	spell.spell_target_list_sort( SORT_TARGET_LIST_BY_HIT_DICE_THEN_DIST, SORT_TARGET_LIST_ORDER_ASCENDING )
	print "target_list sorted by hitdice and dist from target_Loc (least to greatest): ", spell.target_list

def OnSpellEffect ( spell ):
	print "Circle of Death OnSpellEffect"

	remove_list = []

	kill_roll = dice_new( '1d4' )
	kill_roll.num = min( 20, spell.caster_level )
	hit_dice_max = kill_roll.roll()

	for target_item in spell.target_list:

		obj_hit_dice = target_item.obj.hit_dice_num

		# Only works on creatures of less than 9 hit dice, and not on undead or constructs
		if (obj_hit_dice < 9) and (hit_dice_max >= obj_hit_dice) and not(target_item.obj.is_category_type(mc_type_undead)) and not(target_item.obj.is_category_type(mc_type_construct)):

			hit_dice_max = hit_dice_max - obj_hit_dice

			# allow Fortitude saving throw to negate
			if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
	
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
				game.particles( 'Fizzle', target_item.obj )

			else:
	
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
				# So you'll get awarded XP for the kill
				if not target_item.obj in game.leader.group_list():
					target_item.obj.damage( game.leader , D20DT_UNSPECIFIED, dice_new( "1d1" ) )
				target_item.obj.critter_kill_by_effect()
				game.particles( 'sp-Slay Living', target_item.obj )

		remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Circle of Death OnBeginRound"

def OnEndSpellCast( spell ):
	print "Circle of Death OnEndSpellCast"