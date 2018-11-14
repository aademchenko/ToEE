from toee import *

def OnBeginSpellCast( spell ):
	print "Barkskin OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Barkskin OnSpellEffect"

	if spell.caster_level >= 12:
		bonus = 5
	elif spell.caster_level >= 9:
		bonus = 4
	elif spell.caster_level >= 6:
		bonus = 3
	else:
		bonus = 2

	spell.duration = 100 * spell.caster_level
	target_item = spell.target_list[0]

	if target_item.obj.is_friendly( spell.caster ):

		if (target_item.obj.type == obj_t_pc) or (target_item.obj.type == obj_t_npc):
			target_item.obj.condition_add_with_args( 'sp-Barkskin', spell.id, spell.duration, bonus )
			target_item.partsys_id = game.particles( 'sp-Barkskin', target_item.obj )
		else:
			game.particles( 'Fizzle', target_item.obj )
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31001 )
			spell.target_list.remove_target( target_item.obj )

	elif not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

		if (target_item.obj.type == obj_t_pc) or (target_item.obj.type == obj_t_npc):
			# saving throw unsuccessful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			target_item.obj.condition_add_with_args( 'sp-Barkskin', spell.id, spell.duration, bonus )
			target_item.partsys_id = game.particles( 'sp-Barkskin', target_item.obj )
		else:
			game.particles( 'Fizzle', target_item.obj )
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31001 )
			spell.target_list.remove_target( target_item.obj )

	else:

		# saving throw successful
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

		game.particles( 'Fizzle', target_item.obj )
		spell.target_list.remove_target( target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Barkskin OnBeginRound"

def OnEndSpellCast( spell ):
	print "Barkskin OnEndSpellCast"