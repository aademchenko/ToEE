from toee import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	game.global_vars[0] = game.global_vars[0] + 1
	print "Zombies dead=", game.global_vars[0]
	if game.global_vars[0] == 3:
		if game.tutorial_is_active():
			game.tutorial_toggle()
		game.tutorial_show_topic( TAG_TUT_LOOT_REMINDER )
		game.new_sid = 0
	return RUN_DEFAULT