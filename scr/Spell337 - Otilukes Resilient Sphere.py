from toee import *

def OnBeginSpellCast( spell ):
	print "Otiluke's Resilient Sphere OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def do_particles( target ):
	part_str = 'sp-Otilukes Resilient Sphere'

	if target.obj.get_size <= STAT_SIZE_MEDIUM:
		part_str = 'sp-Otilukes Resilient Sphere-MED'
	elif target.obj.get_size == STAT_SIZE_LARGE:
		part_str = 'sp-Otilukes Resilient Sphere-LARGE'
	else:
		part_str = 'sp-Otilukes Resilient Sphere-HUGE'

	target.partsys_id = game.particles( part_str, target.obj )

def	OnSpellEffect( spell ):
	print "Otiluke's Resilient Sphere OnSpellEffect"

	spell.duration = 10 * spell.caster_level

	target = spell.target_list[0]

	friend = target.obj.is_friendly( spell.caster )

	if not friend:
		saved = target.obj.saving_throw_spell( spell.dc,
						       D20_Save_Reflex,
						       D20STD_F_NONE,
						       spell.caster,
						       spell.id )
		if saved:
			target.obj.float_mesfile_line( 'mes\\spell.mes',
						       30001 )
		else:
			target.obj.float_mesfile_line( 'mes\\spell.mes',
						       30002 )
	else:
		saved = 1

	if friend or not saved:
		target.obj.condition_add_with_args(
			'sp-Otilukes Resilient Sphere',
			spell.id, spell.duration, 0 )
		do_particles( target )
	else:
		game.particles( 'Fizzle', target.obj )
		spell.target_list.remove_target( target.obj )
		spell.spell_end( spell.id )
		

def OnBeginRound( spell ):
	print "Otiluke's Resilient Sphere OnBeginRound"

def OnEndSpellCast( spell ):
	print "Otiluke's Resilient Sphere OnEndSpellCast"