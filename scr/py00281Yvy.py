from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.leader.reputation_has(32) == 1 or game.leader.reputation_has(30) == 1 or game.leader.reputation_has(29) == 1):
		attachee.float_line(11004,triggerer)
	else:
		triggerer.begin_dialog( attachee, 1 )
	attachee.turn_towards(triggerer)
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_insert_item( attachee, triggerer ):
	done = attachee.obj_get_int( obj_f_weapon_pad_i_1 )
	if triggerer.has_feat(feat_far_shot):
		if done == 1:
			return RUN_DEFAULT
		else:
			curr = attachee.obj_get_int( obj_f_weapon_range )
			curr = curr * 2
			attachee.obj_set_int( obj_f_weapon_range, curr )
			attachee.obj_set_int( obj_f_weapon_pad_i_1, 1 )
			game.sound(3013,1)
	else:
		if done == 1:
			curr = attachee.obj_get_int( obj_f_weapon_range )
			curr = curr * 0.5
			attachee.obj_set_int( obj_f_weapon_range, curr )
			attachee.obj_set_int( obj_f_weapon_pad_i_1, 0 )
			game.sound(3013,1)
	return RUN_DEFAULT