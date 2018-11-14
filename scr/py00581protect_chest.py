from toee import *
from combat_standard_routines import *
from utilities import *
from py00439script_daemon import can_see2


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_use( attachee, triggerer ):
	if (attachee.map == 5066): # temple level 1 - Earth altar chests
		attacking_temp = 0
		for npc in game.obj_list_vicinity(location_from_axis(484, 400), OLC_NPC):
			if npc.name in [14337, 14381] and npc.leader_get() == OBJ_HANDLE_NULL: # earth temple guards, elementals
				if can_see2(npc, triggerer):
					npc.attack(game.leader)
					attacking_temp = 1
		for npc in game.obj_list_vicinity(location_from_axis(484, 424), OLC_NPC):
			if npc.name in [14337, 14381, 14296] and npc.leader_get() == OBJ_HANDLE_NULL: # earth temple guards, elementals
				if can_see2(npc, triggerer):
					attacking_temp = 1
		if attacking_temp == 1:
			game.char_ui_hide()
			for npc in game.obj_list_vicinity(location_from_axis(484, 400), OLC_NPC):
				if npc.name in [14337, 14381] and npc.leader_get() == OBJ_HANDLE_NULL: # earth temple guards, elementals
					npc.attack(game.leader)
			for npc in game.obj_list_vicinity(location_from_axis(484, 424), OLC_NPC):
				if npc.name in [14337, 14381, 14296] and npc.leader_get() == OBJ_HANDLE_NULL: # earth temple guards, elementals		
					npc.attack(game.leader)
			return SKIP_DEFAULT
		else:
			return RUN_DEFAULT

	if (attachee.map == 5115):
		npc = find_npc_near(attachee,8803)
		if (npc != OBJ_HANDLE_NULL):
			npc.turn_towards(triggerer)
			npc.attack(triggerer)
	
	elif (attachee.map == 5191):
			npc = find_npc_near(attachee,14472)
			if (npc != OBJ_HANDLE_NULL):
				npc.turn_towards(triggerer)
				npc.attack(triggerer)
	
	game.new_sid = 0
	return SKIP_DEFAULT


def san_spell_cast( attachee, triggerer, spell ):

	if ( ( spell.spell == spell_knock ) or (spell.spell == spell_open_close) ):
		if (attachee.map == 5115):
			npc = find_npc_near(attachee,8803)
			if (npc != OBJ_HANDLE_NULL):
				npc.turn_towards(triggerer)
				npc.attack(triggerer)
		
		elif (attachee.map == 5191):
			npc = find_npc_near(attachee,14472)
			if (npc != OBJ_HANDLE_NULL):
				npc.turn_towards(triggerer)
				npc.attack(triggerer)
		
	return RUN_DEFAULT