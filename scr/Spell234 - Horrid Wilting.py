from toee import *

def OnBeginSpellCast( spell ):
	print "Horrid Wilting OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Horrid Wilting OnSpellEffect"

	remove_list = []

	dam = dice_new( '1d6' )
	dam.number = min( 20, spell.caster_level )
	plant_dam = dice_new ( '1d8' )
	plant_dam.number = min( 20, spell.caster_level )

	for target_item in spell.target_list:

		game.particles( 'sp-Blight', target_item.obj )
		# Plants and water elementals take 1d8 damage per caster level, save for half
		if (target_item.obj.is_category_type(mc_type_plant)) or ((target_item.obj.is_category_type(mc_type_elemental)) and (target_item.obj.is_category_subtype(mc_subtype_water))):
			if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
				target_item.obj.spell_damage_with_reduction( spell.caster, D20DT_UNSPECIFIED, plant_dam, D20DAP_UNSPECIFIED, DAMAGE_REDUCTION_HALF, D20A_CAST_SPELL, spell.id )
			else:
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
				target_item.obj.spell_damage( spell.caster, D20DT_UNSPECIFIED, plant_dam, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

		# Everybody else takes 1d6 damage per caster level, save for half
		else:
			if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
				target_item.obj.spell_damage_with_reduction( spell.caster, D20DT_UNSPECIFIED, dam, D20DAP_UNSPECIFIED, DAMAGE_REDUCTION_HALF, D20A_CAST_SPELL, spell.id )
			else:
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
				target_item.obj.spell_damage( spell.caster, D20DT_UNSPECIFIED, dam, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

		remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Horrid Wilting OnBeginRound"

def OnEndSpellCast( spell ):
	print "Horrid Wilting OnEndSpellCast"