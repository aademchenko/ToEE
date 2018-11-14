from toee import *

def OnBeginSpellCast( spell ):
	print "Sound Burst OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Sound Burst OnSpellEffect"

	remove_list = []

	spell.duration = 0
	dam = dice_new( '1d8' )

	game.particles( 'sp-Sound Burst', spell.target_loc )
	for target_item in spell.target_list:

		target_item.obj.spell_damage( spell.caster, D20DT_SONIC, dam, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

		if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
			remove_list.append( target_item.obj )
		else:
			# saving throw unsuccessful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			target_item.obj.condition_add_with_args( 'sp-Sound Burst', spell.id, 1, 0 )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Sound Burst OnBeginRound"

def OnEndSpellCast( spell ):
	print "Sound Burst OnEndSpellCast"