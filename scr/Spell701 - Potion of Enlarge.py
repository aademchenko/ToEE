from toee import *

def OnBeginSpellCast( spell ):
	print "Potion of Enlarge OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Potion of Enlarge OnSpellEffect"

	spell.duration = 10 * spell.caster_level
	target_item = spell.target_list[0]

	if target_item.obj.is_friendly( spell.caster ):
		target_item.obj.condition_add_with_args( 'sp-Potion of Enlarge', spell.id, spell.duration, 0 )
		target_item.partsys_id = game.particles( 'sp-Enlarge', target_item.obj )
	else:
		if not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):

			# saving throw unsuccesful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			target_item.obj.condition_add_with_args( 'sp-Potion of Enlarge', spell.id, spell.duration, 0 )
			target_item.partsys_id = game.particles( 'sp-Enlarge', target_item.obj )

		else:

			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			game.particles( 'Fizzle', target_item.obj )
			spell.target_list.remove_target( target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Potion of Enlarge OnBeginRound"

def OnEndSpellCast( spell ):
	print "Potion of Enlarge OnEndSpellCast"