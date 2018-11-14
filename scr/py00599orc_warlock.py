from utilities import *
from toee import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	webbed = break_free( attachee, 3)
	if (game.party_npc_size() + game.party_pc_size() == 8):
		if (attachee.distance_to(game.party[0]) <= 15 or attachee.distance_to(game.party[1]) <= 15 or attachee.distance_to(game.party[2]) <= 15 or attachee.distance_to(game.party[3]) <= 15 or attachee.distance_to(game.party[4]) <= 15 or attachee.distance_to(game.party[5]) <= 15 or attachee.distance_to(game.party[6]) <= 15 or attachee.distance_to(game.party[7]) <= 15):
			if (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
		elif (attachee.distance_to(game.party[0]) >= 16 and attachee.distance_to(game.party[1]) >= 16 and attachee.distance_to(game.party[2]) >= 16 and attachee.distance_to(game.party[3]) >= 16 and attachee.distance_to(game.party[4]) >= 16 and attachee.distance_to(game.party[5]) >= 16 and attachee.distance_to(game.party[6]) >= 16 and attachee.distance_to(game.party[7]) >= 16):
			if (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
	elif (game.party_npc_size() + game.party_pc_size() == 7):
		if (attachee.distance_to(game.party[0]) <= 15 or attachee.distance_to(game.party[1]) <= 15 or attachee.distance_to(game.party[2]) <= 15 or attachee.distance_to(game.party[3]) <= 15 or attachee.distance_to(game.party[4]) <= 15 or attachee.distance_to(game.party[5]) <= 15 or attachee.distance_to(game.party[6]) <= 15):
			if (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
		elif (attachee.distance_to(game.party[0]) >= 16 and attachee.distance_to(game.party[1]) >= 16 and attachee.distance_to(game.party[2]) >= 16 and attachee.distance_to(game.party[3]) >= 16 and attachee.distance_to(game.party[4]) >= 16 and attachee.distance_to(game.party[5]) >= 16 and attachee.distance_to(game.party[6]) >= 16):
			if (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
	elif (game.party_npc_size() + game.party_pc_size() == 6):
		if (attachee.distance_to(game.party[0]) <= 15 or attachee.distance_to(game.party[1]) <= 15 or attachee.distance_to(game.party[2]) <= 15 or attachee.distance_to(game.party[3]) <= 15 or attachee.distance_to(game.party[4]) <= 15 or attachee.distance_to(game.party[5]) <= 15):
			if (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
		elif (attachee.distance_to(game.party[0]) >= 16 and attachee.distance_to(game.party[1]) >= 16 and attachee.distance_to(game.party[2]) >= 16 and attachee.distance_to(game.party[3]) >= 16 and attachee.distance_to(game.party[4]) >= 16 and attachee.distance_to(game.party[5]) >= 16):
			if (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
	elif (game.party_npc_size() + game.party_pc_size() == 5):
		if (attachee.distance_to(game.party[0]) <= 15 or attachee.distance_to(game.party[1]) <= 15 or attachee.distance_to(game.party[2]) <= 15 or attachee.distance_to(game.party[3]) <= 15 or attachee.distance_to(game.party[4]) <= 15):
			if (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
		elif (attachee.distance_to(game.party[0]) >= 16 and attachee.distance_to(game.party[1]) >= 16 and attachee.distance_to(game.party[2]) >= 16 and attachee.distance_to(game.party[3]) >= 16 and attachee.distance_to(game.party[4]) >= 16):
			if (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
	elif (game.party_npc_size() + game.party_pc_size() == 4):
		if (attachee.distance_to(game.party[0]) <= 15 or attachee.distance_to(game.party[1]) <= 15 or attachee.distance_to(game.party[2]) <= 15 or attachee.distance_to(game.party[3]) <= 15):
			if (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
		elif (attachee.distance_to(game.party[0]) >= 16 and attachee.distance_to(game.party[1]) >= 16 and attachee.distance_to(game.party[2]) >= 16 and attachee.distance_to(game.party[3]) >= 16):
			if (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
	elif (game.party_npc_size() + game.party_pc_size() == 3):
		if (attachee.distance_to(game.party[0]) <= 15 or attachee.distance_to(game.party[1]) <= 15 or attachee.distance_to(game.party[2]) <= 15):
			if (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
		elif (attachee.distance_to(game.party[0]) >= 16 and attachee.distance_to(game.party[1]) >= 16 and attachee.distance_to(game.party[2]) >= 16):
			if (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
	elif (game.party_npc_size() + game.party_pc_size() == 2):
		if (attachee.distance_to(game.party[0]) <= 15 or attachee.distance_to(game.party[1]) <= 15):
			if (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
		elif (attachee.distance_to(game.party[0]) >= 16 and attachee.distance_to(game.party[1]) >= 16):
			if (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
	elif (game.party_npc_size() + game.party_pc_size() == 1):
		if (attachee.distance_to(game.party[0]) <= 15):
			if (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
		elif (attachee.distance_to(game.party[0]) >= 16):
			if (game.global_vars[971] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 391)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 498)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 499)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 500)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 501)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 502)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 503)
				game.global_vars[500] = 2
			elif (game.global_vars[971] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 504)
				game.global_vars[500] = 2
			elif (game.global_vars[784] == 0):
				attachee.obj_set_int(obj_f_critter_strategy, 505)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 506)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 507)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 508)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 509)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 5):
				attachee.obj_set_int(obj_f_critter_strategy, 510)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 6):
				attachee.obj_set_int(obj_f_critter_strategy, 511)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 7):
				attachee.obj_set_int(obj_f_critter_strategy, 512)
				game.global_vars[500] = 1
			elif (game.global_vars[784] == 8 and game.global_vars[971] == 8):
				attachee.obj_set_int(obj_f_critter_strategy, 513)
				game.global_vars[500] = 3
			elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
				attachee.obj_set_int(obj_f_critter_strategy, 514)
				game.global_vars[500] = 3
	return RUN_DEFAULT


def san_end_combat( attachee, triggerer ):
	if (game.global_vars[500] == 1):
		if (game.global_vars[784] == 0):
			game.global_vars[784] = 1
		elif (game.global_vars[784] == 1):
			game.global_vars[784] = 2
		elif (game.global_vars[784] == 2):
			game.global_vars[784] = 3
		elif (game.global_vars[784] == 3):
			game.global_vars[784] = 4
		elif (game.global_vars[784] == 4):
			game.global_vars[784] = 5
		elif (game.global_vars[784] == 5):
			game.global_vars[784] = 6
		elif (game.global_vars[784] == 6):
			game.global_vars[784] = 7
		elif (game.global_vars[784] == 7):
			game.global_vars[784] = 8
	elif (game.global_vars[500] == 2):
		if (game.global_vars[971] == 0):
			game.global_vars[971] = 1
		elif (game.global_vars[971] == 1):
			game.global_vars[971] = 2
		elif (game.global_vars[971] == 2):
			game.global_vars[971] = 3
		elif (game.global_vars[971] == 3):
			game.global_vars[971] = 4
		elif (game.global_vars[971] == 4):
			game.global_vars[971] = 5
		elif (game.global_vars[971] == 5):
			game.global_vars[971] = 6
		elif (game.global_vars[971] == 6):
			game.global_vars[971] = 7
		elif (game.global_vars[971] == 7):
			game.global_vars[971] = 8
	elif (game.global_vars[500] == 3):
		if (game.global_vars[784] == 8 and game.global_vars[971] == 8):
			game.global_vars[784] = 9
			game.global_vars[971] = 9
		elif (game.global_vars[784] == 9 and game.global_vars[971] == 9):
			game.global_vars[784] = 10
			game.global_vars[971] = 10
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_flags[571] == 1):
		attachee.unconceal()
		game.timevent_add( cast_buff, ( attachee, triggerer ), 4000 )
		game.new_sid = 0
	return RUN_DEFAULT


def cast_buff( attachee, triggerer ):
	attachee.cast_spell(spell_shield_of_faith, attachee)
	return