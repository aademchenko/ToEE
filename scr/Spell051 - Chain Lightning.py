from toee import *

def OnBeginSpellCast( spell ):
	print "Chain Lightning OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Chain Lightning OnSpellEffect"

	remove_list = []

	primary_damage_dice = dice_new( '1d6' )
	primary_damage_dice.number = min( 1 * spell.caster_level, 20 )

	secondary_damage_dice = dice_new( '1d6' )
	secondary_damage_dice.number = min( 1 * (spell.caster_level / 2), 20 )

	game.particles( 'sp-Chain Lightning', spell.target_loc )
	game.pfx_chain_lightning( spell.caster, spell.num_of_targets, spell.target_list )

	i = 0
	for target_item in spell.target_list:

		if ( i == 0 ):
			i = 1
			if target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, primary_damage_dice, D20DT_ELECTRICITY, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ) > 0:
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
			else:
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
		else:
			if target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, secondary_damage_dice, D20DT_ELECTRICITY, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ) > 0:
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
			else:
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

		remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Chain Lightning OnBeginRound"

def OnEndSpellCast( spell ):
	print "Chain Lightning OnEndSpellCast"