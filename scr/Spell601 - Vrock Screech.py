from toee import *

def OnBeginSpellCast( spell ):
	print "Vrock Screech OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level

def	OnSpellEffect( spell ):
	print "Vrock Screech OnSpellEffect"

	remove_list = []

	spell.duration = 1
	spell.dc = 22
	game.particles( 'Mon-Vrock-Screech', spell.caster )

	for target_item in spell.target_list:

		print "target=", target_item.obj
		tar = target_item.obj
		if tar.name == 14258 or tar.name == 14110 or tar.name == 14259 or tar.name == 14263 or tar.name == 14286 or tar.name == 14358 or tar.name == 14357 or tar.name == 14360 or tar.name == 14361:
##		if target_item.obj.is_category_type( mc_subtype_demon ):
			remove_list.append( target_item.obj )

		elif not target_item.obj.saving_throw( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, D20A_CAST_SPELL ):

			# saving throw unsuccessful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 20021 )

			target_item.obj.condition_add_with_args( 'sp-Vrock Screech', spell.id, spell.duration, 0 )
			target_item.partsys_id = game.particles( 'Mon-Vrock-Screech-Hit', target_item.obj )

		else:

			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			game.particles( 'Fizzle', target_item.obj )
			remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Vrock Screech OnBeginRound"

def OnEndSpellCast( spell ):
	print "Vrock Screech OnEndSpellCast"