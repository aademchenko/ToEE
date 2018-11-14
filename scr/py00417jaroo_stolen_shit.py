from toee import *
from combat_standard_routines import *


def san_insert_item( attachee, triggerer ):
	game.timevent_add(check_theft, ( attachee, triggerer ), 1000 ) # 1 second
	return RUN_DEFAULT

#	gremag = find_npc_near( game.party[0], 8049 )
#	game.party[0].begin_dialog( gremag, 450 )
#	game.global_flags[500] = 1
#	return SKIP_DEFAULT


def check_theft( attachee, triggerer ):
	if (game.global_flags[243] == 1):
		game.global_flags[243] = 0
	elif (game.global_flags[243] == 0):
		if (triggerer.item_find(12661) != OBJ_HANDLE_NULL):
			triggerer.item_find(12661).destroy()
			create_item_in_inventory(12664,triggerer)
			game.global_flags[243] = 0
	return RUN_DEFAULT