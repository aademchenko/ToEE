from toee import *

def OnBeginSpellCast( spell ):
	print "Lockslip Grease OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Gentle Repose OnSpellEffect"

	target = spell.target_list[0]
	chest = target.obj
	if spell.caster.map == 5081:
		game.particles( 'Fizzle', target.obj )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
		target.obj.float_mesfile_line( 'mes\\narrative.mes', 160, tf_yellow )

	elif target.obj.type == obj_t_portal:

		if ( target.obj.portal_flags_get() & OPF_LOCKED ):
			if target.obj.obj_get_int(obj_f_portal_pad_i_1) == 0:
				x = target.obj.obj_get_int(obj_f_portal_lock_dc)
				x = x - 1
				target.obj.obj_set_int(obj_f_portal_lock_dc, x)
				target.obj.obj_set_int(obj_f_portal_pad_i_1, 1)
				target.partsys_id = game.particles( 'sp-Knock', target.obj )
			else:
				target.obj.float_mesfile_line( 'mes\\spell.mes', 16012 )
		else:
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30006 )

	elif target.obj.type == obj_t_container:

		if ( target.obj.container_flags_get() & OCOF_LOCKED ):
			if target.obj.obj_get_int(obj_f_container_pad_i_1) == 0:
				x = target.obj.obj_get_int(obj_f_container_lock_dc)
				x = x - 1
				target.obj.obj_set_int(obj_f_container_lock_dc, x)
				target.obj.obj_set_int(obj_f_container_pad_i_1, 1)
				target.partsys_id = game.particles( 'sp-Knock', target.obj )
			else:
				target.obj.float_mesfile_line( 'mes\\spell.mes', 16012 )
		else:
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30006 )

	else:

		game.particles( 'Fizzle', target.obj )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 31000 )

	spell.target_list.remove_target( target.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Lockslip Grease OnBeginRound"

def OnEndSpellCast( spell ):
	print "Lockslip Grease OnEndSpellCast"