from toee import *

def OnBeginSpellCast( spell ):
	print "Harm OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Harm OnSpellEffect"

	target = spell.target_list[0]

	game.particles( 'sp-Harm', target.obj )

	# check if target is undead
	if not target.obj.is_category_type( mc_type_undead ):
		# Harm target
		target.obj.condition_add_with_args( 'sp-Harm', spell.id, spell.duration, 0 )
	else:
		# Heal undead
		target.obj.condition_add_with_args( 'sp-Heal', spell.id, spell.duration, 0 )

	spell.target_list.remove_target( target )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Harm OnBeginRound"

def OnEndSpellCast( spell ):
	print "Harm OnEndSpellCast"
