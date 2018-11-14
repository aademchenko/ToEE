from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		if (game.global_flags[179] == 1):
			if (game.global_flags[180] == 1):
				triggerer.begin_dialog( attachee, 170 )
			else:
				triggerer.begin_dialog( attachee, 210 )
		else:
			triggerer.begin_dialog( attachee, 150 )
	elif ((game.global_flags[179] == 1) and (game.global_flags[180] == 0)):
		triggerer.begin_dialog( attachee, 120 )
	elif (not attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 1 )
	elif ((game.global_flags[179] == 1) and (game.global_flags[180] == 1)):
		triggerer.begin_dialog( attachee, 130 )
	else:
		triggerer.begin_dialog( attachee, 140 )
	return SKIP_DEFAULT


def san_enter_combat( attachee, triggerer ):
	attachee.float_line(12023,triggerer)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def change_to_demon( darley, pc, line ):
	if (game.global_flags[179] == 0):
		game.global_flags[179] = 1
		loc = darley.location
		rot = darley.rotation
		darley.destroy()
		new_darley = game.obj_create( 14421, loc )
		if (new_darley != OBJ_HANDLE_NULL):
			new_darley.rotation = rot
			if (line != -1):
				pc.begin_dialog(new_darley,line)
	return RUN_DEFAULT


def san_true_seeing( attachee, triggerer ):
	change_to_demon(attachee,triggerer)
	return RUN_DEFAULT