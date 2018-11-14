from toee import *

def OnBeginSpellCast( spell ):
	print "Unholy Blight OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Unholy Blight OnSpellEffect"

	remove_list = []
	
	npc = spell.caster
	if npc.name == 14958:  ## Nightwalker
		spell.dc = 18
		spell.caster_level = 21
	
	damage_dice = dice_new( '1d8' )
	if ( spell.caster_level >= 10 ):
		damage_dice.number = 5
	elif ( spell.caster_level >= 8 ):
		damage_dice.number = 4
	elif ( spell.caster_level >= 6 ):
		damage_dice.number = 3
	elif ( spell.caster_level >= 4 ):
		damage_dice.number = 2
	else:
		damage_dice.number = 1


		
	game.particles( 'sp-Unholy Blight', spell.target_loc )

	for target_item in spell.target_list:

		# roll possible stagger duration
		stagger_dice = dice_new( '1d4' )
		spell.duration = stagger_dice.roll()

		# check if target is GOOD
		alignment = target_item.obj.critter_get_alignment()
		if (alignment & ALIGNMENT_GOOD) or ( (alignment & ALIGNMENT_NEUTRAL) and not (alignment & ALIGNMENT_EVIL) ):

			# allow Fortitude saving throw for half
			if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
	
				# saving throw succesful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
	
				# half damage
				target_item.obj.spell_damage_with_reduction( spell.caster, D20DT_MAGIC, damage_dice, D20DAP_UNSPECIFIED, DAMAGE_REDUCTION_HALF, D20A_CAST_SPELL, spell.id )
	
				remove_list.append( target_item.obj )
	
			else:
				# saving throw unsuccesful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
	
				# full damage
				target_item.obj.spell_damage( spell.caster, D20DT_MAGIC, damage_dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
	
				# stagger the victim
				target_item.obj.condition_add_with_args( 'sp-Unholy Blight', spell.id, spell.duration, 0 )

		elif not (alignment & ALIGNMENT_GOOD) and not (alignment & ALIGNMENT_EVIL):

			remove_list.append( target_item.obj )

			# allow Fortitude saving throw for quarter
			if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
	
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