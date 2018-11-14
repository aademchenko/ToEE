from toee import *

def OnBeginSpellCast( spell ):
	print "Remove Blindness/Deafness OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect ( spell ):
	print "Remove Blindness/Deafness OnSpellEffect"

	spell.duration = 0

	target = spell.target_list[0]

	## Solves Radial menu problem for Wands/NPCs
	spell_arg = spell.spell_get_menu_arg( RADIAL_MENU_PARAM_MIN_SETTING )
	if spell_arg != 1 and spell_arg != 2:
		spell_arg = 2

	game.particles( 'sp-Remove Blindness Deafness', target.obj )

	if spell_arg == 1:

		# apply remove blindness
		target.obj.condition_add_with_args( 'sp-Remove Blindness', spell.id, spell.duration, 0 )

	else:

		# apply deafness
		target.obj.condition_add_with_args( 'sp-Remove Deafness', spell.id, spell.duration, 0 )

	spell.target_list.remove_target( target.obj )
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Remove Blindness/Deafness OnBeginRound"

def OnEndSpellCast( spell ):
	print "Remove Blindness/Deafness OnEndSpellCast"