from toee import *
from utilities import *
from py00439script_daemon import record_time_stamp
from combat_standard_routines import *


def san_insert_item( attachee, triggerer ):
	if ((triggerer.name == 1203) and (game.global_flags[109] == 0)):
		record_time_stamp(512)
		game.char_ui_hide()
		attachee.destroy()
		game.global_flags[109] = 1
		game.particles( "DesecrateEarth", triggerer )
		for npc in game.obj_list_vicinity(location_from_axis(484, 400), OLC_NPC):
			if npc.name in [14337, 14381] and npc.leader_get() == OBJ_HANDLE_NULL: # earth temple guards
				npc.attack(game.leader)
		for npc in game.obj_list_vicinity(location_from_axis(484, 424), OLC_NPC):
			if npc.name in [14337, 14381, 14296] and npc.leader_get() == OBJ_HANDLE_NULL: # earth temple guards
				npc.attack(game.leader)
	return RUN_DEFAULT
