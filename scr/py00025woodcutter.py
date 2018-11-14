from toee import *
import _include
from co8Util.TimedEvent import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (game.quests[99].state == qs_completed or game.quests[99].state == qs_botched):
		triggerer.begin_dialog( attachee, 600 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
		attachee.object_flag_set(OF_OFF)
	else:
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_flags[875] == 1 and game.global_flags[876] == 0 and game.quests[99].state != qs_completed and not anyone( triggerer.group_list(), "has_item", 12900 )):
		game.global_flags[876] = 1
		game.timevent_add( amii_dies, (), 140000000 )
	return RUN_DEFAULT


def amii_dies():
	game.quests[99].state = qs_botched
	game.global_flags[862] = 1
	return RUN_DEFAULT


def letter_written():
	game.global_vars[767] = 2
	timedEventAdd(give_reward, (), 76)
	return RUN_DEFAULT


def give_reward():
	game.global_vars[767] = 3
	return RUN_DEFAULT


def order_item():
	game.global_vars[769] = 1
	timedEventAdd(item_arrived, (), 409)
	return RUN_DEFAULT


def item_arrived():
	game.global_vars[769] = 2
	return RUN_DEFAULT


def give_item(pc):
	game.global_vars[769] = 0
	item = game.global_vars[768]
	create_item_in_inventory(item,pc)
	game.global_vars[768] = 0
	game.global_vars[776] = game.global_vars[776] + 1
	return RUN_DEFAULT