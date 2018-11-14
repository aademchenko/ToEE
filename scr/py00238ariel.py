from toee import *


def san_dialog( attachee, triggerer ):
	game.global_flags[10] = 0
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 110 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if game.global_flags[ 11 ] == 0:
		attachee.spells_memorized_forget()
		game.global_flags[ 11 ] =1
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	game.tutorial_show_topic( TAG_TUT_ARIEL_KILL )
	game.global_flags[11] = 1
	return RUN_DEFAULT


def san_join( attachee, triggerer ):
	if not game.tutorial_is_active():
		game.tutorial_toggle()
	game.tutorial_show_topic( TAG_TUT_MEMORIZE_SPELLS )
	game.global_flags[1] = 1
	return SKIP_DEFAULT