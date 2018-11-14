from toee import *

def OnBeginSpellCast( spell ):
	print "Unholy Blight OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Unholy Blight OnSpellEffect"

	remove_list = []

	damage_dice = dice_new( '1d8' )
	damage_dice.number = min( 5, spell.caster_level / 2 )
	damage2_dice = dice_new( '1d6' )
	damage2_dice.number = min( 10, spell.caster_level )

	game.particles( 'sp-Unholy Blight', spell.target_loc )

	for target_item in spell.target_list:

		# roll possible sicken duration
		sicken_dice = dice_new( '1d4' )
		spell.duration = sicken_dice.roll()

		# check if target is EVIL
		alignment = target_item.obj.critter_get_alignment()
		if not (alignment & ALIGNMENT_EVIL):

			# check if target is GOOD or NEUTRAL
			if (alignment & ALIGNMENT_GOOD):

				# allow Will saving throw for half
				if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

					# saving throw succesful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

					# half damage
					# check for outsiders
					if target_item.obj.is_category_type( mc_type_outsider ):
						target_item.obj.spell_damage_with_reduction( spell.caster, D20DT_MAGIC, damage2_dice, D20DAP_UNSPECIFIED, DAMAGE_REDUCTION_HALF, D20A_CAST_SPELL, spell.id )
					else:
						target_item.obj.spell_damage_with_reduction( spell.caster, D20DT_MAGIC, damage_dice, D20DAP_UNSPECIFIED, DAMAGE_REDUCTION_HALF, D20A_CAST_SPELL, spell.id )

				else:
					# saving throw unsuccesful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

					# full damage
					# check for outsiders
					if target_item.obj.is_category_type( mc_type_outsider ):
						target_item.obj.spell_damage( spell.caster, D20DT_MAGIC, damage2_dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
					else:
						target_item.obj.spell_damage( spell.caster, D20DT_MAGIC, damage_dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

					# sicken the victim
					target_item.obj.condition_add_with_args( 'sp-Unholy Blight', spell.id, spell.duration, 0 )

			else:

				# allow Will saving throw for quarter
				if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

					# saving throw succesful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

					# quarter damage
					target_item.obj.spell_damage_with_reduction( spell.caster, D20DT_MAGIC, damage_dice, D20DAP_UNSPECIFIED, DAMAGE_REDUCTION_QUARTER, D20A_CAST_SPELL, spell.id )

				else:
					# saving throw unsuccesful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

					# half damage
					target_item.obj.spell_damage_with_reduction( spell.caster, D20DT_MAGIC, damage_dice, D20DAP_UNSPECIFIED, DAMAGE_REDUCTION_HALF, D20A_CAST_SPELL, spell.id )

					# do NOT sicken the victim
					#target_item.obj.condition_add_with_args( 'sp-Unholy Blight', spell.id, spell.duration, 0 )

		else:
			# don't affect EVIL
			game.particles( 'Fizzle', target_item.obj )

		remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Unholy Blight OnBeginRound"

def OnEndSpellCast( spell ):
	print "Unholy Blight OnEndSpellCast"