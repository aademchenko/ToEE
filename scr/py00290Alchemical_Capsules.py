from toee import *
from utilities import *
from combat_standard_routines import *


def san_start_combat( attachee, triggerer ):
	# game.particles( "sp-summon monster I", game.party[0] )
	cap2 = attachee.item_worn_at(13)
	if cap2 != OBJ_HANDLE_NULL and (cap2.name == 12754 or cap2.name == 12755 or cap2.name == 12756 or cap2.name == 12757):
		scid = cap2.obj_get_int(obj_f_item_pad_i_1)
		game.new_sid = scid
		cap2.destroy()
		game.particles( 'sp-Fireball-Hit', attachee )
	return RUN_DEFAULT

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
			game.timeevent_add( get_rid_of_it, ( attachee ), 1000 )
	return RUN_DEFAULT

def get_rid_of_it(attachee):
	attachee.destroy()
	# game.particles( "sp-summon monster I", game.party[0] )
	return

def spare_stuff(attachee, triggerer):
	cap3 = triggerer.item_worn_at(11)
	if cap3 != OBJ_HANDLE_NULL and cap3.name == cap1:
		if not game.combat_is_active():
			triggerer.float_mesfile_line( 'mes\\combat.mes', 6015 )
			holder = game.obj_create(1004, triggerer.location)
			holder.item_get(attachee)
			triggerer.item_get(attachee) 
			holder.destroy()
			game.char_ui_hide()
			return RUN_DEFAULT
		else:
			game.timeevent_add( get_rid_of_it, ( attachee ), 1000 )
	cap4 = triggerer.item_worn_at(7)
	if cap4 != OBJ_HANDLE_NULL and cap4.name == cap1:
		if not game.combat_is_active():
			triggerer.float_mesfile_line( 'mes\\combat.mes', 6015 )
			holder = game.obj_create(1004, triggerer.location)
			holder.item_get(attachee)
			triggerer.item_get(attachee) 
			holder.destroy()
			game.char_ui_hide()
			return RUN_DEFAULT
		else:
			game.timeevent_add( get_rid_of_it, ( attachee ), 1000 )
	return