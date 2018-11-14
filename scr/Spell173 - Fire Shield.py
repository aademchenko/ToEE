from toee import *
from utilities import *

def OnBeginSpellCast( spell ):
	print "Fire Shield OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Fire Shield OnSpellEffect"

	## Solves Radial menu problem for Wands/NPCs
	spell_arg = spell.spell_get_menu_arg( RADIAL_MENU_PARAM_MIN_SETTING )
	if spell_arg != 1 and spell_arg != 2:
		spell_arg = game.random_range(1,2)
	
	if spell_arg == 1:
		element_type = COLD
		partsys_type = 'sp-Fire Shield-Cold'
	elif spell_arg == 2:
		element_type = FIRE
		partsys_type = 'sp-Fire Shield-Warm'

	spell.duration = 1 * spell.caster_level

	npc = spell.caster			##  added so NPC's can use wand/potion/scroll
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL and spell.duration <= 0:
		spell.duration = 10
		spell.caster_level = 10

	target_item = spell.target_list[0]

	xx,yy = location_to_axis(target_item.obj.location)

	if game.leader.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
		## Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
		game.particles( 'swirled gas', target_item.obj )
		target_item.obj.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1 )
		game.sound(7581,1)
		game.sound(7581,1)

	else:
		xx,yy = location_to_axis(spell.caster.location)
		if game.leader.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
			game.particles( 'swirled gas', spell.caster )
			spell.caster.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1 )
			game.sound(7581,1)
			game.sound(7581,1)

		else:

			target_item.obj.condition_add_with_args( 'sp-Fire Shield', spell.id, spell.duration, element_type )
			target_item.partsys_id = game.particles( partsys_type, target_item.obj )


def OnBeginRound( spell ):
	print "Fire Shield OnBeginRound"

def OnEndSpellCast( spell ):
	print "Fire Shield OnEndSpellCast"