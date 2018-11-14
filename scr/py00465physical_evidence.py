from toee import *
from utilities import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	if (attachee.name == 11009):
		game.global_vars[552] = game.global_vars[552] + 1
		if (game.global_vars[552] <= 1):
			game.global_vars[543] = game.global_vars[543] + 1
			check_evidence_rep_pan( attachee, triggerer )
		game.new_sid = 0
	elif (attachee.name == 11058):
		game.global_vars[553] = game.global_vars[553] + 1
		if (game.global_vars[553] <= 1):
			game.global_vars[544] = game.global_vars[544] + 1
			check_evidence_rep_bor( attachee, triggerer )
		game.new_sid = 0
	elif (attachee.name == 11099):
		game.global_vars[554] = game.global_vars[554] + 1
		if (game.global_vars[554] <= 1):
			game.global_vars[545] = game.global_vars[545] + 1
			check_evidence_rep_rak( attachee, triggerer )
		game.new_sid = 0
	elif (attachee.name == 11060):
		game.global_vars[553] = game.global_vars[553] + 1
		if (game.global_vars[553] <= 1):
			game.global_vars[544] = game.global_vars[544] + 1
			check_evidence_rep_bor( attachee, triggerer )
		attachee.destroy()
	elif (attachee.name == 11061):
		game.global_vars[554] = game.global_vars[554] + 1
		if (game.global_vars[554] <= 1):
			game.global_vars[545] = game.global_vars[545] + 1
			check_evidence_rep_rak( attachee, triggerer )
		attachee.destroy()
	elif (attachee.name == 11062):
		game.global_vars[552] = game.global_vars[552] + 1
		if (game.global_vars[552] <= 1):
			game.global_vars[543] = game.global_vars[543] + 1
			check_evidence_rep_pan( attachee, triggerer )
		attachee.destroy()
	return RUN_DEFAULT


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