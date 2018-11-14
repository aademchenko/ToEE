from toee import *
from combat_standard_routines import *


def san_insert_item( attachee, triggerer ):
	orb = triggerer.item_find(2203)
	if (orb != OBJ_HANDLE_NULL):
		triggerer.d20_send_signal(S_Golden_Skull_Combine,attachee)
		attachee.destroy()
	return SKIP_DEFAULT