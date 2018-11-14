from toee import *

from __main__ import game

from utilities import *

from livonya import *

import _include

from co8Util import size


def npc_1(attachee):
	attachee.obj_set_int( obj_f_npc_pad_i_3, 1 )
	return

def npc_2(attachee):
	attachee.obj_set_int( obj_f_npc_pad_i_4, 1 )
	return

def npc_3(attachee):
	attachee.obj_set_int( obj_f_npc_pad_i_5, 1 )
	return

def npc_1_undo(attachee):
	attachee.obj_set_int( obj_f_npc_pad_i_3, 0 )
	return

def npc_2_undo(attachee):
	attachee.obj_set_int( obj_f_npc_pad_i_4, 0 )
	return

def npc_3_undo(attachee):
	attachee.obj_set_int( obj_f_npc_pad_i_5, 0 )
	return

def get_1(attachee):
	x1 = attachee.obj_get_int( obj_f_npc_pad_i_3 )
	if x1 != 0:
		return 1
	return

def get_2(attachee):
	x2 = attachee.obj_get_int( obj_f_npc_pad_i_4 )
	if x2 != 0:
		return 1
	return

def get_3(attachee):
	x3 = attachee.obj_get_int( obj_f_npc_pad_i_5 )
	if x3 != 0:
		return 1
	return

def oflag_1(attachee):
	attachee.obj_set_int(obj_f_item_pad_i_1, 1)
	return

def get_of1(attachee):
	x4 = attachee.obj_set_int(obj_f_item_pad_i_1)
	if x4 != 0:
		return 1
	return

def npcvar_1(attachee, var):
	attachee.obj_set_int( obj_f_npc_pad_i_3, var )
	return

def npcvar_2(attachee, var):
	attachee.obj_set_int( obj_f_npc_pad_i_4, var )
	return

def npcvar_3(attachee, var):
	attachee.obj_set_int( obj_f_npc_pad_i_5, var )
	return

def getvar_1(attachee):
	x1 = attachee.obj_get_int( obj_f_npc_pad_i_3 )
	if x1 != 0:
		return x1
	return 0

def getvar_2(attachee):
	x2 = attachee.obj_get_int( obj_f_npc_pad_i_4 )
	if x2 != 0:
		return x2
	return 0

def getvar_3(attachee):
	x3 = attachee.obj_get_int( obj_f_npc_pad_i_5 )
	if x3 != 0:
		return x3
	return 0

def bluff( attachee, triggerer, dc ):
	x = game.random_range(1,20)
	y = x + triggerer.skill_level_get(attachee, skill_bluff)
	if y >= dc:
		return 1
	return 0

def dipl( attachee, triggerer, dc ):
	a = game.random_range(1,20)
	b = a + triggerer.skill_level_get(attachee, skill_diplomacy)
	if b >= dc:
		return 1
	return 0

def intim( attachee, triggerer, dc ):
	c = game.random_range(1,20)
	d = c + triggerer.skill_level_get(attachee, skill_intimidate)
	if d >= dc:
		return 1
	return 0

def info( attachee, triggerer, dc ):
	e = game.random_range(1,20)
	f = e + triggerer.skill_level_get(attachee, skill_gather_information)
	if f >= dc:
		return 1
	return 0

def sense( attachee, triggerer, dc ):
	g = game.random_range(1,20)
	h = g + triggerer.skill_level_get(attachee, skill_sense_motive)
	if h >= dc:
		return 1
	return 0

def away(attachee):
	x = attachee.rotation
	x = x+3.1416
	if x >= 6.28:
		x = x - 6.27
	attachee.rotation = x
	return

def pc_only( attachee, triggerer ):
	d = 0
	for mem in game.party:
		if mem.type == obj_t_npc:
			d = 1
	if d != 0:
		return 0
	return 1

def next_slot( wearer, slot):
	slot = 35
	full = wearer.item_worn_at(slot)
	while full != OBJ_HANDLE_NULL:
		slot = slot + 1
	return slot

def give_a_ton():
	for obj in game.leader.group_list():
		curxp = obj.stat_level_get(stat_experience)
		newxp = curxp + 100
		obj.stat_base_set(stat_experience, newxp)
		obj.float_mesfile_line( 'mes\\narrative.mes', 1010 )
	return

def sense_roll( attachee, triggerer, dc, ayup, nope ):
	i = game.random_range(1,20)
	j = i + triggerer.skill_level_get(attachee, skill_sense_motive)
	if j >= dc:
		triggerer.begin_dialog( attachee, ayup )
	else:
		triggerer.begin_dialog( attachee, nope )
	return

