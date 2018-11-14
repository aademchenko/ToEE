from toee import *

def OnBeginSpellCast( spell ):
	print "Summon Giant Constictor Snake OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Summon Giant Constictor Snake OnSpellEffect"

	spell.duration = 10

	# get the proto_id for this monster 
	monster_proto_id = 14389

	# create monster
	spell.summon_monsters( 1, monster_proto_id )
	
	#  Gets handle on monster, and sets a flag so that it won't be mistaken for a new summoned monster
	monster_obj = GetHandle(spell, monster_proto_id)
	set_ID(monster_obj, 1)

	game.particles( 'Orb-Summon-Air-Elemental', monster_obj )

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
	print "Summon Giant Constictor Snake OnBeginRound"

def OnEndSpellCast( spell ):
	print "Summon Giant Constictor Snake OnEndSpellCast"

	
def GetHandle( spell, proto_id ):
# Returns a handle that can be used to manipulate the familiar creature object
	for npc in game.obj_list_vicinity( spell.target_loc, OLC_CRITTERS ):
		if (npc.name == proto_id):
			if not ( get_ID( npc ) ):
				return npc
	return OBJ_HANDLE_NULL

def get_ID(obj):
# Returns embedded ID number
	return obj.obj_get_int(obj_f_secretdoor_dc)

def set_ID( obj, val ):
# Embeds ID number into mobile object.  Returns ID number.
	obj.obj_set_int( obj_f_secretdoor_dc, val )
	return obj.obj_get_int( obj_f_secretdoor_dc )
	
def clear_ID( obj ):
# Clears embedded ID number from mobile object
	obj.obj_set_int( obj_f_secretdoor_dc, 0 )

