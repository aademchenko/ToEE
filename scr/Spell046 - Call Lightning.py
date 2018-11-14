from toee import *

def OnBeginSpellCast( spell ):
	print "Call Lightning OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Call Lightning OnSpellEffect"

	remove_list = []

	spell.duration = 10 * spell.caster_level

	# check if outdoors
	if ( game.is_outdoor() == 1 ):
		dam = dice_new( '3d10' )
	else:
		dam = dice_new( '3d6' )

	# play fx
	game.pfx_call_lightning( spell.target_loc, spell.target_loc_off_x, spell.target_loc_off_y, spell.target_loc_off_z )

	# damage all initial targets
	for target_item in spell.target_list:

		game.particles( 'sp-Call Lightning', target_item.obj )

		if target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_ELECTRICITY, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ) > 0:
			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
		else:
			# saving throw unsuccessful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

		remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	#spell.spell_end( spell.id )

	# add call-lightning condition, which allows additional bolts to be called
	spell.caster.condition_add_with_args( 'sp-Call Lightning', spell.id, spell.duration, (spell.caster_level - 1) )

def OnBeginRound( spell ):
	print "Call Lightning OnBeginRound"

def OnEndSpellCast( spell ):
	print "Call Lightning OnEndSpellCast"