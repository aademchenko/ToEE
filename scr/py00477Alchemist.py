from toee import *
from utilities import *
from scripts import *
from InventoryRespawn import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.has_met( triggerer )):
		triggerer.begin_dialog( attachee, 100 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[897] == 0):
		game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
		game.global_flags[897] = 1
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def respawn(attachee):
	box = find_container_near(attachee,1078)
	RespawnInventory(box)
	game.timevent_add(respawn, (attachee), 86400000 ) #86400000ms is 24 hours
	return


def san_insert_item( attachee, triggerer ):
	cap1 = attachee.name
	cap2 = triggerer.item_worn_at(13)
	if cap2 != OBJ_HANDLE_NULL and cap2.name == cap1:
		if (not game.combat_is_active()):
			triggerer.float_mesfile_line( 'mes\\combat.mes', 6015 )
			holder = game.obj_create(1004, triggerer.location)
			holder.item_get(attachee)
			triggerer.item_get(attachee) 
			holder.destroy()
			game.char_ui_hide()
			return SKIP_DEFAULT
		else:
			game.timeevent_add( get_rid_of_it, ( attachee, triggerer ), 1000 )
	return RUN_DEFAULT


def get_rid_of_it(attachee, triggerer):
	cap1 = attachee.name
	cap2 = triggerer.item_worn_at(13)
	if cap2 != OBJ_HANDLE_NULL and cap2.name == cap1:
		attachee.destroy()
	# game.particles( "sp-summon monster I", game.party[0] )
	return