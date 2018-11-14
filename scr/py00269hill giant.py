from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if (game.quests[100].state == qs_accepted):
		create_item_in_inventory ( 12602, attachee )
	if (game.quests[100].state == qs_mentioned):
		create_item_in_inventory ( 12602, attachee )
	if (game.quests[100].state == qs_unknown):
		create_item_in_inventory ( 12602, attachee )
	return RUN_DEFAULT

