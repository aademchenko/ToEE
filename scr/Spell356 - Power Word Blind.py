from toee import *

def OnBeginSpellCast( spell ):
	print "Power Word Blind OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def OnSpellEffect ( spell ):
	print "Power Word Blind OnSpellEffect"

	target = spell.target_list[0]

	# If target has over 200 hit points, spell fails
	if target.obj.stat_level_get( stat_hp_current ) > 200:
		target.obj.float_mesfile_line( 'mes\\spell.mes', 32000 )
		game.particles( 'Fizzle', target.obj )

	elif target.obj.stat_level_get( stat_hp_current ) > 100:
		spell.duration = game.random_range(2,5)
		# apply blindness
		return_val = target.obj.condition_add_with_args( 'sp-Glitterdust Blindness', spell.id, spell.duration, 0 )
		if return_val == 1:
			target.partsys_id = game.particles( 'sp-Blindness-Deafness', target.obj )

	elif target.obj.stat_level_get( stat_hp_current ) > 50:
		spell.duration = game.random_range(2,5) * 10
		# apply blindness
		return_val = target.obj.condition_add_with_args( 'sp-Glitterdust Blindness', spell.id, spell.duration, 0 )
		if return_val == 1:
			target.partsys_id = game.particles( 'sp-Blindness-Deafness', target.obj )
	else:
		spell.duration = 99999
		# apply blindness
		return_val = target.obj.condition_add_with_args( 'sp-Glitterdust Blindness', spell.id, spell.duration, 0 )
		if return_val == 1:
			target.partsys_id = game.particles( 'sp-Blindness-Deafness', target.obj )

	spell.target_list.remove_target( target.obj )
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Power Word Blind OnBeginRound"

def OnEndSpellCast( spell ):
	print "Power Word Blind OnEndSpellCast"
