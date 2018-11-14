from toee import *

def OnBeginSpellCast( spell ):
	print "Wind Wall OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Wind Wall OnSpellEffect"

	spell.duration = 1 * spell.caster_level
	target_item = spell.target_list[0]

	# put sp-Wind Wall condition on target
	spell_obj_partsys_id = game.particles( 'sp-Wind Wall', target_item.obj )
	target_item.obj.condition_add_with_args( 'sp-Wind Wall', spell.id, spell.duration, 0, spell_obj_partsys_id )
	#target_item.obj.condition_add_arg_x( 3, spell_obj_partsys_id )
	#objectevent_id = target_item.obj.condition_get_arg_x( 2 )

def OnBeginRound( spell ):
	print "Wind Wall OnBeginRound"

def OnEndSpellCast( spell ):
	print "Wind Wall OnEndSpellCast"

def OnAreaOfEffectHit( spell ):
	print "Wind Wall OnAreaOfEffectHit"

def OnSpellStruck( spell ):
	print "Wind Wall OnSpellStruck"