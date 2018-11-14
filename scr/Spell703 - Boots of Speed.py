from toee import *

def OnBeginSpellCast( spell ):
	print "Boots of Speed OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Boots of Speed OnSpellEffect"

	remove_list = []

	spell.duration = 0
	print "spell.duration = ", spell.duration

	for target_item in spell.target_list:

		if target_item.obj.is_friendly( spell.caster ):
			return_val = target_item.obj.condition_add_with_args( 'sp-Haste', spell.id, spell.duration, 1 )
			target_item.partsys_id = game.particles( 'sp-Haste', target_item.obj )

			# dont allow multiple adds (WIP! - until intgame select prevents MULTI (same target)
			if return_val == 0:
				remove_list.append( target_item.obj )

		else:
			if not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
	
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

				return_val = target_item.obj.condition_add_with_args( 'sp-Boots of Speed', spell.id, spell.duration, 1 )
				target_item.partsys_id = game.particles( 'sp-Haste', target_item.obj )

				# dont allow multiple adds (WIP! - until intgame select prevents MULTI (same target)
				if return_val == 0:
					remove_list.append( target_item.obj )
	
			else:
	
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

				game.particles( 'Fizzle', target_item.obj )
				remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Boots of Speed OnBeginRound"

def OnEndSpellCast( spell ):
	print "Boots of Speed OnEndSpellCast"