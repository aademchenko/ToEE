from toee import *
from __main__ import game
from utilities import *
from Co8 import *


def qs():
	partyhpset(800)
	partyabset(1,40)
	partyabset(2,40)
	partyabset(3,40)
	partyabset(4,40)
	partyabset(5,40)
	partyabset(6,40)
	for pc in game.party:
		if (pc.stat_level_get(stat_level_cleric)):	# CLERIC
			create_item_in_inventory( 6396, pc )	# armor
			create_item_in_inventory( 6020, pc )	# boots
			create_item_in_inventory( 6021, pc )	# gloves
			create_item_in_inventory( 6018, pc )	# helm
			create_item_in_inventory( 6234, pc )	# cloak - white
			create_item_in_inventory( 6050, pc )	# shield
			create_item_in_inventory( 4109, pc )	# weapon
			create_item_in_inventory( 12625, pc )	# ring
			create_item_in_inventory( 6242, pc )	# amulet health
			create_item_in_inventory( 12089, pc )	# wand of cure critical
			create_item_in_inventory( 12089, pc )	# wand of cure critical
			create_item_in_inventory( 12089, pc )	# wand of cure critical
			create_item_in_inventory( 12379, pc )	# wand of raise dead
			pc.item_wield_best_all()
			pc.money_adj(2000000)
		if (pc.stat_level_get(stat_level_fighter)):	# FIGHTER
			create_item_in_inventory( 6104, pc )	# armor
			create_item_in_inventory( 6040, pc )	# boots
			create_item_in_inventory( 6041, pc )	# gloves
			create_item_in_inventory( 6033, pc )	# helm
			create_item_in_inventory( 6338, pc )	# cloak - blue
			create_item_in_inventory( 6050, pc )	# shield
			create_item_in_inventory( 4081, pc )	# weapon
			create_item_in_inventory( 12625, pc )	# ring
			create_item_in_inventory( 6242, pc )	# amulet health
			pc.item_wield_best_all()
			pc.money_adj(2000000)
		if (pc.stat_level_get(stat_level_paladin)):	# PALADIN
			create_item_in_inventory( 6104, pc )	# armor
			create_item_in_inventory( 6040, pc )	# boots
			create_item_in_inventory( 6041, pc )	# gloves
			create_item_in_inventory( 6035, pc )	# helm
			create_item_in_inventory( 6428, pc )	# cloak - violet
			create_item_in_inventory( 6050, pc )	# shield
			create_item_in_inventory( 4081, pc )	# weapon
			create_item_in_inventory( 12625, pc )	# ring
			create_item_in_inventory( 6242, pc )	# amulet health
			pc.item_wield_best_all()
			pc.money_adj(2000000)
		if (pc.stat_level_get(stat_level_barbarian)):	# BARBARIAN
			create_item_in_inventory( 6298, pc )	# armor
			create_item_in_inventory( 6011, pc )	# boots
			create_item_in_inventory( 6012, pc )	# gloves
			create_item_in_inventory( 6026, pc )	# helm
			create_item_in_inventory( 6124, pc )	# cloak - red
			create_item_in_inventory( 6059, pc )	# shield
			create_item_in_inventory( 4254, pc )	# weapon
			create_item_in_inventory( 12625, pc )	# ring
			create_item_in_inventory( 6242, pc )	# amulet health
			pc.item_wield_best_all()
			pc.money_adj(2000000)
		if (pc.stat_level_get(stat_level_druid)):	# DRUID
			create_item_in_inventory( 6306, pc )	# armor
			create_item_in_inventory( 6011, pc )	# boots
			create_item_in_inventory( 6012, pc )	# gloves
			create_item_in_inventory( 6217, pc )	# helm
			create_item_in_inventory( 6421, pc )	# cloak - fur
			create_item_in_inventory( 6064, pc )	# shield
			create_item_in_inventory( 4047, pc )	# weapon
			create_item_in_inventory( 12625, pc )	# ring
			create_item_in_inventory( 6242, pc )	# amulet health
			create_item_in_inventory( 12089, pc )	# wand of cure critical
			create_item_in_inventory( 12089, pc )	# wand of cure critical
			create_item_in_inventory( 12089, pc )	# wand of cure critical
			create_item_in_inventory( 12379, pc )	# wand of raise dead
			pc.item_wield_best_all()
			pc.money_adj(2000000)
		if (pc.stat_level_get(stat_level_ranger)):	# RANGER
			create_item_in_inventory( 6091, pc )	# armor
			create_item_in_inventory( 6011, pc )	# boots
			create_item_in_inventory( 6012, pc )	# gloves
								# helm
			create_item_in_inventory( 6269, pc )	# cloak - green
			create_item_in_inventory( 6059, pc )	# shield
			create_item_in_inventory( 4191, pc )	# weapon
			create_item_in_inventory( 12625, pc )	# ring
			create_item_in_inventory( 6242, pc )	# amulet health
			pc.item_wield_best_all()
			pc.money_adj(2000000)
		if (pc.stat_level_get(stat_level_bard)):	# BARD
			create_item_in_inventory( 6297, pc )	# armor
			create_item_in_inventory( 6023, pc )	# boots
			create_item_in_inventory( 6024, pc )	# gloves
			create_item_in_inventory( 6335, pc )	# helm
			create_item_in_inventory( 6427, pc )	# cloak - orange
			create_item_in_inventory( 6050, pc )	# shield
			create_item_in_inventory( 4126, pc )	# weapon
			create_item_in_inventory( 12625, pc )	# ring
			create_item_in_inventory( 6242, pc )	# amulet health
			create_item_in_inventory( 12587, pc )	# mw mandolin
			pc.item_wield_best_all()
			pc.money_adj(2000000)
		if (pc.stat_level_get(stat_level_rogue)):	# ROGUE
			create_item_in_inventory( 6299, pc )	# armor
			create_item_in_inventory( 6045, pc )	# boots
			create_item_in_inventory( 6046, pc )	# gloves
								# helm
			create_item_in_inventory( 6233, pc )	# cloak - black
			create_item_in_inventory( 6059, pc )	# shield
			create_item_in_inventory( 4126, pc )	# weapon
			create_item_in_inventory( 12625, pc )	# ring
			create_item_in_inventory( 6242, pc )	# amulet health
			create_item_in_inventory( 12013, pc )	# mw thieves tools
			pc.item_wield_best_all()
			pc.money_adj(2000000)
		if (pc.stat_level_get(stat_level_monk)):	# MONK
			create_item_in_inventory( 6115, pc )	# armor
			create_item_in_inventory( 6023, pc )	# boots
			create_item_in_inventory( 6024, pc )	# gloves
			create_item_in_inventory( 6025, pc )	# helm
			create_item_in_inventory( 6205, pc )	# robes - brown
								# shield
			create_item_in_inventory( 4427, pc )	# weapon
			create_item_in_inventory( 12625, pc )	# ring
			create_item_in_inventory( 6242, pc )	# amulet health
			pc.item_wield_best_all()
			pc.money_adj(2000000)
		if (pc.stat_level_get(stat_level_sorcerer)):	# SORCERER
			if (pc.stat_level_get( stat_gender ) == gender_female):	# FEMALE
				create_item_in_inventory( 6115, pc )		# armor
				create_item_in_inventory( 6045, pc )		# boots
				create_item_in_inventory( 6046, pc )		# gloves
										# helm
				create_item_in_inventory( 6637, pc )		# garb - red
										# shield
				create_item_in_inventory( 4242, pc )		# weapon
				create_item_in_inventory( 12625, pc )		# ring
				create_item_in_inventory( 6242, pc )		# amulet health
				create_item_in_inventory( 12262, pc )		# wand of knock
				create_item_in_inventory( 12238, pc )		# wand of identify
				create_item_in_inventory( 12581, pc )		# wand of fireball
				create_item_in_inventory( 12581, pc )		# wand of fireball
				create_item_in_inventory( 12581, pc )		# wand of fireball
				pc.item_wield_best_all()
				pc.money_adj(2000000)
			elif (pc.stat_level_get( stat_gender ) == gender_male):	# MALE
				create_item_in_inventory( 6115, pc )		# armor
				create_item_in_inventory( 6045, pc )		# boots
				create_item_in_inventory( 6046, pc )		# gloves
										# helm
				create_item_in_inventory( 6637, pc )		# garb - red
										# shield
				create_item_in_inventory( 4242, pc )		# weapon
				create_item_in_inventory( 12625, pc )		# ring
				create_item_in_inventory( 6242, pc )		# amulet health
				create_item_in_inventory( 12262, pc )		# wand of knock
				create_item_in_inventory( 12238, pc )		# wand of identify
				create_item_in_inventory( 12581, pc )		# wand of fireball
				create_item_in_inventory( 12581, pc )		# wand of fireball
				create_item_in_inventory( 12581, pc )		# wand of fireball
				pc.item_wield_best_all()
				pc.money_adj(2000000)
		if (pc.stat_level_get(stat_level_wizard)):	# WIZARD
			if (pc.stat_level_get( stat_gender ) == gender_female):	# FEMALE
				create_item_in_inventory( 6115, pc )		# armor
				create_item_in_inventory( 6045, pc )		# boots
				create_item_in_inventory( 6046, pc )		# gloves
										# helm
				create_item_in_inventory( 6638, pc )		# garb - blue
										# shield
				create_item_in_inventory( 4243, pc )		# weapon
				create_item_in_inventory( 12625, pc )		# ring
				create_item_in_inventory( 6242, pc )		# amulet health
				create_item_in_inventory( 12262, pc )		# wand of knock
				create_item_in_inventory( 12238, pc )		# wand of identify
				create_item_in_inventory( 12581, pc )		# wand of fireball
				create_item_in_inventory( 12581, pc )		# wand of fireball
				create_item_in_inventory( 12581, pc )		# wand of fireball
				pc.item_wield_best_all()
				pc.money_adj(2000000)
			elif (pc.stat_level_get( stat_gender ) == gender_male):	# MALE
				create_item_in_inventory( 6115, pc )		# armor
				create_item_in_inventory( 6045, pc )		# boots
				create_item_in_inventory( 6046, pc )		# gloves
				create_item_in_inventory( 6630, pc )		# wizard hat - blue
				create_item_in_inventory( 6627, pc )		# robes - blue
										# shield
				create_item_in_inventory( 4243, pc )		# weapon
				create_item_in_inventory( 12625, pc )		# ring
				create_item_in_inventory( 6242, pc )		# amulet health
				create_item_in_inventory( 12262, pc )		# wand of knock
				create_item_in_inventory( 12238, pc )		# wand of identify
				create_item_in_inventory( 12581, pc )		# wand of fireball
				create_item_in_inventory( 12581, pc )		# wand of fireball
				create_item_in_inventory( 12581, pc )		# wand of fireball
				pc.item_wield_best_all()
				pc.money_adj(2000000)
	game.fade_and_teleport(0,0,0,5001,622,418)
	game.areas[2] = 1
	game.areas[3] = 1
	game.areas[4] = 1
	game.areas[5] = 1
	game.areas[6] = 1
	game.areas[7] = 1
	game.areas[8] = 1
	game.areas[9] = 1
	game.areas[10] = 1
	game.areas[11] = 1
	game.areas[12] = 1
	game.areas[14] = 1
	game.areas[15] = 1
	game.areas[16] = 1
	return