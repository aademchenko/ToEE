from toee import *

def OnBeginSpellCast( spell ):
	print "Desecrate OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Desecrate OnSpellEffect"

	spell.duration = 1200 * spell.caster_level

	# spawn one spell_object object
	spell_obj = game.obj_create( OBJECT_SPELL_GENERIC, spell.target_loc )

	# add to d20initiative
	caster_init_value = spell.caster.get_initiative()
	spell_obj.d20_status_init()
	spell_obj.set_initiative( caster_init_value )

	# put sp-Desecrate condition on obj
	spell_obj_partsys_id = game.particles( 'sp-Desecrate', spell_obj )
	spell_obj.condition_add_with_args( 'sp-Desecrate', spell.id, spell.duration, 0, spell_obj_partsys_id )
	#spell_obj.condition_add_arg_x( 3, spell_obj_partsys_id )
	#objectevent_id = spell_obj.condition_get_arg_x( 2 )

def OnBeginRound( spell ):
	print "Desecrate OnBeginRound"

def OnEndSpellCast( spell ):
	print "Desecrate OnEndSpellCast"

def OnAreaOfEffectHit( spell ):
	print "Desecrate OnAreaOfEffectHit"

def OnSpellStruck( spell ):
	print "Desecrate OnSpellStruck"