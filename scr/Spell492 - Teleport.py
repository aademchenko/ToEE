from toee import *

def OnBeginSpellCast( spell ):
	print "Teleport OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Teleport OnSpellEffect"

	spell.duration = 0

	target_item = spell.target_list[0]

	# added for a form of movement barred by a Dimensional Anchor
	if target_item.obj.d20_query_has_spell_condition(sp_Dimensional_Anchor) == 1:
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30011 )
		game.particles( 'Fizzle', target_item.obj )

	else:
		game.particles( 'sp-Teleport', target_item.obj )
		game.ui_show_worldmap( worldmap_ui_f_spell_teleport )

	spell.target_list.remove_target( target_item.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Teleport OnBeginRound"

def OnEndSpellCast( spell ):
	print "Teleport OnEndSpellCast"