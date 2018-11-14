from toee import *

def OnBeginSpellCast( spell ):
	print "Blink OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Blink OnSpellEffect"

	spell.duration = 1 * spell.caster_level
	target_item = spell.target_list[0]

	# added for a form of movement barred by a Dimensional Anchor
	if target_item.obj.d20_query_has_spell_condition(sp_Dimensional_Anchor) == 1:
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30011 )
		game.particles( 'Fizzle', target_item.obj )

	else:
		target_item.obj.condition_add_with_args( 'sp-Blink', spell.id, spell.duration, 242 )
		target_item.partsys_id = game.particles( 'sp-Blink', target_item.obj )

def OnBeginRound( spell ):
	print "Blink OnBeginRound"

def OnEndSpellCast( spell ):
	print "Blink OnEndSpellCast"