def intim_roll( attachee, triggerer, dc, ayup, nope ):
	k = game.random_range(1,20)
	l = k + triggerer.skill_level_get(attachee, skill_intimidate)
	if l >= dc:
		triggerer.begin_dialog( attachee, ayup )
	else:
		triggerer.begin_dialog( attachee, nope )
	return

def bluff_roll( attachee, triggerer, dc, ayup, nope ):
	m = game.random_range(1,20)
	n = m + triggerer.skill_level_get(attachee, skill_bluff)
	if n >= dc:
		triggerer.begin_dialog( attachee, ayup )
	else:
		triggerer.begin_dialog( attachee, nope )
	return

def dipl_roll( attachee, triggerer, dc, ayup, nope ):
	o = game.random_range(1,20)
	p = o + triggerer.skill_level_get(attachee, skill_diplomacy)
	if p >= dc:
		triggerer.begin_dialog( attachee, ayup )
	else:
		triggerer.begin_dialog( attachee, nope )
	return

def gath_roll( attachee, triggerer, dc, ayup, nope ):
	q = game.random_range(1,20)
	r = q + triggerer.skill_level_get(attachee, skill_gather_information)
	if r >= dc:
		triggerer.begin_dialog( attachee, ayup )
	else:
		triggerer.begin_dialog( attachee, nope )
	return

def how_many_ai():
	foll = len(game.party)
	aifoll = len(game.leader.group_list())
	x = aifoll - foll
	return x

def drop_all(target):
	item = target.item_worn_at(3)
	if item != OBJ_HANDLE_NULL:
		basil3 = game.obj_create(item.name, target.location)
		basil3.rotation = 2.3
		item.destroy()
		target.critter_flag_set( OCF_UNUSED_00000400 )
	item2 = target.item_worn_at(4)
	if item2 != OBJ_HANDLE_NULL:
		basil1 = game.obj_create(item2.name, target.location)
		basil1.rotation = 2.3
		item2.destroy()
	item3 = target.item_worn_at(11)
	if item3 != OBJ_HANDLE_NULL:
		basil2 = game.obj_create(item3.name, target.location)
		basil2.rotation = 2.3
		item3.destroy()
	return

def nothing(attachee):
	if attachee.is_category_type( mc_type_humanoid ):
		attachee.item_wield_best_all()
		weap = attachee.item_worn_at(3)
		if weap == OBJ_HANDLE_NULL:
			return 1
		else:
			attachee.critter_flag_unset( OCF_UNUSED_00000400 )
	return 0

def get_something(attachee):
	if critter_is_unconscious(attachee) == 1 or attachee.d20_query_has_spell_condition( sp_Sound_Burst ) != 0 or attachee.d20_query(Q_Critter_Is_Stunned) != 0:
		attachee.float_mesfile_line( 'mes\\spell.mes', 20021 )
		return
#	game.particles( "sp-summon monster I", game.party[0] )
	for weap in game.obj_list_vicinity(attachee.location,OLC_WEAPON):
		if weap != OBJ_HANDLE_NULL:
			sizeCat = attachee.obj_get_int(obj_f_size)
			if sizeCat <= STAT_SIZE_MEDIUM and attachee.distance_to(weap) <= 10:
				attachee.item_get(weap)
				attachee.item_wield_best_all()
			elif sizeCat > STAT_SIZE_MEDIUM and attachee.distance_to(weap) <= 17:
				attachee.item_get(weap)
				attachee.item_wield_best_all()
	if nothing(attachee):
		get_melee_strategy(attachee)
		return
	else:
		attachee.critter_flag_unset( OCF_UNUSED_00000400 )
		if attachee.has_feat(feat_quick_draw):
			get_melee_strategy(attachee)
			attachee.float_mesfile_line( 'mes\\skill_ui.mes', 199 )
		elif attachee.has_feat(feat_combat_expertise):
			attachee.obj_set_int( obj_f_critter_strategy, 54)
			attachee.float_mesfile_line( 'mes\\skill_ui.mes', 654 )
		else:
			attachee.obj_set_int( obj_f_critter_strategy, 55)
			attachee.float_mesfile_line( 'mes\\skill_ui.mes', 655 )
	return

def get_lvl(attachee):
	lvl = 0
	la = attachee.stat_level_get(stat_level_cleric)
	lb = attachee.stat_level_get(stat_level_paladin)
	lc = attachee.stat_level_get(stat_level_ranger)
	ld = attachee.stat_level_get(stat_level_druid)
	le = attachee.stat_level_get(stat_level_barbarian)
	lf = attachee.stat_level_get(stat_level_monk)
	lg = attachee.stat_level_get(stat_level_rogue)
	li = attachee.stat_level_get(stat_level_bard)
	lj = attachee.stat_level_get(stat_level_wizard)
	lk = attachee.stat_level_get(stat_level_sorcerer)
	lh = attachee.stat_level_get(stat_level_fighter)
	lvl = (la + lb + lc + ld + le + lf + lg + lh + li + lj + lk)
	return lvl

