from toee import *

def OnBeginSpellCast( spell ):
	print "Protection From Arrows OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Protection From Arrows OnSpellEffect"

	damage_max = 10 * min( 10, spell.caster_level )
	spell.duration = 600 * spell.caster_level

	target = spell.target_list[0]

	if target.obj.is_friendly( spell.caster ):
		target.obj.condition_add_with_args( 'sp-Protection From Arrows', spell.id, spell.duration, damage_max )
		target.partsys_id = game.particles( 'sp-Protection From Arrows', target.obj )

	elif not target.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
		# saving throw unsuccessful
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
		target.obj.condition_add_with_args( 'sp-Protection From Arrows', spell.id, spell.duration, damage_max )
		target.partsys_id = game.particles( 'sp-Protection From Arrows', target.obj )

	else:
		# saving throw successful
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
		game.particles( 'Fizzle', target.obj )
		spell.target_list.remove_target( target.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Protection From Arrows OnBeginRound"

def OnEndSpellCast( spell ):
	print "Protection From Arrows OnEndSpellCast"