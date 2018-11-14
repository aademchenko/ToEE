from toee import *

def OnBeginSpellCast( spell ):
	print "Armour Oil OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Armour Oil OnSpellEffect"

	target = spell.target_list[0]

	if target.obj.type == obj_t_armor:

		if ( target.obj.obj_get_int(obj_f_item_wear_flags) == 32 ):
			if target.obj.obj_get_int( obj_f_material ) == mat_metal:
				if target.obj.obj_get_int(obj_f_armor_pad_i_1) == 0:
					x = target.obj.obj_get_int(obj_f_armor_armor_check_penalty)
					x = x + 1
					target.obj.obj_set_int(obj_f_armor_armor_check_penalty, x)
					target.obj.obj_set_int(obj_f_armor_pad_i_1, 1)
					target.partsys_id = game.particles( 'sp-Knock', spell.caster )
				else:
					spell.caster.float_mesfile_line( 'mes\\spell.mes', 16012 )
			else:
				spell.caster.float_mesfile_line( 'mes\\spell.mes', 31010 )
		else:
			spell.caster.float_mesfile_line( 'mes\\spell.mes', 16013 )

	else:

		game.particles( 'Fizzle', target.obj )
		spell.caster.float_mesfile_line( 'mes\\spell.mes', 16013 )

	spell.target_list.remove_target( target.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Armour Oil OnBeginRound"

def OnEndSpellCast( spell ):
	print "Armour Oil OnEndSpellCast"