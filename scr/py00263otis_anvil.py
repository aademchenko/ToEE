from toee import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	if ((game.quests[32].state == qs_accepted) and (not(anyone( triggerer.group_list(), "has_follower", 8014 )))):
		game.quests[32].state = qs_completed
	elif (anyone( triggerer.group_list(), "has_follower", 8014 )):
#		otis = find_npc_near( triggerer, 8014 )
#		attachee.item_transfer_to( otis, 2202 )
#		attachee.item_transfer_to( otis, 3008 )
		mag_sword = attachee.item_find(2202)
		mag_sword.destroy()
		mag_armor = attachee.item_find(3008)
		mag_armor.destroy()
		amber = attachee.item_find(12040)
		amber.destroy()
		blue_sapphire = attachee.item_find(12038)
		blue_sapphire.destroy()
	return RUN_DEFAULT
