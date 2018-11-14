from toee import *

def OnBeginSpellCast( spell ):
	print "Giant Vermin OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Giant Vermin OnSpellEffect"

	spell.duration = 10 * spell.caster_level # fixed - should be 1min/level

	# get the proto_id for this monster (from radial menu)
	## Solves Radial menu problem for Wands/NPCs
	spell_arg = spell.spell_get_menu_arg( RADIAL_MENU_PARAM_MIN_SETTING )
	if spell_arg != 14089 and spell_arg != 14047 and spell_arg != 14417:
		spell_arg = game.random_range(1,3)
		if spell_arg == 1:
			spell_arg = 14089
		elif spell_arg == 2:
			spell_arg = 14047
		elif spell_arg == 3:
			spell_arg = 14417

	# create monster, monster should be added to target_list
	spell.summon_monsters( 1, spell_arg )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Giant Vermin OnBeginRound"

def OnEndSpellCast( spell ):
	print "Giant Vermin OnEndSpellCast"