from toee import *

def OnBeginSpellCast( spell ):
	print "Break Enchantment OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect ( spell ):
	print "Break Enchantment OnSpellEffect"

#	Dar's level check no longer needed thanks to Spellslinger's dll fix
#	if spell.caster_class == 13: #added to check for proper paladin slot level (darmagon)
#		if spell.spell_level < 4:
#			spell.caster.float_mesfile_line('mes\\spell.mes', 16008)
#			spell.spell_end(spell.id)
#			return

	remove_list = []

	spell.duration = 0

	game.particles( 'sp-Break Enchantment-Area', spell.caster )
	for target_item in spell.target_list:

		target_item.obj.condition_add_with_args( 'sp-Break Enchantment', spell.id, spell.duration, 0 )
		target_item.partsys_id = game.particles( 'sp-Break Enchantment-Hit', target_item.obj )

		remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Break Enchantment OnBeginRound"

def OnEndSpellCast( spell ):
	print "Break Enchantment OnEndSpellCast"