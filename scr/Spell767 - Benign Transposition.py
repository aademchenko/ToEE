from toee import *
from utilities import *

def OnBeginSpellCast( spell ):
	print "Benign Transposition OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Benign Transposition OnSpellEffect"

	target_1 = spell.target_list[0]
	target_2 = spell.target_list[1]

	loc_1 = target_1.obj.location
	loc_2 = target_2.obj.location

	size_1 = target_1.obj.get_size
	size_2 = target_2.obj.get_size

	if (target_1.obj.d20_query_has_spell_condition( sp_Dimensional_Anchor ) != 0 or target_2.obj.d20_query_has_spell_condition( sp_Dimensional_Anchor ) != 0):
		spell.caster.float_mesfile_line( 'mes\\spell.mes', 30011 )
		game.particles( 'Fizzle', spell.caster )

	elif (size_1 > STAT_SIZE_LARGE or size_2 > STAT_SIZE_LARGE):
		spell.caster.float_mesfile_line( 'mes\\spell.mes', 31005 )
		game.particles( 'Fizzle', spell.caster )

	elif target_1.obj.is_friendly( spell.caster ) and target_2.obj.is_friendly( spell.caster ):
		target_1.obj.move( loc_2 )
		game.particles( 'sp-Dimension Door', target_1.obj )
		target_2.obj.move( loc_1 )
		game.particles( 'sp-Dimension Door', target_2.obj )

	else:
		game.particles( 'Fizzle', spell.caster )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Benign Transposition OnBeginRound"

def OnEndSpellCast( spell ):
	print "Benign Transposition OnEndSpellCast"

