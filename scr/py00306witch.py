from utilities import *
from combat_standard_routines import *
from toee import *


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
		game.global_vars[729] = 0
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (game.global_flags[833] == 0 and attachee.map == 5065):
		for pc in game.party:
			if (pc.type == obj_t_pc):
				attachee.ai_shitlist_remove( pc )
		for obj in game.obj_list_vicinity(attachee.location,OLC_CRITTERS):
			if (obj.name == 8002 and obj.leader_get() != OBJ_HANDLE_NULL ):
				leader = obj.leader_get()
				leader.begin_dialog( obj, 266 )
		return SKIP_DEFAULT
	if (game.global_flags[839] == 1 and attachee.map == 5065 and game.global_flags[840] == 0):
		for pc in game.party:
			if (pc.type == obj_t_pc):
				attachee.ai_shitlist_remove( pc )
		for obj in game.obj_list_vicinity(attachee.location,OLC_CRITTERS):
			if (obj.name == 14614 and obj.leader_get() != OBJ_HANDLE_NULL ):
				leader = obj.leader_get()
				leader.begin_dialog( obj, 400 )
				return SKIP_DEFAULT
		if (game.global_flags[847] == 1):
			target = game.obj_create( 14617, location_from_axis (479L, 489L))
			game.global_flags[841] = 0
			game.global_flags[847] = 0
			target.turn_towards(game.party[0])
			game.party[0].begin_dialog(target, 350)
		return SKIP_DEFAULT
	if (game.global_flags[840] == 1 and attachee.map == 5065):
#		game.global_flags[840] = 0
		game.global_flags[849] = 1
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	if ((game.global_flags[833] == 0 and attachee.map == 5065 and game.global_flags[835] == 0 and game.global_flags[849] == 0) or (game.global_flags[839] == 1 and attachee.map == 5065 and game.global_flags[840] == 0 and game.global_flags[849] == 0)):
		return SKIP_DEFAULT
	if (game.global_vars[711] == 0 and attachee.map == 5065):
		create_item_in_inventory( 8906, attachee )
		game.global_vars[711] = 1
	for obj in game.obj_list_vicinity(attachee.location,OLC_CRITTERS):
		curr = obj.stat_level_get( stat_hp_current )
		if (curr <= -10 and obj.distance_to(attachee) <= 10 and obj.leader_get() == OBJ_HANDLE_NULL and (obj.is_category_type( mc_type_humanoid ) or obj.is_category_type( mc_type_fey ) or obj.is_category_type( mc_type_giant ) or obj.is_category_type( mc_type_monstrous_humanoid ))):
			create_item_in_inventory( 8907, attachee )
			return RUN_DEFAULT
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[729] == 0 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active() and attachee.map != 5065):
		attachee.cast_spell(spell_endurance, attachee)
		attachee.spells_pending_to_memorized()
	if (game.global_vars[729] == 4 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active() and attachee.map != 5065):
		attachee.cast_spell(spell_endure_elements, attachee)
		attachee.spells_pending_to_memorized()
	if (game.global_vars[729] == 8 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active() and attachee.map != 5065):
		attachee.cast_spell(spell_owls_wisdom, attachee)
		attachee.spells_pending_to_memorized()
	game.global_vars[729] = game.global_vars[729] + 1
	return RUN_DEFAULT


def san_will_kos( attachee, triggerer ):
	if (game.global_flags[840] == 1 and attachee.map == 5065):
		return SKIP_DEFAULT
	return RUN_DEFAULT