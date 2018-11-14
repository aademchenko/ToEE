from toee import *

from Co8 import *

def OnBeginSpellCast( spell ):
	print "Mordenkainen's Faithful Hound OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Mordenkainen's Faithful Hound OnSpellEffect"

	spell.duration = 600 * spell.caster_level

	# get the proto_id for this monster (from radial menu)
	monster_proto_id = 14278

	# create monster
	#game.particles( 'sp-Mordenkainens Faithful Hound', spell.target_loc )
	spell.summon_monsters( 1, monster_proto_id )
	
	monster_obj = GetCritterHandle( spell, 14278 )

	hit_points = 6 * spell.caster_level
	hit_points = 25 + hit_points
	monster_obj.stat_base_set(stat_hp_max, hit_points)

	# add monster to follower list for spell_caster
	spell.caster.ai_follower_add( monster_obj )

	# add monster_obj to d20initiative, and set initiative to spell_caster's
	caster_init_value = spell.caster.get_initiative()
	monster_obj.add_to_initiative()
	monster_obj.set_initiative( caster_init_value )
	game.update_combat_ui()

	# add monster to target list
	spell.num_of_targets = 1
	spell.target_list[0].obj = monster_obj

	# add condition
	spell.target_list[0].obj.condition_add_with_args( 'sp-Mordenkainens Faithful Hound', spell.id, spell.duration, 0 )
	spell.target_list[0].partsys_id = game.particles( 'sp-Mordenkainens Faithful Hound', spell.target_list[0].obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	if game.combat_is_active():
		time = 6000 * spell.caster_level
		Timed_Destroy(spell.target_list[0].obj, time)
	print "Mordenkainen's Faithful Hound OnBeginRound"

def OnEndSpellCast( spell ):
	print "Mordenkainen's Faithful Hound OnEndSpellCast"