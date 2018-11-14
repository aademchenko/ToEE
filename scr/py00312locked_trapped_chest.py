from utilities import *
from toee import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	if (attachee.map == 5002):  ####  This is to replace thieves tools
		create_item_in_inventory ( 12012, triggerer )
		attachee.destroy()
		return SKIP_DEFAULT
	if (attachee.map == 5001):
		obj = find_npc_near(triggerer,20005)
		if (obj != OBJ_HANDLE_NULL and game.global_vars[705] != 2):
			triggerer.begin_dialog(obj,330)
			return SKIP_DEFAULT
	return RUN_DEFAULT



def san_heartbeat( attachee, triggerer ):
	if (attachee.map == 5066): 
		for obj in game.obj_list_vicinity(attachee.location,OLC_NPC):
			if (obj.name == 14079):
				loc = obj.location
				rot = obj.rotation
				obj.destroy()
				newNPC = game.obj_create( 14631, loc )
				newNPC.rotation = rot
			if (obj.name == 14080):
				loc = obj.location
				rot = obj.rotation
				obj.destroy()
				newNPC = game.obj_create( 14632, loc )
				newNPC.rotation = rot
			if (obj.name == 14186):
				loc = obj.location
				rot = obj.rotation
				obj.destroy()
				newNPC = game.obj_create( 14636, loc )
				newNPC.rotation = rot
				newNPC = game.obj_create( 14636, loc )
				newNPC.rotation = rot
		attachee.destroy()
	return RUN_DEFAULT
