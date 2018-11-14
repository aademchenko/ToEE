from utilities import *
from combat_standard_routines import *
from toee import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		triggerer.begin_dialog(attachee,1)
		return SKIP_DEFAULT
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_exit_combat( attachee, triggerer ):
	game.timevent_add( set_up_intro, (), 5000 )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (attachee.leader_get() == OBJ_HANDLE_NULL):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_safe_to_talk(attachee,obj)):
					obj.begin_dialog(attachee,1)
					game.new_sid = 0
					return RUN_DEFAULT
	return RUN_DEFAULT


def set_up_intro():
	game.fade(0,0,1022,0)
	start_game_with_botched_quest(26)
	return RUN_DEFAULT