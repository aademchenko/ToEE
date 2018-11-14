from toee import *
from utilities import *
from combat_standard_routines import *


## these scripts are used to get Hommlet interior doors that normally lead to Hommlet exterior to instead lead to the custom Hommlet substitute map where WotGS is staged while WotGS is active.


def san_use( door, triggerer ):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6):
		if (door.name == 1701):
		# prosperous farmer
			game.fade_and_teleport( 0,0,0,5189,717,486 )
			return SKIP_DEFAULT
		elif (door.name == 1702):
		# modest farmhouse
			game.fade_and_teleport( 0,0,0,5189,763,433 )
			return SKIP_DEFAULT
		elif (door.name == 1703):
		# woodcutter
			game.fade_and_teleport( 0,0,0,5189,733,381 )
			return SKIP_DEFAULT
		elif (door.name == 1704):
		# well kept farm
			game.fade_and_teleport( 0,0,0,5189,676,507 )
			return SKIP_DEFAULT
		elif (door.name == 1705):
		# prosperous farmhouse
			game.fade_and_teleport( 0,0,0,5189,658,448 )
			return SKIP_DEFAULT
		elif (door.name == 1706):
		# leatherworker
			game.fade_and_teleport( 0,0,0,5189,634,450 )
			return SKIP_DEFAULT
		elif (door.name == 1707):
		# moneychanger 2
			game.fade_and_teleport( 0,0,0,5189,548,332 )
			return SKIP_DEFAULT
		elif (door.name == 1708):
		# blacksmith
			game.fade_and_teleport( 0,0,0,5189,562,444 )
			return SKIP_DEFAULT
		elif (door.name == 1709):
		# new building
			game.fade_and_teleport( 0,0,0,5189,575,409 )
			return SKIP_DEFAULT
		elif (door.name == 1710):
		# weaver
			game.fade_and_teleport( 0,0,0,5189,548,409 )
			return SKIP_DEFAULT
		elif (door.name == 1711):
		# tailor
			game.fade_and_teleport( 0,0,0,5189,539,380 )
			return SKIP_DEFAULT
		elif (door.name == 1712):
		# strapping farmer
			game.fade_and_teleport( 0,0,0,5189,524,393 )
			return SKIP_DEFAULT
		elif (door.name == 1713):
		# cabinet maker 2
			game.fade_and_teleport( 0,0,0,5189,569,284 )
			return SKIP_DEFAULT
		elif (door.name == 1714):
		# teamster
			game.fade_and_teleport( 0,0,0,5189,448,321 )
			return SKIP_DEFAULT
		elif (door.name == 1715):
		# moneychanger 1
			game.fade_and_teleport( 0,0,0,5189,559,325 )
			return SKIP_DEFAULT
		elif (door.name == 1716):
		# cabinet maker 1
			game.fade_and_teleport( 0,0,0,5189,572,275 )
			return SKIP_DEFAULT
		elif (door.name == 1717):
		# potter
			game.fade_and_teleport( 0,0,0,5189,588,298 )
			return SKIP_DEFAULT
		elif (door.name == 1718):
		# brewhouse 1
			game.fade_and_teleport( 0,0,0,5189,647,324 )
			return SKIP_DEFAULT
		elif (door.name == 1719):
		# modest cottage
			game.fade_and_teleport( 0,0,0,5189,548,242 )
			return SKIP_DEFAULT
		elif (door.name == 1720):
		# cabinet maker 3
			game.fade_and_teleport( 0,0,0,5189,562,293 )
			return SKIP_DEFAULT
		elif (door.name == 1721):
		# cheesemaker
			game.fade_and_teleport( 0,0,0,5189,445,368 )
			return SKIP_DEFAULT
		elif (door.name == 1722):
		# mill
			game.fade_and_teleport( 0,0,0,5189,448,410 )
			return SKIP_DEFAULT
		elif (door.name == 1723):
		# reclusive farmer
			game.fade_and_teleport( 0,0,0,5189,397,413 )
			return SKIP_DEFAULT
		elif (door.name == 1724):
		# the grove
			game.fade_and_teleport( 0,0,0,5189,621,520 )
			return SKIP_DEFAULT
		elif (door.name == 1725):
		# herdsman barn 1
			game.fade_and_teleport( 0,0,0,5189,592,473 )
			return SKIP_DEFAULT
		elif (door.name == 1726):
		# wainwright
			game.fade_and_teleport( 0,0,0,5189,558,484 )
			return SKIP_DEFAULT
		elif (door.name == 1727):
		# village elder
			game.fade_and_teleport( 0,0,0,5189,496,463 )
			return SKIP_DEFAULT
		elif (door.name == 1728):
		# carpenter
			game.fade_and_teleport( 0,0,0,5189,523,508 )
			return SKIP_DEFAULT
		elif (door.name == 1729):
		# stone mason
			game.fade_and_teleport( 0,0,0,5189,452,517 )
			return SKIP_DEFAULT
		elif (door.name == 1730):
		# brewhouse 2
			game.fade_and_teleport( 0,0,0,5189,642,327 )
			return SKIP_DEFAULT
		elif (door.name == 1731):
		# inn first
			game.fade_and_teleport( 0,0,0,5189,627,401 )
			return SKIP_DEFAULT
		elif (door.name == 1732):
		# traders barn 1
			game.fade_and_teleport( 0,0,0,5189,492,295 )
			return SKIP_DEFAULT
		elif (door.name == 1733):
		# traders barn 2
			game.fade_and_teleport( 0,0,0,5189,488,309 )
			return SKIP_DEFAULT
		elif (door.name == 1734):
		# traders barn 3
			game.fade_and_teleport( 0,0,0,5189,460,314 )
			return SKIP_DEFAULT
		elif (door.name == 1735):
		# traders store 1
			game.fade_and_teleport( 0,0,0,5189,519,302 )
			return SKIP_DEFAULT
		elif (door.name == 1736):
		# traders store 2
			game.fade_and_teleport( 0,0,0,5189,493,309 )
			return SKIP_DEFAULT
		elif (door.name == 1737):
		# traders store 3
			game.fade_and_teleport( 0,0,0,5189,516,329 )
			return SKIP_DEFAULT
		elif (door.name == 1738):
		# main floor
			game.fade_and_teleport( 0,0,0,5189,495,231 )
			return SKIP_DEFAULT
		elif (door.name == 1739):
		# main hall
			game.fade_and_teleport( 0,0,0,5189,449,607 )
			return SKIP_DEFAULT
		elif (door.name == 1740):
		# herdsman barn 2
			game.fade_and_teleport( 0,0,0,5189,577,492 )
			return SKIP_DEFAULT
	else:
		return RUN_DEFAULT