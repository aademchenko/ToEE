from toee import *

def OnBeginSpellCast( spell ):
	print "Power Word Stun OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def OnSpellEffect ( spell ):
	print "Power Word Stun OnSpellEffect"

	target = spell.target_list[0]

	# If target has over 150 hit points, spell fails
	if target.obj.stat_level_get( stat_hp_current ) > 150:
		target.obj.float_mesfile_line( 'mes\\spell.mes', 32000 )
		game.particles( 'Fizzle', target_item.obj )

	elif target.obj.stat_level_get( stat_hp_current ) > 100:
		spell.duration = game.random_range(1,4)
		# apply stun
		return_val = target.obj.condition_add_with_args( 'sp-Sound Burst', spell.id, spell.duration, 0 )
		if return_val == 1:
			target.partsys_id = game.particles( 'sp-Sound Burst', target.obj )

	elif target.obj.stat_level_get( stat_hp_current ) > 50:
		spell.duration = game.random_range(1,4) + game.random_range(1,4)
		# apply stun
		return_val = target.obj.condition_add_with_args( 'sp-Sound Burst', spell.id, spell.duration, 0 )
		if return_val == 1:
			target.partsys_id = game.particles( 'sp-Sound Burst', target.obj )
	else:
		spell.duration = game.random_range(1,4) + game.random_range(1,4) + game.random_range(1,4) + game.random_range(1,4)
		# apply stun
		return_val = target.obj.condition_add_with_args( 'sp-Sound Burst', spell.id, spell.duration, 0 )
		if return_val == 1:
			target.partsys_id = game.particles( 'sp-Sound Burst', target.obj )

	spell.target_list.remove_target( target.obj )
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Power Word Stun OnBeginRound"

def OnEndSpellCast( spell ):
	print "Power Word Stun OnEndSpellCast"
