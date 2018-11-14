from toee import *

proto_table = {
feat_exotic_weapon_proficiency_bastard_sword: 4015,
feat_exotic_weapon_proficiency_dwarven_waraxe: 4063,
feat_exotic_weapon_proficiency_gnome_hooked_hammer: 4075,
feat_exotic_weapon_proficiency_orc_double_axe: 4062,
feat_exotic_weapon_proficiency_spike_chain: 4209,
feat_exotic_weapon_proficiency_shuriken: 4211,
feat_improved_critical_dagger: 4060,
feat_improved_critical_light_mace: 4071,
feat_improved_critical_club: 4074,
feat_improved_critical_halfspear: 4116,
feat_improved_critical_heavy_mace: 4068,
feat_improved_critical_morningstar: 4070,
feat_improved_critical_quarterstaff: 4110,
feat_improved_critical_shortspear: 4117,
feat_improved_critical_light_crossbow: 4096,
feat_improved_critical_dart: 4127,
feat_improved_critical_sling: 4115,
feat_improved_critical_heavy_crossbow: 4097,
feat_improved_critical_javelin: 4123,
feat_improved_critical_light_hammer: 4076,
feat_improved_critical_handaxe: 4067,
feat_improved_critical_short_sword: 4049,
feat_improved_critical_battleaxe: 4114,
feat_improved_critical_longsword: 4036,
feat_improved_critical_heavy_pick: 4069,
feat_improved_critical_rapier: 4009,
feat_improved_critical_scimitar: 4045,
feat_improved_critical_warhammer: 4077,
feat_improved_critical_falchion: 4026,
feat_improved_critical_heavy_flail: 4207,
feat_improved_critical_glaive: 4118,
feat_improved_critical_greataxe: 4064,
feat_improved_critical_greatclub: 4066,
feat_improved_critical_greatsword: 4010,
feat_improved_critical_guisarme: 4113,
feat_improved_critical_longspear: 4194,
feat_improved_critical_ranseur: 4119,
feat_improved_critical_scythe: 4072,
feat_improved_critical_shortbow: 4201,
feat_improved_critical_longbow: 4087,
feat_improved_critical_bastard_sword: 4015,
feat_improved_critical_dwarven_waraxe: 4063,
feat_improved_critical_gnome_hooked_hammer: 4075,
feat_improved_critical_orc_double_axe: 4062,
feat_improved_critical_spike_chain: 4209,
feat_improved_critical_shuriken: 4211,
feat_martial_weapon_proficiency_light_hammer: 4076,
feat_martial_weapon_proficiency_handaxe: 4067,
feat_martial_weapon_proficiency_short_sword: 4049,
feat_martial_weapon_proficiency_battleaxe: 4114,
feat_martial_weapon_proficiency_longsword: 4036,
feat_martial_weapon_proficiency_heavy_pick: 4069,
feat_martial_weapon_proficiency_rapier: 4009,
feat_martial_weapon_proficiency_scimitar: 4045,
feat_martial_weapon_proficiency_warhammer: 4077,
feat_martial_weapon_proficiency_falchion: 4026,
feat_martial_weapon_proficiency_heavy_flail: 4207,
feat_martial_weapon_proficiency_glaive: 4118,
feat_martial_weapon_proficiency_greataxe: 4064,
feat_martial_weapon_proficiency_greatclub: 4066,
feat_martial_weapon_proficiency_greatsword: 4010,
feat_martial_weapon_proficiency_guisarme: 4113,
feat_martial_weapon_proficiency_longspear: 4194,
feat_martial_weapon_proficiency_ranseur: 4119,
feat_martial_weapon_proficiency_scythe: 4072,
feat_martial_weapon_proficiency_shortbow: 4201,
feat_martial_weapon_proficiency_longbow: 4087,
feat_weapon_finesse_dagger: 4060,
feat_weapon_finesse_light_mace: 4071,
feat_weapon_finesse_club: 4074,
feat_weapon_finesse_halfspear: 4116,
feat_weapon_finesse_heavy_mace: 4068,
feat_weapon_finesse_morningstar: 4070,
feat_weapon_finesse_quarterstaff: 4110,
feat_weapon_finesse_shortspear: 4117,
feat_weapon_finesse_light_crossbow: 4096,
feat_weapon_finesse_dart: 4127,
feat_weapon_finesse_sling: 4115,
feat_weapon_finesse_heavy_crossbow: 4097,
feat_weapon_finesse_javelin: 4123,
feat_weapon_finesse_light_hammer: 4076,
feat_weapon_finesse_handaxe: 4067,
feat_weapon_finesse_short_sword: 4049,
feat_weapon_finesse_battleaxe: 4114,
feat_weapon_finesse_longsword: 4036,
feat_weapon_finesse_heavy_pick: 4069,
feat_weapon_finesse_rapier: 4009,
feat_weapon_finesse_scimitar: 4045,
feat_weapon_finesse_warhammer: 4077,
feat_weapon_finesse_falchion: 4026,
feat_weapon_finesse_heavy_flail: 4207,
feat_weapon_finesse_glaive: 4118,
feat_weapon_finesse_greataxe: 4064,
feat_weapon_finesse_greatclub: 4066,
feat_weapon_finesse_greatsword: 4010,
feat_weapon_finesse_guisarme: 4113,
feat_weapon_finesse_longspear: 4194,
feat_weapon_finesse_ranseur: 4119,
feat_weapon_finesse_scythe: 4072,
feat_weapon_finesse_shortbow: 4201,
feat_weapon_finesse_longbow: 4087,
feat_weapon_finesse_bastard_sword: 4015,
feat_weapon_finesse_dwarven_waraxe: 4063,
feat_weapon_finesse_gnome_hooked_hammer: 4075,
feat_weapon_finesse_orc_double_axe: 4062,
feat_weapon_finesse_spike_chain: 4209,
feat_weapon_finesse_shuriken: 4211,
feat_weapon_focus_dagger: 4060,
feat_weapon_focus_light_mace: 4071,
feat_weapon_focus_club: 4074,
feat_weapon_focus_halfspear: 4116,
feat_weapon_focus_heavy_mace: 4068,
feat_weapon_focus_morningstar: 4070,
feat_weapon_focus_quarterstaff: 4110,
feat_weapon_focus_shortspear: 4117,
feat_weapon_focus_light_crossbow: 4096,
feat_weapon_focus_dart: 4127,
feat_weapon_focus_sling: 4115,
feat_weapon_focus_heavy_crossbow: 4097,
feat_weapon_focus_javelin: 4123,
feat_weapon_focus_light_hammer: 4076,
feat_weapon_focus_handaxe: 4067,
feat_weapon_focus_short_sword: 4049,
feat_weapon_focus_battleaxe: 4114,
feat_weapon_focus_longsword: 4036,
feat_weapon_focus_heavy_pick: 4069,
feat_weapon_focus_rapier: 4009,
feat_weapon_focus_scimitar: 4045,
feat_weapon_focus_warhammer: 4077,
feat_weapon_focus_falchion: 4026,
feat_weapon_focus_heavy_flail: 4207,
feat_weapon_focus_glaive: 4118,
feat_weapon_focus_greataxe: 4064,
feat_weapon_focus_greatclub: 4066,
feat_weapon_focus_greatsword: 4010,
feat_weapon_focus_guisarme: 4113,
feat_weapon_focus_longspear: 4194,
feat_weapon_focus_ranseur: 4119,
feat_weapon_focus_scythe: 4072,
feat_weapon_focus_shortbow: 4201,
feat_weapon_focus_longbow: 4087,
feat_weapon_focus_bastard_sword: 4015,
feat_weapon_focus_dwarven_waraxe: 4063,
feat_weapon_focus_gnome_hooked_hammer: 4075,
feat_weapon_focus_orc_double_axe: 4062,
feat_weapon_focus_spike_chain: 4209,
feat_weapon_focus_shuriken: 4211
}


