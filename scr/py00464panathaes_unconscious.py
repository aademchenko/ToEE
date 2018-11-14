from toee import *
from utilities import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	if (game.global_flags[533] == 0):
		pan1 = find_npc_near( triggerer, 8791 )
		if (pan1 != OBJ_HANDLE_NULL):
			loc = triggerer.location
			npc = game.obj_create( 14818, loc )
			triggerer.begin_dialog(npc,200)
		pan2 = find_npc_near( triggerer, 8792 )
		if (pan2 != OBJ_HANDLE_NULL):
			loc = triggerer.location
			npc = game.obj_create( 14818, loc )
			triggerer.begin_dialog(npc,200)
		pan3 = find_npc_near( triggerer, 8793 )
		if (pan3 != OBJ_HANDLE_NULL):
			loc = triggerer.location
			npc = game.obj_create( 14818, loc )
			triggerer.begin_dialog(npc,200)
		pan4 = find_npc_near( triggerer, 8794 )
		if (pan4 != OBJ_HANDLE_NULL):
			loc = triggerer.location
			npc = game.obj_create( 14818, loc )
			triggerer.begin_dialog(npc,200)
		pan5 = find_npc_near( triggerer, 8795 )
		if (pan5 != OBJ_HANDLE_NULL):
			loc = triggerer.location
			npc = game.obj_create( 14818, loc )
			triggerer.begin_dialog(npc,200)
		pan6 = find_npc_near( triggerer, 8796 )
		if (pan6 != OBJ_HANDLE_NULL):
			loc = triggerer.location
			npc = game.obj_create( 14818, loc )
			triggerer.begin_dialog(npc,200)
		pan7 = find_npc_near( triggerer, 8797 )
		if (pan7 != OBJ_HANDLE_NULL):
			loc = triggerer.location
			npc = game.obj_create( 14818, loc )
			triggerer.begin_dialog(npc,200)
		pan8 = find_npc_near( triggerer, 8798 )
		if (pan8 != OBJ_HANDLE_NULL):
			loc = triggerer.location
			npc = game.obj_create( 14818, loc )
			triggerer.begin_dialog(npc,200)
	return SKIP_DEFAULT


def gather_panathaes( attachee, triggerer ):
	if (game.global_vars[539] == 1):
		pan1 = find_npc_near( triggerer, 8791 )
		triggerer.follower_add(pan1)
		game.global_vars[551] = 1
		for pc in game.party:
			pan1.ai_shitlist_remove( pc )
			pan1.reaction_set( pc, 50 )
	elif (game.global_vars[539] == 2):
		pan2 = find_npc_near( triggerer, 8792 )
		triggerer.follower_add(pan2)
		game.global_vars[551] = 1
		for pc in game.party:
			pan2.ai_shitlist_remove( pc )
			pan2.reaction_set( pc, 50 )
	elif (game.global_vars[539] == 3):
		pan3 = find_npc_near( triggerer, 8793 )
		triggerer.follower_add(pan3)
		game.global_vars[551] = 1
		for pc in game.party:
			pan3.ai_shitlist_remove( pc )
			pan3.reaction_set( pc, 50 )
	elif (game.global_vars[539] == 4):
		pan4 = find_npc_near( triggerer, 8794 )
		triggerer.follower_add(pan4)
		game.global_vars[551] = 1
		for pc in game.party:
			pan4.ai_shitlist_remove( pc )
			pan4.reaction_set( pc, 50 )
	elif (game.global_vars[539] == 5):
		pan5 = find_npc_near( triggerer, 8795 )
		triggerer.follower_add(pan5)
		game.global_vars[551] = 1
		for pc in game.party:
			pan5.ai_shitlist_remove( pc )
			pan5.reaction_set( pc, 50 )
	elif (game.global_vars[539] == 6):
		pan6 = find_npc_near( triggerer, 8796 )
		triggerer.follower_add(pan6)
		game.global_vars[551] = 1
		for pc in game.party:
			pan6.ai_shitlist_remove( pc )
			pan6.reaction_set( pc, 50 )
	elif (game.global_vars[539] == 7):
		pan7 = find_npc_near( triggerer, 8797 )
		triggerer.follower_add(pan7)
		game.global_vars[551] = 1
		for pc in game.party:
			pan7.ai_shitlist_remove( pc )
			pan7.reaction_set( pc, 50 )
	elif (game.global_vars[539] == 8):
		pan8 = find_npc_near( triggerer, 8798 )
		triggerer.follower_add(pan8)
		game.global_vars[551] = 1
		for pc in game.party:
			pan8.ai_shitlist_remove( pc )
			pan8.reaction_set( pc, 50 )
	return RUN_DEFAULT


def increment_var_543( attachee, triggerer ):
	game.global_vars[543] = game.global_vars[543] + 1
	return


def increment_var_544( attachee, triggerer ):
	game.global_vars[544] = game.global_vars[544] + 1
	return


def increment_var_545( attachee, triggerer ):
	game.global_vars[545] = game.global_vars[545] + 1
	return


def increment_var_556( attachee, triggerer ):
	game.global_vars[556] = game.global_vars[556] + 1
	game.new_sid = 0
	return


def increment_var_557( attachee, triggerer ):
	game.global_vars[557] = game.global_vars[557] + 1
	game.new_sid = 0
	return


def check_evidence_rep_bor( attachee, triggerer ):
	if (game.party[0].reputation_has(72)==1):
		game.party[0].reputation_add(75)
		game.party[0].reputation_remove(72)
	elif (game.party[0].reputation_has(69)==1):
		game.party[0].reputation_add(72)
		game.party[0].reputation_remove(69)
	elif (game.party[0].reputation_has(69)==0):
		if (game.party[0].reputation_has(72)==0):
			if (game.party[0].reputation_has(75)==0):
				game.party[0].reputation_add(69)
	return


def check_evidence_rep_pan( attachee, triggerer ):
	if (game.party[0].reputation_has(73)==1):
		game.party[0].reputation_add(76)
		game.party[0].reputation_remove(73)
	elif (game.party[0].reputation_has(70)==1):
		game.party[0].reputation_add(73)
		game.party[0].reputation_remove(70)
	elif (game.party[0].reputation_has(70)==0):
		if (game.party[0].reputation_has(73)==0):
			if (game.party[0].reputation_has(76)==0):
				game.party[0].reputation_add(70)
	return


def check_evidence_rep_rak( attachee, triggerer ):
	if (game.party[0].reputation_has(74)==1):
		game.party[0].reputation_add(77)
		game.party[0].reputation_remove(74)
	elif (game.party[0].reputation_has(71)==1):
		game.party[0].reputation_add(74)
		game.party[0].reputation_remove(71)
	elif (game.party[0].reputation_has(71)==0):
		if (game.party[0].reputation_has(74)==0):
			if (game.party[0].reputation_has(77)==0):
				game.party[0].reputation_add(71)
	return