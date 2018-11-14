#### Added by Ranth for High Level Expansion
from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		attachee.float_line(10000,triggerer)
	elif (game.party[0].reputation_has( 61 ) == 1):
		triggerer.begin_dialog( attachee, 1 )
	else:
       		triggerer.begin_dialog( attachee, 100 )
      	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		if should_modify_CR( attachee ):
			modify_CR( attachee, get_av_level() )
	game.global_flags[501] = 1
	game.global_vars[511] = game.global_vars[511] + 1
	if (game.global_vars[511] >= 12 and game.global_flags[501] == 1):
		game.global_flags[511] = 1
		if (game.global_flags[511] == 1 and game.global_flags[512] == 1 and game.global_flags[513] == 1 and game.global_flags[514] == 1 and game.global_flags[515] == 1 and game.global_flags[516] == 1 and game.global_flags[517] == 1 and game.global_flags[518] == 1 and game.global_flags[519] == 1 and game.global_flags[520] == 1 and game.global_flags[521] == 1 and game.global_flags[522] == 1):
			game.quests[97].state = qs_completed
			game.party[0].reputation_add( 52 )
			game.global_vars[501] = 7
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (game.global_vars[505] == 0):
		game.timevent_add( out_of_time, ( attachee, triggerer ), 7200000 )	# 2 hours
		game.global_vars[505] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[501] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.party[0].reputation_has( 61 ) == 1):
		if (attachee.leader_get() != OBJ_HANDLE_NULL):
			if (not game.combat_is_active()):
				leader = attachee.leader_get()
				leader.follower_remove(attachee)
				game.party[0].begin_dialog( attachee, 1 )
				game.new_sid = 0
			elif (leader == OBJ_HANDLE_NULL):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (is_better_to_talk(attachee, obj)):
						attachee.turn_towards(game.party[0])
						game.party[0].begin_dialog( attachee, 1 )
						game.new_sid = 0
	elif (game.quests[97].state == qs_botched):
		attachee.object_flag_set(OF_OFF)
	elif (game.global_vars[501] == 5):
		if (attachee.leader_get() == OBJ_HANDLE_NULL):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (is_better_to_talk(attachee, obj)):
						attachee.turn_towards(game.party[0])
						game.party[0].begin_dialog( attachee, 100 )
#						game.new_sid = 0
	elif (game.global_vars[501] == 4):
		if (attachee.leader_get() == OBJ_HANDLE_NULL):
			if (not game.combat_is_active()):
				game.sound( 4132, 2 )
				game.sound( 4136, 1 )
				game.shake(75,3200)
				if (game.global_vars[504] == 0):
					if (game.party_alignment == CHAOTIC_GOOD or game.party_alignment == CHAOTIC_NEUTRAL or game.party_alignment == CHAOTIC_EVIL):
						attachee.cast_spell(spell_magic_circle_against_chaos, attachee)
					else:
						attachee.cast_spell(spell_divine_power, attachee)
					game.global_vars[504] = 1
				game.timevent_add( set_var_501, ( attachee, triggerer ), 3000 )
	return RUN_DEFAULT


def san_join( attachee, triggerer ):
	game.global_flags[527] = 1
	rod = attachee.item_find( 4232 )
	rod.item_flag_set(OIF_NO_TRANSFER)
	armor = attachee.item_find( 6334 )
	armor.item_flag_set(OIF_NO_TRANSFER)
	boots = attachee.item_find( 6045 )
	boots.item_flag_set(OIF_NO_TRANSFER)
	gloves = attachee.item_find( 6046 )
	gloves.item_flag_set(OIF_NO_TRANSFER)
	helm = attachee.item_find( 6335 )
	helm.item_flag_set(OIF_NO_TRANSFER)
	shield = attachee.item_find( 6079 )
	shield.item_flag_set(OIF_NO_TRANSFER)
	cloak = attachee.item_find( 6233 )
	cloak.item_flag_set(OIF_NO_TRANSFER)
	return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	game.global_flags[527] = 0
	rod = attachee.item_find( 4232 )
	rod.item_flag_unset(OIF_NO_TRANSFER)
	armor = attachee.item_find( 6334 )
	armor.item_flag_unset(OIF_NO_TRANSFER)
	boots = attachee.item_find( 6045 )
	boots.item_flag_unset(OIF_NO_TRANSFER)
	gloves = attachee.item_find( 6046 )
	gloves.item_flag_unset(OIF_NO_TRANSFER)
	helm = attachee.item_find( 6335 )
	helm.item_flag_unset(OIF_NO_TRANSFER)
	shield = attachee.item_find( 6079 )
	shield.item_flag_unset(OIF_NO_TRANSFER)
	cloak = attachee.item_find( 6233 )
	cloak.item_flag_unset(OIF_NO_TRANSFER)
	return RUN_DEFAULT


def hextor_buff_2(attachee, triggerer):
	attachee.cast_spell(spell_righteous_might, attachee)
	for obj in game.obj_list_vicinity(attachee.location,OLC_NPC):
		if (obj.name == 8753):
			obj.cast_spell(spell_wind_wall, obj)
		if (obj.name == 8754):
			obj.cast_spell(spell_blur, obj)
	return


def set_var_501( attachee, triggerer ):
	game.global_vars[501] = 5
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 40):
			return 1
	return 0


def out_of_time( attachee, triggerer ):
	game.global_vars[505] = 3
	return


def run_off( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT


def flag_no_transfer( attachee, triggerer ):
	orb = attachee.item_find(2203)
	orb.item_flag_set(OIF_NO_TRANSFER)
	return RUN_DEFAULT


def td_attack( attachee, triggerer ):
	game.timevent_add( defense_attack, ( attachee, triggerer ), 6000 )
	return RUN_DEFAULT


def defense_attack( attachee, triggerer ):
	game.particles( "sp-Fireball-Hit", location_from_axis( 493, 469 ) )
	game.particles( "ef-fireburning", location_from_axis( 493, 469 ) )
	game.particles( "ef-FirePit", location_from_axis( 493, 469 ) )
	game.particles( "sp-Fireball-Hit", location_from_axis( 494, 461 ) )
	game.particles( "ef-fireburning", location_from_axis( 494, 461 ) )
	game.particles( "ef-FirePit", location_from_axis( 494, 461 ) )
	game.sound( 4136, 1 )
	game.shake(75,3200)
	game.timevent_add( defense_attack_followup, (), 12000 )
	return RUN_DEFAULT


def defense_attack_followup():
	if (not game.combat_is_active()):
		random_x = game.random_range(465,494)
		random_y = game.random_range(446,469)
		game.particles( "sp-Fireball-Hit", location_from_axis( random_x, random_y ) )
		game.particles( "ef-fireburning", location_from_axis( random_x, random_y ) )
		game.particles( "ef-FirePit", location_from_axis( random_x, random_y ) )
		game.sound( 4135, 1 )
		game.shake(50,1600)
		game.timevent_add( defense_attack_followup, (), 12000 )
	return RUN_DEFAULT