from toee import *

def OnBeginSpellCast( spell ):
	print "Invisibility Purge OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Invisibility Purge OnSpellEffect"

	spell.duration = 10 * spell.caster_level
	target_item = spell.target_list[0]

	# put sp-Invisibility Purge condition on obj
	spell_obj_partsys_id = game.particles( 'sp-Invisibility Purge', target_item.obj )
	target_item.obj.condition_add_with_args( 'sp-Invisibility Purge', spell.id, spell.duration, 0, spell_obj_partsys_id )
	#target_item.obj.condition_add_arg_x( 3, spell_obj_partsys_id )
	#objectevent_id = target_item.obj.condition_get_arg_x( 2 )

def OnBeginRound( spell ):
	print "Invisibility Purge OnBeginRound"

def OnEndSpellCast( spell ):
	print "Invisibility Purge OnEndSpellCast"

def OnAreaOfEffectHit( spell ):
	print "Invisibility Purge OnAreaOfEffectHit"

def OnSpellStruck( spell ):
	print "Invisibility Purge OnSpellStruck"