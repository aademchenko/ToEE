from toee import *
from utilities import  * 

def OnBeginSpellCast( spell ):
	print "Cure Moderate Wounds OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Cure Moderate Wounds OnSpellEffect"

#	Dar's level checks are no longer needed thanks to Spellslinger's dll fix
#	if spell.caster_class == 13: #added to check for proper paladin slot level (darmagon)
#		if spell.spell_level < 3:
#			spell.caster.float_mesfile_line('mes\\spell.mes', 16008)
#			spell.spell_end(spell.id)
#			return
#	if spell.caster_class == 14:
#		if spell.spell_level < 3:#added to check for proper ranger slot level (darmagon)
#			spell.caster.float_mesfile_line('mes\\spell.mes', 16008)
#			spell.spell_end(spell.id)
#			return
	

	npc = spell.caster			##  added so NPC's can use potion
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL and spell.caster_level <= 0:
		spell.caster_level = 7

	dice = dice_new( "2d8" )
	dice.bonus = min( 10, spell.caster_level )
	'''
	f=open("curefeedback.txt","w")
	f.write("bonus is "+str(dice.bonus) + "\n")
	
	f.write("caster is " +str(spell.caster)  + "\n")
	f.write("caster level is " + str(spell.caster_level) + "\n")
	f.write("Spell caster class is " + str(spell.caster_class) + "\n" ) # sometimes returns negative number when casting from Domain radial selection, or very large number for potions (but not always)
	f.write("spell.caster.stat_level_get(spell.caster_class) -> " +str(spell.caster.stat_level_get( spell.caster_class )) + "\n " )
	f.write("Spell variables are " + str(spell.variables) + "\n" ) # is empty here...
	f.close() '''
	
	target = spell.target_list[0].obj

	# check if target is friendly (willing target)
	if target.is_friendly( spell.caster ):

		# check if target is undead
		if target.is_category_type( mc_type_undead ):
			# check saving throw, damage target
			if target.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
				target.float_mesfile_line( 'mes\\spell.mes', 30001 )

				# saving throw succesful, damage target, 1/2 damage
				target.spell_damage_with_reduction( spell.caster, D20DT_POSITIVE_ENERGY, dice, D20DAP_UNSPECIFIED, DAMAGE_REDUCTION_HALF, D20A_CAST_SPELL, spell.id )
			else:
				target.float_mesfile_line( 'mes\\spell.mes', 30002 )

				# saving throw unsuccesful, damage target, full damage
				target.spell_damage( spell.caster, D20DT_POSITIVE_ENERGY, dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
		else:
			# heal target
			target.spell_heal( spell.caster, dice, D20A_CAST_SPELL, spell.id )
			target.healsubdual( spell.caster, dice, D20A_CAST_SPELL, spell.id )

	else:

		# check if target is undead
		if target.is_category_type( mc_type_undead ):
			# check saving throw, damage target
			if target.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
				target.float_mesfile_line( 'mes\\spell.mes', 30001 )

				# saving throw succesful, damage target, 1/2 damage
				target.spell_damage_with_reduction( spell.caster, D20DT_POSITIVE_ENERGY, dice, D20DAP_UNSPECIFIED, DAMAGE_REDUCTION_HALF, D20A_CAST_SPELL, spell.id )
			else:
				target.float_mesfile_line( 'mes\\spell.mes', 30002 )

				# saving throw unsuccesful, damage target, full damage
				target.spell_damage( spell.caster, D20DT_POSITIVE_ENERGY, dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
		else:
			# check saving throw
			if target.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
				#target.float_mesfile_line( 'mes\\spell.mes', 30001 )

				# saving throw succesful, heal target, 1/2 heal
				target.spell_heal( spell.caster, dice, D20A_CAST_SPELL, spell.id )
				target.healsubdual( spell.caster, dice, D20A_CAST_SPELL, spell.id )
			else:
				#target.float_mesfile_line( 'mes\\spell.mes', 30002 )

				# saving throw unsuccesful, heal target, full heal
				target.spell_heal( spell.caster, dice, D20A_CAST_SPELL, spell.id )
				target.healsubdual( spell.caster, dice, D20A_CAST_SPELL, spell.id )

	game.particles( 'sp-Cure Moderate Wounds', target )

	spell.target_list.remove_target( target )
	
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Cure Moderate Wounds OnBeginRound"

def OnEndSpellCast( spell ):
	print "Cure Moderate Wounds OnEndSpellCast"