from toee import *
from utilities import  * 

def OnBeginSpellCast( spell ):
	print "Prayer OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect ( spell ):
	print "Prayer OnSpellEffect"

	#remove_list = []

	spell.duration = 1 * spell.caster_level

	game.particles( 'sp-Prayer Burst', spell.target_loc )

	for target_item in spell.target_list:

		if target_item.obj.is_friendly( spell.caster ):

			target_item.obj.condition_add_with_args( 'sp-Prayer', spell.id, spell.duration, D20_MODS_SPELLS_F_PRAYER_POSITIVE )
			target_item.partsys_id = game.particles( 'sp-Prayer Burst Favor', target_item.obj )

		else:

			target_item.obj.condition_add_with_args( 'sp-Prayer', spell.id, spell.duration, D20_MODS_SPELLS_F_PRAYER_NEGATIVE )
			target_item.partsys_id = game.particles( 'sp-Prayer Burst DisFavor', target_item.obj )

	#spell.target_list.remove_list( remove_list )
	
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Prayer OnBeginRound"

def OnEndSpellCast( spell ):
	print "Prayer OnEndSpellCast"