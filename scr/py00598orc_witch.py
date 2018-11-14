from utilities import *
from toee import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	webbed = break_free( attachee, 3)
	if (game.global_vars[785] == 1):
		attachee.obj_set_int(obj_f_critter_strategy, 516)
	elif (game.global_vars[785] == 2):
		attachee.obj_set_int(obj_f_critter_strategy, 517)
	elif (game.global_vars[785] == 3):
		attachee.obj_set_int(obj_f_critter_strategy, 518)
	elif (game.global_vars[785] == 4):
		attachee.obj_set_int(obj_f_critter_strategy, 519)
	elif (game.global_vars[785] == 5):
		attachee.obj_set_int(obj_f_critter_strategy, 520)
	elif (game.global_vars[785] == 6):
		attachee.obj_set_int(obj_f_critter_strategy, 521)
	elif (game.global_vars[785] == 7):
		attachee.obj_set_int(obj_f_critter_strategy, 522)
	elif (game.global_vars[785] == 8):
		attachee.obj_set_int(obj_f_critter_strategy, 523)
	elif (game.global_vars[785] == 9):
		attachee.obj_set_int(obj_f_critter_strategy, 524)
	elif (game.global_vars[785] == 10):
		attachee.obj_set_int(obj_f_critter_strategy, 525)
	elif (game.global_vars[785] == 11):
		attachee.obj_set_int(obj_f_critter_strategy, 526)
	elif (game.global_vars[785] == 12):
		attachee.obj_set_int(obj_f_critter_strategy, 527)
	elif (game.global_vars[785] == 13):
		attachee.obj_set_int(obj_f_critter_strategy, 528)
	elif (game.global_vars[785] == 14):
		attachee.obj_set_int(obj_f_critter_strategy, 529)
	elif (game.global_vars[785] == 15):
		attachee.obj_set_int(obj_f_critter_strategy, 530)
	elif (game.global_vars[785] == 16):
		attachee.obj_set_int(obj_f_critter_strategy, 531)
	elif (game.global_vars[785] >= 17):
		attachee.obj_set_int(obj_f_critter_strategy, 532)
	return RUN_DEFAULT


def san_end_combat( attachee, triggerer ):
	if (game.global_vars[785] == 0):
		game.global_vars[785] = 1
	elif (game.global_vars[785] == 1):
		game.global_vars[785] = 2
	elif (game.global_vars[785] == 2):
		game.global_vars[785] = 3
	elif (game.global_vars[785] == 3):
		game.global_vars[785] = 4
	elif (game.global_vars[785] == 4):
		game.global_vars[785] = 5
	elif (game.global_vars[785] == 5):
		game.global_vars[785] = 6
	elif (game.global_vars[785] == 6):
		game.global_vars[785] = 7
	elif (game.global_vars[785] == 7):
		game.global_vars[785] = 8
	elif (game.global_vars[785] == 8):
		game.global_vars[785] = 9
	elif (game.global_vars[785] == 9):
		game.global_vars[785] = 10
	elif (game.global_vars[785] == 10):
		game.global_vars[785] = 11
	elif (game.global_vars[785] == 11):
		game.global_vars[785] = 12
	elif (game.global_vars[785] == 12):
		game.global_vars[785] = 13
	elif (game.global_vars[785] == 13):
		game.global_vars[785] = 14
	elif (game.global_vars[785] == 14):
		game.global_vars[785] = 15
	elif (game.global_vars[785] == 15):
		game.global_vars[785] = 16
	elif (game.global_vars[785] == 16):
		game.global_vars[785] = 17
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_flags[571] == 1):
		attachee.unconceal()
		game.timevent_add( cast_buff, ( attachee, triggerer ), 4000 )
		game.new_sid = 0
	return RUN_DEFAULT


def cast_buff( attachee, triggerer ):
	attachee.cast_spell(spell_mirror_image, attachee)
	return