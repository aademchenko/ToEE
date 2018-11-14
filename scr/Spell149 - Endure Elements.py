from toee import *


# Added Nalorrem - SA

def OnBeginSpellCast( spell ):
	print "Endure Elements OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Endure Elements OnSpellEffect"

	spell_arg = spell.spell_get_menu_arg( RADIAL_MENU_PARAM_MIN_SETTING )
	
	## Solves Radial menu problem for Wands/NPCs
	if spell_arg != 1 and spell_arg != 2 and spell_arg != 3 and spell_arg != 4 and spell_arg != 5:
		spell_arg = game.random_range(1,5)

	npc = spell.caster
	if npc.name == 14332:			
		spell_arg = 4
	if npc.name == 14197 or npc.name == 14198:
	#Merrolan and Nalorrem
		spell_arg = 4
	if (npc.name == 14212 or npc.name == 14211) and npc == spell.target_list[0].obj: #Tubal, Antonio casting endure elements on self
		spell_arg = 4
	if (npc.name == 14212 or npc.name == 14211) and npc != spell.target_list[0].obj: #Tubal, Antonio casting protection from cold on others
		spell_arg = 2

	if spell.target_list[0].obj.name == 14195 or spell.target_list[0].obj.name == 14224: # Oohlgrist or Aern; they already has a magic ring against fire
		spell_arg = 2

	if spell_arg == 1:
		element_type = ACID
		partsys_type = 'sp-Endure Elements-acid'
	elif spell_arg == 2:
		element_type = COLD
		partsys_type = 'sp-Endure Elements-cold'
	elif spell_arg == 3:
		element_type = ELECTRICITY
		partsys_type = 'sp-Endure Elements-water'
	elif spell_arg == 4:
		element_type = FIRE
		partsys_type = 'sp-Endure Elements-fire'
	elif spell_arg == 5:
		element_type = SONIC
		partsys_type = 'sp-Endure Elements-Sonic'

	# 24 hours
	spell.duration = 14400

	target_item = spell.target_list[0]

	target_item.obj.condition_add_with_args( 'sp-Endure Elements', spell.id, element_type, spell.duration )
	target_item.partsys_id = game.particles( partsys_type, target_item.obj )

	#spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Endure Elements OnBeginRound"

def OnEndSpellCast( spell ):
	print "Endure Elements OnEndSpellCast"