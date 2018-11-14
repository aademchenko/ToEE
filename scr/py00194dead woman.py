from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog(attachee,1)
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
		if (critter_is_unconscious(obj) == 0):
			if (not attachee.has_met( obj )):
				attachee.turn_towards(obj)
				obj.begin_dialog(attachee,1)
			return RUN_DEFAULT
	return RUN_DEFAULT

	
	
def loot_murderous_thief( pc ):
	for obj in game.obj_list_vicinity(pc.location, OLC_NPC):
		if obj.name == 14323: # The murderous thief
			for item_number in [6043 ,6045 ,6046 ,4071 ,4096, 7001]:
				countt = 0
				while obj.item_find(item_number) != OBJ_HANDLE_NULL and countt <= 20: ## count <= added as failsafe (in case PC is overloaded and something freaky happens...)
					pc.item_get(obj.item_find(item_number) )
					countt += 1	
	game.fade(0,0,1010,0)
	start_game_with_quest(23)