def i_should_run(attachee):
	p = 0
	q = 0
	for co_com in game.obj_list_vicinity(attachee.location,OLC_NPC):
		if (co_com.is_friendly( attachee ) and (critter_is_unconscious(co_com) == 1 or co_com.stat_level_get( stat_hp_current ) < -8)):
			p = p + 1
		else:
			p = p - 1
	q = game.random_range(1,8)
	q = q + 2
	if p > q:
		return 1
	return 0

def run_away(attachee):
	attachee.condition_add_with_args( 'sp-Fear', 0, 100, 0 )
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
		attachee.reaction_set( pc, 30 )
	attachee.npc_flag_unset(ONF_KOS)
	attachee.npc_flag_set(ONF_KOS_OVERRIDE)
	attachee.remove_from_initiative()
	game.update_combat_ui()
	return

def speaks_drac(speaker):
	if speaker.stat_level_get(stat_level_wizard) >= 1:
		return 1
	elif speaker.stat_level_get(stat_race) == race_gnome or speaker.stat_level_get(stat_race) == race_halforc or speaker.stat_level_get(stat_race) == race_elf:
		return 1
	elif ((speaker.stat_level_get(stat_race) == race_halfling and speaker.skill_level_get(skill_decipher_script) >= 3) or (speaker.stat_level_get(stat_race) == race_halfelf and speaker.skill_level_get(skill_decipher_script) >= 5) or (speaker.stat_level_get(stat_race) == race_dwarf and speaker.skill_level_get(skill_decipher_script) >= 2) or (speaker.stat_level_get(stat_race) == race_human and speaker.skill_level_get(skill_decipher_script) >= 6)):
		return 1
	else:
		return 0

def speaks_goblin(speaker):
	if (speaker.stat_level_get(stat_race) == race_halfelf and speaker.skill_level_get(skill_decipher_script) < 1) or (speaker.stat_level_get(stat_race) == race_human and speaker.skill_level_get(skill_decipher_script) < 2):
		return 0
	else:
		return 1

def speaks_orc(speaker):
	if (speaker.stat_level_get(stat_race) == race_halfelf and speaker.skill_level_get(skill_decipher_script) < 2) or (speaker.stat_level_get(stat_race) == race_human and speaker.skill_level_get(skill_decipher_script) < 3):
		return 0
	else:
		return 1

def bard_know(triggerer, dc):
	take20 = game.random_range(1,20)
	lev = triggerer.stat_level_get(stat_level_bard)
	lev = lev + triggerer.stat_level_get(stat_int_mod)
	lev = lev + take20
	if lev >= dc:
		return 1
	else:
		return 0


def is_married( obj , who_is_spouse__option = -1):
	# DESCRIPTION:
	#   This function determines whether obj is married.
	#	Optionally, it also returns the spouse's name ID. (If there is more than 1 spouse, it returns 999)
	# Inputs:
	#     obj - should be a PC's object handle
	#     who_is_spouse__option - by default is -1
	#          if you wish to return the name ID of the spouse (instead of 0 or 1), change this variable to something else
	#          e.g. if obj is married to Fruella, it will return her name ID - 8067
	#          if obj is married to more than one person, it will return 999 :)
	# Example usage in dialogue:
	#      {11}{Sorry ma'am, I'm already married.}{}{1}{is_married(pc, 1) != 0 and is_married(pc, 1) != 8067 and is_married(pc, 1) != 999}{20}{}
	#      {12}{I would never betray my beloved Fruella!}{}{1}{is_married(pc, 1) == 8067}{40}{}
	#	   {13}{I'm gonna fuck all y'all! Yeehaw!}{}{1}{is_married(pc, 1) == 999}{60}{}
	marriage_array = []
	for npc in game.party:
		if npc.leader_get() == obj and npc.name in [8015, 8020, 8057, 8067]:
			# 8015 - Meleny
			# 8020 - Bertram
			# 8057 - Bertram (straight version)
			# 8067 - Fruella
			marriage_array+= [npc.name,]

	if len(marriage_array) == 0:
		return 0
	elif who_is_spouse__option == -1:
		return 1
	elif len(marriage_array) == 1:
		return marriage_array[0]
	else:
		return 999
	return 0
