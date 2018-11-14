from toee import *
import _include
from utilities import *
from scripts import *
from co8Util.PersistentData import *
from co8Util.ObjHandling import *
from combat_standard_routines import *
HB_BLOCKAGE_KEY = "HB_BLOCKAGE_SERIAL"


def san_use( door, triggerer ):
	if (door.name == 1620):
		if (game.global_flags[531] == 1):
		## if cave blockage is active, disable door portal
			return SKIP_DEFAULT
		else:
			return RUN_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if ((game.global_vars[980] == 2) or (game.global_vars[981] == 2) or (game.global_vars[982] == 2) or (game.global_vars[983] == 2) or (game.global_vars[984] == 2) and game.global_flags[531] == 0):
	## turns on cave blockage
		attachee.object_flag_unset(OF_OFF)
		game.global_flags[531] = 1
		game.global_flags[572] = 1
		game.new_sid = 0
	hb_blockage_serial = derefHandle(attachee)
	Co8PersistentData.setData(HB_BLOCKAGE_KEY, hb_blockage_serial)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.particles( 'ef-MinoCloud', attachee )
	game.particles( 'Orb-Summon-Earth Elemental', attachee )
	game.particles( 'Mon-EarthElem-Unconceal', attachee )
	game.sound( 4042, 1 )
	attachee.object_flag_set(OF_OFF)
	game.global_flags[531] = 0
	return SKIP_DEFAULT


def san_enter_combat( attachee, triggerer ):
	return SKIP_DEFAULT


def san_start_combat( attachee, triggerer ):
	for target in game.party[0].group_list():
		return SKIP_DEFAULT
	return RUN_DEFAULT