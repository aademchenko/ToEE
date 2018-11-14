from toee import *
from utilities import *
from Co8 import *

def OnBeginSpellCast( spell ):
	print "Flaming Sphere OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect ( spell ):
	print "Flaming Sphere OnSpellEffect"
	dam = dice_new('1d4')
		
	spell.duration = 1 * spell.caster_level	
	weapon_proto = 4143
	weapon_portrait = 4320	
	monster_proto_id = 14629

	npc = spell.caster
	if npc.name == 8036 or npc.name == 14425:		##  faction 7
		monster_proto_id = 14621
	if npc.name == 14425 and npc.map == 5065:		##  faction 15
		monster_proto_id = 14604


	# create monster
	spell.summon_monsters(1, monster_proto_id)
	monster_obj = OBJ_HANDLE_NULL
	m_list = game.obj_list_cone( spell.caster, OLC_CRITTERS, 200, -180, 360 )
	for m in m_list:
		if m.name == monster_proto_id and m.item_worn_at(3) == OBJ_HANDLE_NULL and m.leader_get() == spell.caster and are_spell_flags_null(m):
			monster_obj = m
			set_spell_flag(m, OSF_IS_FLAMING_SPHERE)
			m.obj_set_int(obj_f_critter_description_unknown, 20356)			
	m_list = game.obj_list_cone(monster_obj, OLC_CRITTERS, 5, -180, 360 )
	for m in m_list:
		if m != spell.caster and is_spell_flag_set(m, OSF_IS_FLAMING_SPHERE) == 0:
			if m.saving_throw( spell.dc, D20_Save_Reflex, D20STD_F_NONE, monster_obj)==0: 
				m.damage(monster_obj,D20DT_FIRE,dam,D20DAP_NORMAL) 
			else:
				m.float_mesfile_line( 'mes\\spell.mes', 30001 )
	
	monster_obj.condition_add_with_args('Amulet of Mighty Fists', -20,-10)	
	monster_obj.condition_add_with_args('Monster Plant', 0,0)	
	monster_obj.obj_set_int( obj_f_critter_portrait, weapon_portrait )
	hit_points = 10 * spell.caster_level
	hit_points = 25 + hit_points
	monster_obj.stat_base_set(stat_hp_max, hit_points)
	monster_obj.object_flag_unset(OF_CLICK_THROUGH)
	#monster_obj.npc_flag_set(ONF_NO_ATTACK)
	
	
	# add monster to follower list for spell_caster
	if not spell.caster.follower_atmax():
		spell.caster.ai_follower_remove(monster_obj)
		spell.caster.follower_add( monster_obj )
		monster_obj.condition_add_with_args('sp-Endurance', spell.id, spell.duration, 0)	

	# add monster to target list
	spell.num_of_targets = 1
	spell.target_list[0].obj = monster_obj
	spell.target_list[0].partsys_id = game.particles( 'sp-Fireball-proj', spell.target_list[0].obj )
	
	
	#add spell indicator to spell caster 
	spell.caster.condition_add_with_args('sp-Endurance', spell.id, spell.duration, 0)
	
	print spell.target_list[0].obj	
	
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Flaming Sphere OnBeginRound"
	dam = dice_new('1d4')
	m_list = game.obj_list_cone( spell.target_list[0].obj, OLC_CRITTERS, 5, -180, 360 )
	for m in m_list:
		
		if m != spell.target_list[0].obj and m != spell.caster and not is_spell_flag_set(m, OSF_IS_FLAMING_SPHERE):
			if m.saving_throw( spell.dc, D20_Save_Reflex, D20STD_F_NONE, spell.target_list[0].obj)==0: 
				m.damage(OBJ_HANDLE_NULL,D20DT_FIRE,dam,D20DAP_NORMAL) 
			else:
				m.float_mesfile_line( 'mes\\spell.mes', 30001 )
	
def OnEndSpellCast( spell ):
	print "Flaming Sphere OnEndSpellCast"
	
	