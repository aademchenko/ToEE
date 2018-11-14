from toee import *

def OnBeginSpellCast( spell ):
	print "Open/Close OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Open/Close OnSpellEffect"

	target = spell.target_list[0]

	if target.obj.type == obj_t_portal:
		target.partsys_id = game.particles( 'sp-Open Close', target.obj )

		if ( target.obj.portal_flags_get() & OPF_LOCKED ):
			game.particles( 'Fizzle', target.obj )
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )

		elif ( target.obj.portal_flags_get() & OPF_MAGICALLY_HELD ):
			game.particles( 'Fizzle', target.obj )
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )

		elif not (target.obj.portal_flags_get() & OPF_OPEN):
			target.obj.portal_toggle_open()
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30013 )

		else:
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30014 )

	elif target.obj.type == obj_t_container:
		target.partsys_id = game.particles( 'sp-Open Close', target.obj )

		if ( target.obj.container_flags_get() & OCOF_LOCKED ):
			game.particles( 'Fizzle', target.obj )
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )

		elif ( target.obj.container_flags_get() & OCOF_MAGICALLY_HELD ):
			game.particles( 'Fizzle', target.obj )
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )

		elif not (target.obj.container_flags_get() & OCOF_OPEN):
			target.obj.container_toggle_open()
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30013 )

		else:
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30014 )

	else:
		game.particles( 'Fizzle', target.obj )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30003 )

	spell.target_list.remove_target( target.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Open/Close OnBeginRound"

def OnEndSpellCast( spell ):
	print "Open/Close OnEndSpellCast"