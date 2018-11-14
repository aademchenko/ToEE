from toee import *
from utilities import *

def OnBeginSpellCast( spell ):
	print "Discern Lies OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-divination-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Discern Lies OnSpellEffect"

#	Dar's level check no longer needed thanks to Spellslinger's dll fix
#	if spell.caster_class == 13: #added to check for proper paladin slot level (darmagon)
#		if spell.spell_level < 3:
#			spell.caster.float_mesfile_line('mes\\spell.mes', 16008)
#			spell.spell_end(spell.id)
#			return

	spell.duration = 1 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Discern Lies', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Discern Lies', spell.caster )
	
def OnBeginRound( spell ):
	print "Discern Lies OnBeginRound"

def OnEndSpellCast( spell ):
	print "Discern Lies OnEndSpellCast"