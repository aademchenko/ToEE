from toee import *

def OnBeginSpellCast( spell ):
	print "Magic Vestment OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Magic Vestment OnSpellEffect"

	enhancement_bonus = spell.caster_level / 4

	spell.duration = 600 * spell.caster_level
	target_item = spell.target_list[0]

	if (target_item.obj.type == obj_t_armor) and ((target_item.obj.d20_query_has_spell_condition( sp_Magic_Vestment ) == 0)):

		target_item.obj.d20_status_init()
		target_item.obj.condition_add_with_args( 'sp-Magic Vestment', spell.id, spell.duration, enhancement_bonus )
		target_item.partsys_id = game.particles( 'sp-Detect Magic 2 Med', spell.caster )

	else:

		# not an item!
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30003 )

		game.particles( 'Fizzle', target_item.obj )
		spell.target_list.remove_target( target_item.obj )
		spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Magic Vestment OnBeginRound"

def OnEndSpellCast( spell ):
	print "Magic Vestment OnEndSpellCast"