from toee import *
from utilities import  * 

def OnBeginSpellCast( spell ):
	print "Dispel Evil OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def OnSpellEffect ( spell ):
	print "Dispel Evil OnSpellEffect"

#	Dar's level check no longer needed thanks to Spellslinger's dll fix
#	if spell.caster_class == 13: #added to check for proper paladin slot level (darmagon)
#		if spell.spell_level < 4:
#			spell.caster.float_mesfile_line('mes\\spell.mes', 16008)
#			spell.spell_end(spell.id)
#			return

	spell.duration = 1 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Dispel Evil', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Dispel Evil', target.obj )
	

def OnBeginRound( spell ):
	print "Dispel Evil OnBeginRound"

def OnEndSpellCast( spell ):
	print "Dispel Evil OnEndSpellCast"