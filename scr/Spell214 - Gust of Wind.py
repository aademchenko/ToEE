from toee import *

def OnBeginSpellCast( spell ):
	print "Gust of Wind OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Gust of Wind OnSpellEffect"

	remove_list = []

	spell.duration = 1

	game.particles( 'sp-Gust of Wind', spell.caster )

	for target_item in spell.target_list:

		if not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

			# saving throw unsuccesful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			target_item.obj.condition_add_with_args( 'sp-Gust of Wind', spell.id, spell.duration, 0 )
			target_item.partsys_id = game.particles( 'sp-Gust of Wind', target_item.obj )

		else:

			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			game.particles( 'Fizzle', target_item.obj )
			remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Gust of Wind OnBeginRound"

def OnEndSpellCast( spell ):
	print "Gust of Wind OnEndSpellCast"