#### Added by Ranth for High Level Expansion
from toee import *
from utilities import *
from co8 import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if (attachee.name == 8755):
		destroy_gear( attachee, triggerer )
		game.global_vars[511] = game.global_vars[511] + 1
		if (game.global_vars[511] >= 24 and game.global_flags[501] == 1):
			game.global_flags[511] = 1
			if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
				game.quests[97].state = qs_completed
				game.party[0].reputation_add( 52 )
				game.global_vars[501] = 7
			else:
				game.sound( 4132, 2 )
	if (attachee.name == 8756):
		destroy_gear( attachee, triggerer )
		game.global_vars[512] = game.global_vars[512] + 1
		if (game.global_vars[512] >= 24):
			game.global_flags[512] = 1
			if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
				game.quests[97].state = qs_completed
				game.party[0].reputation_add( 52 )
				game.global_vars[501] = 7
			else:
				game.sound( 4132, 2 )
	if (attachee.name == 8757):
		destroy_gear( attachee, triggerer )
		game.global_vars[513] = game.global_vars[513] + 1
		if (game.global_vars[513] >= 24):
			game.global_flags[513] = 1
			if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
				game.quests[97].state = qs_completed
				game.party[0].reputation_add( 52 )
				game.global_vars[501] = 7
			else:
				game.sound( 4132, 2 )
	if (attachee.name == 8758):
		destroy_gear( attachee, triggerer )
		game.global_vars[514] = game.global_vars[514] + 1
		if (game.global_vars[514] >= 24):
			game.global_flags[514] = 1
			if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
				game.quests[97].state = qs_completed
				game.party[0].reputation_add( 52 )
				game.global_vars[501] = 7
			else:
				game.sound( 4132, 2 )
	if (attachee.name == 8759):
		destroy_gear( attachee, triggerer )
		game.global_vars[515] = game.global_vars[515] + 1
		if (game.global_vars[515] >= 24):
			game.global_flags[515] = 1
			if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
				game.quests[97].state = qs_completed
				game.party[0].reputation_add( 52 )
				game.global_vars[501] = 7
			else:
				game.sound( 4132, 2 )
	if (attachee.name == 8749):
		destroy_gear( attachee, triggerer )
		game.global_vars[516] = game.global_vars[516] + 1
		if (game.global_vars[516] >= 12):
			game.global_flags[516] = 1
			if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
				game.quests[97].state = qs_completed
				game.party[0].reputation_add( 52 )
				game.global_vars[501] = 7
			else:
				game.sound( 4132, 2 )
	if (attachee.name == 8750):
		destroy_gear( attachee, triggerer )
		game.global_vars[517] = game.global_vars[517] + 1
		if (game.global_vars[517] >= 12):
			game.global_flags[517] = 1
			if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
				game.quests[97].state = qs_completed
				game.party[0].reputation_add( 52 )
				game.global_vars[501] = 7
			else:
				game.sound( 4132, 2 )
	if (attachee.name == 8751):
		destroy_gear( attachee, triggerer )
		game.global_vars[518] = game.global_vars[518] + 1
		if (game.global_vars[518] >= 12):
			game.global_flags[518] = 1
			if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
				game.quests[97].state = qs_completed
				game.party[0].reputation_add( 52 )
				game.global_vars[501] = 7
			else:
				game.sound( 4132, 2 )
	if (attachee.name == 8752):
		destroy_gear( attachee, triggerer )
		game.global_vars[519] = game.global_vars[519] + 1
		if (game.global_vars[519] >= 12):
			game.global_flags[519] = 1
			if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
				game.quests[97].state = qs_completed
				game.party[0].reputation_add( 52 )
				game.global_vars[501] = 7
			else:
				game.sound( 4132, 2 )
	if (attachee.name == 8760):
		destroy_gear( attachee, triggerer )
		game.global_vars[520] = game.global_vars[520] + 1
		if (game.global_vars[520] >= 5):
			game.global_flags[520] = 1
			if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
				game.quests[97].state = qs_completed
				game.party[0].reputation_add( 52 )
				game.global_vars[501] = 7
			else:
				game.sound( 4132, 2 )
	if (attachee.name == 8761):
		destroy_gear( attachee, triggerer )
		game.global_vars[521] = game.global_vars[521] + 1
		if (game.global_vars[521] >= 6):
			game.global_flags[521] = 1
			if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
				game.quests[97].state = qs_completed
				game.party[0].reputation_add( 52 )
				game.global_vars[501] = 7
			else:
				game.sound( 4132, 2 )
	if (attachee.name == 8762):
		destroy_gear( attachee, triggerer )
		game.global_vars[522] = game.global_vars[522] + 1
		if (game.global_vars[522] >= 6):
			game.global_flags[522] = 1
			if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
				game.quests[97].state = qs_completed
				game.party[0].reputation_add( 52 )
				game.global_vars[501] = 7
			else:
				game.sound( 4132, 2 )
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (game.global_vars[505] == 0):
		game.timevent_add( out_of_time, ( attachee, triggerer ), 7200000 )	# 2 hours
		game.global_vars[505] = 1
	if (not attachee.has_wielded(4500) or not attachee.has_wielded(4126)):
		attachee.item_wield_best_all()
	if (triggerer.type == obj_t_pc):
		if anyone( triggerer.group_list(), "has_follower", 8736 ):
			wakefield = find_npc_near( triggerer, 8736 )
			if (wakefield != OBJ_HANDLE_NULL):
				triggerer.follower_remove(wakefield)
				wakefield.float_line( 20000,triggerer )
				wakefield.attack(triggerer)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.quests[97].state == qs_botched):
		attachee.object_flag_set(OF_OFF)
	elif (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6):
		if (game.combat_is_active()):
			if (not attachee.has_wielded(4161) or not attachee.has_wielded(4245)):
				attachee.item_wield_best_all()
#				game.new_sid = 0
	return RUN_DEFAULT


def san_will_kos( attachee, triggerer ):
	if (game.global_flags[525] == 1):
		return SKIP_DEFAULT
	else:
		return RUN_DEFAULT


def destroy_gear( attachee, triggerer ):
	assassin_mithrilshirt = attachee.item_find(6315)
	assassin_mithrilshirt.destroy()
	assassin_rapier = attachee.item_find(4500)
	assassin_rapier.destroy()
	assassin_shortsword = attachee.item_find(4126)
	assassin_shortsword.destroy()
	assassin_glovesdex = attachee.item_find(6200)
	assassin_glovesdex.destroy()
	return


def out_of_time( attachee, triggerer ):
	game.global_vars[505] = 3
	return