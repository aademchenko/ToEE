from toee import *

from Co8 import *

def OnBeginSpellCast( spell ):
	print "All Die OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "All Die OnSpellEffect"
		
	remove_list = []
	
	spell.duration = 1	
		
	game.particles( 'sp-Bane', spell.caster )
		
		
	for target_item in spell.target_list:
		if target_item.obj not in game.party and target_item.obj.name != 14455:
			target_item.obj.critter_kill()
		else:
			remove_list.append( target_item.obj )
		
	spell.target_list.remove_list( remove_list )
		
	End_Spell(spell)
		
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "All Die OnBeginRound"

def OnEndSpellCast( spell ):
	print "All Die OnEndSpellCast"

