from toee import *

def OnBeginSpellCast( spell ):
	print "Hold Portal OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Hold Portal OnSpellEffect"

	spell.duration = 10 * spell.caster_level

	target = spell.target_list[0]

	# HTN - apply condition HOLD_PORTAL
	if target.obj.type == obj_t_portal:

		target.obj.portal_flag_set( OPF_MAGICALLY_HELD )
		target.partsys_id = game.particles( 'sp-Hold Portal', target.obj )

		# HTN - need to add hold_portal spell condition to portal

		if ( target.obj.portal_flags_get() & OPF_OPEN ):
			target.obj.portal_toggle_open()

	else:

		game.particles( 'Fizzle', target.obj )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 31000 )

	spell.target_list.remove_target( target.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Hold Portal OnBeginRound"

	spell.duration = spell.duration - 1

	if spell.duration <= 0:
		spell.target_list[0].portal_flag_unset( OPF_MAGICALLY_HELD )
		game.particles_kill( spell.partsys_id )
		spell.spell_end( spell.id )

def OnEndSpellCast( spell ):
	print "Hold Portal OnEndSpellCast"