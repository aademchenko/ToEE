from toee import *
from combat_standard_routines import *


def san_insert_item( attachee, triggerer ):
	if ((triggerer.type == obj_t_pc) and (game.global_flags[341] == 0)):
		game.global_flags[341] = 1
		game.char_ui_hide()
		game.fade(2,0,303,0)
		burne = find_npc_near( triggerer, 8054 )
		if (burne != OBJ_HANDLE_NULL):
			triggerer.begin_dialog( burne, 470 )
	gem = triggerer.item_find(5808)
	if (gem != OBJ_HANDLE_NULL):
		triggerer.d20_send_signal(S_Golden_Skull_Combine,gem)
		gem.destroy()
	gem = triggerer.item_find(5809)
	if (gem != OBJ_HANDLE_NULL):
		triggerer.d20_send_signal(S_Golden_Skull_Combine,gem)
		gem.destroy()
	gem = triggerer.item_find(5810)
	if (gem != OBJ_HANDLE_NULL):
		triggerer.d20_send_signal(S_Golden_Skull_Combine,gem)
		gem.destroy()
	gem = triggerer.item_find(5811)
	if (gem != OBJ_HANDLE_NULL):
		triggerer.d20_send_signal(S_Golden_Skull_Combine,gem)
		gem.destroy()
	return SKIP_DEFAULT