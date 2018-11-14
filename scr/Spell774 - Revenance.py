from toee import *
from scripts import *
from Co8 import *

def OnBeginSpellCast( spell ):
	print ("Revenance OnBeginSpellCast")
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Revenance OnSpellEffect"

	spell.duration = 10 * spell.caster_level
	target_item = spell.target_list[0]

	if target_item.obj.stat_level_get(stat_hp_current) <= -10:
		target_item.obj.resurrect( CRITTER_R_CUTHBERT_RESURRECT, 0 )
		damage_dice = (target_item.obj.stat_level_get( stat_hp_current ) / 2)
		dam = dice_new( '1d1' )
		dam.number = min( 500, damage_dice )
		target_item.obj.spell_damage( spell.caster, D20DT_BLOOD_LOSS, dam, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
		target_item.obj.scripts[14] = 453

	else:
		game.particles( 'Fizzle', target_item.obj )
	
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print ("Revenance OnBeginRound")

def OnEndSpellCast( spell ):
	print ("Revenance OnEndSpellCast")