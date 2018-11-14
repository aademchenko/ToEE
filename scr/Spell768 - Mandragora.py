from toee import *

def OnBeginSpellCast( spell ):
	print "Mandragora OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Mandragora OnSpellEffect"

	remove_list = []

	spell.duration = 1 * spell.caster_level

	for target_item in spell.target_list:

		if not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
			# saving throw unsuccesful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			target_item.obj.condition_add_with_args( 'sp-Confusion', spell.id, spell.duration, 0 )
			target_item.partsys_id = game.particles( 'sp-Confusion Lesser', target_item.obj )
#			spell.target_list.remove_target( target_item.obj )
			remove_list.append( target_item.obj )

		else:
			# saving throw successful
			target_item.obj.condition_add_with_args( 'sp-True Seeing', spell.id, spell.duration, 0 )
			target_item.partsys_id = game.particles( 'sp-True Seeing', target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Mandragora OnBeginRound"
	range = 120
	for target_item in spell.target_list:

		print "target_list0 is=", target_item.obj
#		target_item.obj.float_mesfile_line('mes\\spell.mes', 25005, tf_red)
		# 40 == san_true_seeing
		if not target_item.obj.d20_query_has_spell_condition( sp_Confusion ):
#			target_item.obj.float_mesfile_line('mes\\spell.mes', 25007, tf_red)
			for obj in game.obj_list_cone( target_item.obj, OLC_CRITTERS, range, 0, 360 ):
				print "found obj=", obj
				if ( obj.object_script_execute( target_item.obj, 40 ) == SKIP_DEFAULT ):
					game.particles( 'Fizzle', obj )

def OnEndSpellCast( spell ):
	print "Mandragora OnEndSpellCast"