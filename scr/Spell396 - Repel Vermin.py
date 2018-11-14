from toee import *

def OnBeginSpellCast( spell ):
	print "Repel Vermin OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect ( spell ):
	print "Repel Vermin OnSpellEffect"

	spell.duration = 600 * spell.caster_level
	target_item = spell.target_list[0]

	# put sp-Minor Globe condition on target
	spell_obj_partsys_id = game.particles( 'sp-Repel Vermin', target_item.obj )
	target_item.obj.condition_add_with_args( 'sp-Repel Vermin', spell.id, spell.duration, 0, spell_obj_partsys_id )
	#target_item.obj.condition_add_arg_x( 3, spell_obj_partsys_id )
	#objectevent_id = target_item.obj.condition_get_arg_x( 2 )

def OnBeginRound( spell ):
	print "Repel Vermin OnBeginRound"

def OnEndSpellCast( spell ):
	print "Repel Vermin OnEndSpellCast"

def OnAreaOfEffectHit( spell ):
	print "Repel Vermin OnAreaOfEffectHit"

def OnSpellStruck( spell ):
	print "Repel Vermin OnSpellStruck"