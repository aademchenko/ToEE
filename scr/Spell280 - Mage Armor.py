from toee import *

def OnBeginSpellCast( spell ):
	print "Mage Armor OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Mage Armor OnSpellEffect"

	armor_bonus = 4
	spell.duration = 600 * spell.caster_level

	target = spell.target_list[0]

	# check if target is friendly (willing target)
	if target.obj.is_friendly( spell.caster ):

			# HTN - WIP! this needs to be changed to a 'force_armor_bonus' that doesn't stack 
			# 	with 'armor_bonus' (in addition, we need to allow non-corporeal monsters 
			#	to pass thru squares occupied by people without 'force_armor')
			target.obj.condition_add_with_args( 'sp-Mage Armor', spell.id, spell.duration, armor_bonus )
			target.partsys_id = game.particles( 'sp-Mage Armor', target.obj )

	else:

		# allow Will saving throw to negate
		if target.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
			# saving throw successful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			game.particles( 'Fizzle', target.obj )
			spell.target_list.remove_target( target.obj )
		else:
			# saving throw unsuccessful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			# HTN - WIP! this needs to be changed to a 'force_armor_bonus' that doesn't stack 
			# 	with 'armor_bonus' (in addition, we need to allow non-corporeal monsters 
			#	to pass thru squares occupied by people without 'force_armor')
			target.obj.condition_add_with_args( 'sp-Mage Armor', spell.id, spell.duration, armor_bonus )
			target.partsys_id = game.particles( 'sp-Mage Armor', target.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Mage Armor OnBeginRound"

def OnEndSpellCast( spell ):
	print "Mage Armor OnEndSpellCast"
