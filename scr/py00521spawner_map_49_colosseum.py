from utilities import *
from toee import *
from combat_standard_routines import *


def san_heartbeat(attachee, triggerer):
	mota = game.obj_create(14578, location_from_axis(504, 462))
	mota.rotation = 2.5
	attachee.destroy()
	return RUN_DEFAULT
