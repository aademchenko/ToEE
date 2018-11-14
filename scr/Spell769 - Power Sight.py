from toee import *
from scripts import *

def OnBeginSpellCast( spell ):
	print "Power Sight OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-divination-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Power Sight OnSpellEffect"

	spell.duration = 0
	target_item = spell.target_list[0]

	obj_hit_dice = target_item.obj.hit_dice_num
#	game.global_vars[555] = obj_hit_dice
	fin = obj_hit_dice + 100
	if fin > 120:
		fin = 121
	
	target_item.obj.float_mesfile_line( 'mes\\dice_rolls.mes', 11, tf_light_blue )
	target_item.obj.float_mesfile_line( 'mes\\dice_rolls.mes', fin, tf_light_blue )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Power Sight OnBeginRound"

def OnEndSpellCast( spell ):
	print "Power Sight OnEndSpellCast"