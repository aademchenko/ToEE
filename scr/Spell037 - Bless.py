from toee import *

def OnBeginSpellCast( spell ):
	print "Bless OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Bless OnSpellEffect"

	remove_list = []

	spell.duration = 10 * spell.caster_level
	#game.particles( 'sp-Bless', spell.target_loc_off_x, spell.target_loc_off_y, spell.target_loc_off_z )

	for target_item in spell.target_list:

		if target_item.obj.is_friendly( spell.caster ):

			return_val = target_item.obj.condition_add_with_args( 'sp-Bless', spell.id, spell.duration, 0 )
			if return_val == 1:
				target_item.partsys_id = game.particles( 'sp-Bless', target_item.obj )

		else:

			remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Bless OnBeginRound"

def OnEndSpellCast( spell ):
	print "Bless OnEndSpellCast"