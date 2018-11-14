from toee import *

def OnBeginSpellCast( spell ):
	print "Potion of super-heroism OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Potion of super-heroism OnSpellEffect"

	spell.duration = 600
	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Potion of super-heroism', spell.id, spell.duration, 0 )
	#target.partsys_id = game.particles( 'sp-Potion of super-heroism', spell.caster )

	#add the temp hit points
	if (spell.caster_level < 20):
		temp_hit_points = spell.caster_level
	else:
		temp_hit_points = 20
	
	target.obj.condition_add_with_args( 'Temporary_Hit_Points', spell.id, spell.duration, temp_hit_points )

	#spell.target_list.remove_target( target.obj )
	#spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Potion of super-heroism OnBeginRound"

def OnEndSpellCast( spell ):
	print "Potion of super-heroism OnEndSpellCast"