def san_use( attachee, triggerer ):
	container = attachee.substitute_inventory
	if ( container == OBJ_HANDLE_NULL ):
		container = attachee
	for pc in game.party:
		if (pc.stat_level_get(stat_level_barbarian) > 0):
			create_item_in_inventory( 6056, container )
			create_item_in_inventory( 4114, container )
		if (pc.stat_level_get(stat_level_bard) > 0):
			create_item_in_inventory( 6056, container )
			create_item_in_inventory( 4036, container )
		if (pc.stat_level_get(stat_level_cleric) > 0):
			create_item_in_inventory( 6047, container )
			create_item_in_inventory( 4071, container )
		if (pc.stat_level_get(stat_level_druid) > 0):
			create_item_in_inventory( 6216, container )
			create_item_in_inventory( 6217, container )
			create_item_in_inventory( 4045, container )
		if (pc.stat_level_get(stat_level_fighter) > 0):
			create_item_in_inventory( 6047, container )
			create_item_in_inventory( 4036, container )
		if (pc.stat_level_get(stat_level_monk) > 0):
			create_item_in_inventory( 6202, container )
			create_item_in_inventory( 6205, container )
			create_item_in_inventory( 4110, container )
		if (pc.stat_level_get(stat_level_paladin) > 0):
			create_item_in_inventory( 6047, container )
			create_item_in_inventory( 4036, container )
		if (pc.stat_level_get(stat_level_ranger) > 0):
			create_item_in_inventory( 6056, container )
			create_item_in_inventory( 4049, container )
		if (pc.stat_level_get(stat_level_rogue) > 0):
			create_item_in_inventory( 6013, container )
			create_item_in_inventory( 4060, container )
			create_item_in_inventory( 12012, container )
		if (pc.stat_level_get(stat_level_sorcerer) > 0):
			create_item_in_inventory( 4117, container )
			create_item_in_inventory( 6038, container )
			create_item_in_inventory( 6130, container )
		if (pc.stat_level_get(stat_level_wizard) > 0):
			create_item_in_inventory( 6038, container )
			create_item_in_inventory( 6130, container )
			create_item_in_inventory( 4110, container )
		for f in pc.feats:
			if ( proto_table.has_key(f) ):		
				proto = proto_table[f]
				create_item_in_inventory( proto, container )
	return RUN_DEFAULT
