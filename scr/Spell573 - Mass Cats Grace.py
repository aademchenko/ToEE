from toee import *
from utilities import *

def OnBeginSpellCast( spell ):
	print "Mass Cats Grace OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Mass Cats Grace OnSpellEffect"

	dex_amount = 4
	spell.duration = 10 * spell.caster_level

	for target_item in spell.target_list:
		if target_item.obj.is_friendly( spell.caster ):
			target_item.obj.condition_add_with_args( 'sp-Cats Grace', spell.id, spell.duration, dex_amount )
			target_item.partsys_id = game.particles( 'sp-Cats Grace', target_item.obj )

		elif not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
			# saving throw unsuccesful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
			target_item.obj.condition_add_with_args( 'sp-Cats Grace', spell.id, spell.duration, dex_amount )
			target_item.partsys_id = game.particles( 'sp-Cats Grace', target_item.obj )

		else:
			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
			game.particles( 'Fizzle', target_item.obj )
	
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Mass Cats Grace OnBeginRound"

def OnEndSpellCast( spell ):
	print "Mass Cats Grace OnEndSpellCast"