from toee import *
from utilities import  * 
from Co8 import *

def OnBeginSpellCast( spell ):
	print "Healing Circle OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def OnSpellEffect ( spell ):
	check = 0
	check = check_for_protection_from_spells (spell.target_list, check)
	print "Healing Circle OnSpellEffect"

	remove_list = []

	dice = dice_new( '1d8' )
#	dice.bonus = min( 25, spell.caster.stat_level_get( spell.caster_class ) )
	dice.bonus = min( 25, spell.caster_level )

#	game.particles( 'sp-Healing Circle', spell.target_loc )

	for target_item in spell.target_list:

		game.particles( 'sp-Cure Light Wounds', target_item.obj )

		# heal allies, hurt undead
		if target_item.obj.is_category_type( mc_type_undead ):

			# allow Fortitude saving throw for half
			if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
				# saving throw succesful, damage target, 1/2 damage
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
	
				target_item.obj.spell_damage_with_reduction( spell.caster, D20DT_POSITIVE_ENERGY, dice, D20DAP_UNSPECIFIED, DAMAGE_REDUCTION_HALF, D20A_CAST_SPELL, spell.id )
			else:
				# saving throw unsuccesful, damage target, full damage
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
	
				target_item.obj.spell_damage( spell.caster, D20DT_POSITIVE_ENERGY, dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

		else:
			# heal allies
			target_item.obj.spell_heal( spell.caster, dice, D20A_CAST_SPELL, spell.id )


		remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	if check == 1:
		replace_protection_from_spells()
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Healing Circle OnBeginRound"

def OnEndSpellCast( spell ):
	print "Healing Circle OnEndSpellCast"