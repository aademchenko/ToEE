from toee import *

def OnBeginSpellCast( spell ):
	print "Frog Tongue OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level

def	OnSpellEffect( spell ):
	print "Frog Tongue OnSpellEffect"

	# it takes 1 round to pull the target to the frog (normally)
	spell.duration = 0

	target_item = spell.target_list[0]

	# if the target is larger than the frog, it takes 2 turns to "pull" the target in
	if target_item.obj.get_size > spell.caster.get_size:
		spell.duration = 1

	if spell.caster.perform_touch_attack( target_item.obj ) == 1:

		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 21000 )

		# hit
		#target_item.obj.condition_add_with_args( 'sp-Frog Tongue', spell.id, spell.duration, 0 )
		spell.caster.condition_add_with_args( 'sp-Frog Tongue', spell.id, spell.duration, 0 )
		target_item.partsys_id = game.particles( 'sp-Frog Tongue', target_item.obj )

	else:

		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 21001 )

		spell.caster.anim_callback( ANIM_CALLBACK_FROG_FAILED_LATCH )

		# missed
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30007 )

		game.particles( 'Fizzle', target_item.obj )
		spell.target_list.remove_target( target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Frog Tongue OnBeginRound"

def OnEndSpellCast( spell ):
	print "Frog Tongue OnEndSpellCast"
