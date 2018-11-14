from toee import *
from utilities import *
from Co8 import *

def OnBeginSpellCast( spell ):
	print "Mordenkainens Sword OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Mordenkainens Sword OnSpellEffect"

	spell.duration = 1 * spell.caster_level	
	hp_bonus = 25
	weapon_proto = 4143
	weapon_portrait = 7980	
	monster_proto_id = 14629

	npc = spell.caster
	if npc.name == 8036 or npc.name == 14425:		##  faction 7
		monster_proto_id = 14621
		spell.duration = 10
		hp_bonus = 1000
	if npc.name == 14425 and npc.map == 5065:		##  faction 15
		monster_proto_id = 14604

	# determine focus
	focus = 0
	if (spell.caster.type != obj_t_pc) and (spell.caster.leader_get() == OBJ_HANDLE_NULL):
		# for NPCs not in game party
		focus = 1
	else:
		if spell.caster.money_get() >= 25000:
			focus = 1

	# check for focus
	if focus == 1:
		# create monster
		spell.summon_monsters( 1, monster_proto_id )
		monster_obj = OBJ_HANDLE_NULL
		m_list = game.obj_list_cone( spell.caster, OLC_CRITTERS, 200, -180, 360 )
		for m in m_list:
			if m.name == monster_proto_id and m.item_worn_at(3) == OBJ_HANDLE_NULL and m.leader_get() == spell.caster and are_spell_flags_null(m) == 1:
				monster_obj = m
				set_spell_flag(m, OSF_IS_MORDENKAINENS_SWORD)
				m.obj_set_int(obj_f_critter_description_unknown, 20355)
				monster_obj.object_flag_unset(OF_CLICK_THROUGH)

		if not is_in_party(spell.caster):
			monster_obj.object_flag_unset(OF_INVULNERABLE)
			monster_obj.condition_add_with_args( 'Monster Energy Immunity', 'Force', 0 )

		monster_obj.condition_add_with_args( 'Monster Plant', 0, 0 )
		monster_obj.obj_set_int(obj_f_critter_portrait, weapon_portrait)
		hit_points = 10 * spell.caster_level
		hit_points = hp_bonus + hit_points
		monster_obj.stat_base_set(stat_hp_max, hit_points)

		# equip the tempman with the appropriate weapon
		weapon_obj = game.obj_create( weapon_proto, monster_obj.location )
		weapon_obj.obj_set_int(obj_f_weapon_damage_dice, 772)
		weapon_obj.obj_set_int(obj_f_weapon_attacktype, D20DT_FORCE)
		weapon_obj.item_condition_add_with_args( 'Armor Bonus', -7, 0 )
		to_hit = spell.caster_level + 3 - monster_obj.stat_base_get(stat_attack_bonus)
		if spell.caster_class == stat_level_wizard:
			to_hit = to_hit + spell.caster.stat_level_get(stat_int_mod)
		else:
			to_hit = to_hit + spell.caster.stat_level_get(stat_cha_mod)
		weapon_obj.item_condition_add_with_args( 'To Hit Bonus', to_hit, 0 )
		weapon_obj.item_condition_add_with_args( 'Damage Bonus', 3, 0 )
		monster_obj.item_get( weapon_obj )
		weapon_obj.item_flag_set(OIF_NO_TRANSFER)
		monster_obj.item_wield_best_all()	

		# add monster to follower list for spell_caster
		if is_in_party(spell.caster):
			if not spell.caster.follower_atmax():
				spell.caster.ai_follower_remove( monster_obj )
				spell.caster.follower_add( monster_obj )
				monster_obj.condition_add_with_args( 'sp-Endurance', spell.id, spell.duration, 0 )	

		# add monster to target list
		spell.num_of_targets = 1
		spell.target_list[0].obj = monster_obj
		spell.target_list[0].partsys_id = game.particles( 'sp-Spell Resistance', spell.target_list[0].obj )

		# add spell indicator to spell caster
		spell.caster.condition_add_with_args( 'sp-Endurance', spell.id, spell.duration, 0 )

	else:
		# no focus
		spell.caster.float_mesfile_line( 'mes\\spell.mes', 16009 )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Mordenkainens Sword OnBeginRound"

def OnEndSpellCast( spell ):
	print "Mordenkainens Sword OnEndSpellCast"