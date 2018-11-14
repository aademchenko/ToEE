from toee import *

def san_trap( trap, triggerer ):
	game.particles( trap.partsys, trap.obj )
	for dmg in trap.damage:
		triggerer.damage( trap.obj, dmg.type, dmg.damage )
	return SKIP_DEFAULT
