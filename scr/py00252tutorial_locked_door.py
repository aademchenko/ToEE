from toee import *
from combat_standard_routines import *


def san_unlock_attempt( attachee, triggerer ):
	if not game.tutorial_is_active():
		game.tutorial_toggle()
	game.tutorial_show_topic( TAG_TUT_LOCKED_DOOR_REMINDER )
	#game.new_sid = 0
	return SKIP_DEFAULT