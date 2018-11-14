from toee import *
from utilities import *

def OnBeginSpellCast( spell ):
	print "Endurance OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def OnSpellEffect ( spell ):
	print "Endurance OnSpellEffect"

	endurance_bonus = 4

	spell.duration = 10 * spell.caster_level

	meta = spell.caster.item_find(8090)
	if meta != OBJ_HANDLE_NULL:
		meta.destroy()
		spell.duration = spell.duration * 2

	target = spell.target_list[0]

	target.obj.float_mesfile_line( 'mes\\spell.mes', 20023 )
	target.obj.condition_add_with_args( 'sp-Endurance', spell.id, spell.duration, endurance_bonus )
	target.partsys_id = game.particles( 'sp-Bears Endurance', target.obj )

def OnBeginRound( spell ):
	print "Endurance OnBeginRound"

def OnEndSpellCast( spell ):
	print "Endurance OnEndSpellCast"