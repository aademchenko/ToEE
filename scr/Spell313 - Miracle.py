from toee import *

def OnBeginSpellCast( spell ):
	print "Miracle OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	for target_item in spell.target_list:
		if not target_item.obj.is_friendly( spell.caster ):
			spell.target_list.remove_target( target_item.obj )
	
def OnSpellEffect( spell ):
	print "Miracle OnSpellEffect"
	spell.duration = 0
	
	for target_item in spell.target_list:		
		if target_item.obj.is_friendly( spell.caster ):
			if target_item.obj.stat_level_get( stat_hp_current ) <= -10:
				target_item.obj.condition_add_with_args( 'sp-Raise Dead', spell.id, spell.duration, 0 )
			else:
				target_item.obj.condition_add_with_args('sp-Heal',spell.id, spell.duration, 0)
				game.particles( 'sp-Cure Critical Wounds', target_item.obj )
		
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Miracle OnBeginRound"

def OnEndSpellCast( spell ):
	print "Miracle OnEndSpellCast"
	


