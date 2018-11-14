from toee import *

def OnBeginSpellCast( spell ):
	print "Knock OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Knock OnSpellEffect"

	target = spell.target_list[0]
	chest = target.obj

	if target.obj.type == obj_t_portal:
		target.partsys_id = game.particles( 'sp-Knock', target.obj )

		if ( target.obj.portal_flags_get() & OPF_LOCKED ):
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30004 )
			target.obj.portal_flag_unset( OPF_LOCKED )
		else:
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30006 )

		if ( target.obj.portal_flags_get() & OPF_MAGICALLY_HELD ):
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30005 )
			target.obj.portal_flag_unset( OPF_MAGICALLY_HELD )

		if not ( target.obj.portal_flags_get() & OPF_OPEN ):
			target.obj.portal_toggle_open()

	elif chest.name == 1053 or chest.name == 1055:
		game.particles( 'Fizzle', target.obj )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 31014 )

	elif chest.name == 1056:
		game.global_flags[874] = 1
		game.particles( 'Fizzle', target.obj )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 31014 )

	elif target.obj.type == obj_t_container:
		target.partsys_id = game.particles( 'sp-Knock', target.obj )

		if ( target.obj.container_flags_get() & OCOF_LOCKED ):
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30004 )
			target.obj.container_flag_unset( OCOF_LOCKED )

		if ( target.obj.container_flags_get() & OCOF_MAGICALLY_HELD ):
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30005 )
			target.obj.container_flag_unset( OCOF_MAGICALLY_HELD )

		if not ( target.obj.container_flags_get() & OCOF_OPEN ):
			target.obj.container_toggle_open()

	else:
		game.particles( 'Fizzle', target.obj )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30003 )

	spell.target_list.remove_target( target.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Knock OnBeginRound"

	#spell.duration = spell.duration - 1

	#if (was_magically_locked == 0) and (spell.target_list[0].portal_flags_get() & OPF_MAGICALLY_HELD):
		#was_magically_locked = 1
		#spell.target_list[0].float_mesfile_line( 'mes\\spell.mes', 30005 )
		#spell.target_list[0].portal_flag_unset( OPF_MAGICALLY_HELD )

	#if spell.duration <= 0:
		#if was_magically_locked == 1:
			#spell.target_list[0].portal_flag_set( OPF_MAGICALLY_HELD )
		#game.particles_kill( spell.partsys_id )
		#spell.spell_end( spell.id )

def OnEndSpellCast( spell ):
	print "Knock OnEndSpellCast"