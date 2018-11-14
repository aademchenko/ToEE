from toee import *
from utilities import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 90 )
	else:
		triggerer.turn_towards(attachee)
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_enter_combat( attachee, triggerer ):
	leader = attachee.leader_get()
	leader.follower_remove(attachee)
	game.particles( "CounterSpell", attachee )
	game.sound( 4016, 1 )
	game.global_vars[989] = 2
	attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	asaph = find_npc_near(attachee,14781)
	game.particles( "CounterSpell", asaph )
	game.sound( 4016, 1 )
	game.global_vars[989] = 3
	asaph.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	return


def san_join( attachee, triggerer ):
	cloak = attachee.item_find( 6269 )
	cloak.item_flag_set(OIF_NO_TRANSFER)
	armor = attachee.item_find( 6047 )
	armor.item_flag_set(OIF_NO_TRANSFER)
	boots = attachee.item_find( 6020 )
	boots.item_flag_set(OIF_NO_TRANSFER)
	gloves = attachee.item_find( 6021 )
	gloves.item_flag_set(OIF_NO_TRANSFER)
	helm = attachee.item_find( 6035 )
	helm.item_flag_set(OIF_NO_TRANSFER)
	shield = attachee.item_find( 6499 )
	shield.item_flag_set(OIF_NO_TRANSFER)
	sword = attachee.item_find( 4037 )
	sword.item_flag_set(OIF_NO_TRANSFER)
	return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	game.particles( "CounterSpell", attachee )
	game.sound( 4016, 1 )
	game.global_vars[989] = 5
	attachee.object_flag_set(OF_OFF)
	return SKIP_DEFAULT


def san_new_map( attachee, triggerer ):
	if (attachee.map == 5192 or attachee.map == 5193):
		game.leader.begin_dialog( attachee, 80 )
	elif (attachee.map != 5093 and attachee.map != 5192 and attachee.map != 5193):
		leader = attachee.leader_get()
		leader.follower_remove(attachee)
		game.particles( "CounterSpell", attachee )
		game.sound( 4016, 1 )
		game.global_vars[989] = 4
		attachee.object_flag_set(OF_OFF)
	return SKIP_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_safe_to_talk(attachee,obj)):
				if (not attachee.has_met(obj)):
					attachee.turn_towards(obj)
					obj.begin_dialog(attachee,1)
					game.new_sid = 0
	return RUN_DEFAULT


def kill_asaph( attachee, triggerer ):
	game.particles( "CounterSpell", attachee )
	game.global_vars[989] = 1
	attachee.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	return


def kill_asaph_guards( attachee, triggerer ):
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	guard = find_npc_near(attachee,14716)
	game.particles( "CounterSpell", guard )
	guard.object_flag_set(OF_OFF)
	return