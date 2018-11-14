from toee import *

from Co8 import *

def OnBeginSpellCast( spell ):
	print "Summon Balor OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Summon Balor OnSpellEffect"

	spell.duration = 4

	# get the proto_id for this monster 
	monster_proto_id = 14286

	# create monster
	# monster_obj = game.obj_create( monster_proto_id, spell.target_loc ) ## this line doesn't work - can't added timed disapearance if created this way
	spell.summon_monsters( 1, monster_proto_id )
	
	#  Gets handle on monster, and sets a flag so that it won't be mistaken for a new summoned monster
	monster_obj = GetCritterHandle(spell, monster_proto_id)

	game.particles( 'Orb-Summon-Balor', monster_obj )

	# add monster to follower list for spell_caster
	spell.caster.ai_follower_add( monster_obj )

	# add monster_obj to d20initiative, and set initiative to spell_caster's
	caster_init_value = spell.caster.get_initiative()
	monster_obj.add_to_initiative()
	monster_obj.set_initiative( caster_init_value )
	game.update_combat_ui()

	# monster should disappear when duration is over, apply "TIMED_DISAPPEAR" condition
	monster_obj.condition_add_with_args( 'sp-Summoned', spell.id, spell.duration, 0 )

	# add monster to target list
	spell.num_of_targets = 1
	spell.target_list[0].obj = monster_obj

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Summon Balor OnBeginRound"

def OnEndSpellCast( spell ):
	print "Summon Balor OnEndSpellCast"

	
