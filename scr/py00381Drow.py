from utilities import *
from toee import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if (attachee.name == 14708):
		game.global_vars[999] += 1
		create_item_in_inventory( 6120, attachee )
	elif (attachee.name == 14724):
		game.global_vars[999] += 1
		create_item_in_inventory( 6120, attachee )
	elif (attachee.name == 14725):
		game.global_vars[999] += 1
		create_item_in_inventory( 6093, attachee )
	elif (attachee.name == 14726):
		game.global_vars[999] += 1
		create_item_in_inventory( 6334, attachee )
	elif (attachee.name == 14733):
		game.global_vars[999] += 1
	elif (attachee.name == 14734):
		game.global_vars[999] += 1
		create_item_in_inventory( 6120, attachee )
	elif (attachee.name == 14735):
		game.global_vars[999] += 1
		create_item_in_inventory( 6223, attachee )
	elif (attachee.name == 14736):
		game.global_vars[999] += 1
		create_item_in_inventory( 6334, attachee )
	elif (attachee.name == 14737):
		game.global_vars[999] += 1
	return RUN_DEFAULT