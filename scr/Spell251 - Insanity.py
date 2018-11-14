from toee import *

def OnBeginSpellCast( spell ):
	print "Insanity OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Insanity OnSpellEffect"

	spell.duration = 9999999

	target_item = spell.target_list[0]

	if not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

		# saving throw unsuccesful
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

		target_item.obj.condition_add_with_args( 'sp-Confusion', spell.id, spell.duration, 0 )
		target_item.partsys_id = game.particles( 'sp-Confusion-Hit', target_item.obj )

	else:

		# saving throw successful
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

		game.particles( 'Fizzle', target_item.obj )
		spell.target_list.remove_target( target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Insanity OnBeginRound"

def OnEndSpellCast( spell ):
	print "Insanity OnEndSpellCast"