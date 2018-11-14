from toee import *
from utilities import *
from Co8 import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.name == 14581):					## red portal
		if (game.global_vars[931] != 0):
			triggerer.begin_dialog( attachee, 710 )
		else:
			triggerer.begin_dialog( attachee, 110 )
	elif (attachee.name == 14582):					## orange portal
		if (game.global_vars[932] != 0):
			triggerer.begin_dialog( attachee, 810 )
		else:
			triggerer.begin_dialog( attachee, 210 )
	elif (attachee.name == 14583):					## yellow portal
		if (game.global_vars[933] != 0):
			triggerer.begin_dialog( attachee, 910 )
		else:
			triggerer.begin_dialog( attachee, 310 )
	elif (attachee.name == 14584):					## green portal
		if (game.global_vars[934] != 0):
			triggerer.begin_dialog( attachee, 1010 )
		else:
			triggerer.begin_dialog( attachee, 410 )
	elif (attachee.name == 14585):					## blue portal
		if (game.global_vars[935] != 0):
			triggerer.begin_dialog( attachee, 1110 )
		else:
			triggerer.begin_dialog( attachee, 510 )
	elif (attachee.name == 14586):					## violet portal
		if (game.global_vars[936] != 0):
			triggerer.begin_dialog( attachee, 1210 )
		else:
			triggerer.begin_dialog( attachee, 610 )
	return SKIP_DEFAULT


def san_start_combat( attachee, triggerer ):
	leader = game.party[0]
	StopCombat(attachee, 0)
	leader.begin_dialog( attachee, 1 )
	return RUN_DEFAULT


def play_sparkles( attachee ):
	for pc in game.party:
		game.particles( "hit-BANE-medium", pc )
	return RUN_DEFAULT


def teleport_hommlet( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_hommlet, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_hommlet( attachee ):
	game.fade_and_teleport(0,0,0,5001,623,418)
	return RUN_DEFAULT


def teleport_nulb( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_nulb, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_nulb( attachee ):
	game.fade_and_teleport(0,0,0,5051,507,361)
	return RUN_DEFAULT


def teleport_verbobonc( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_verbobonc, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_verbobonc( attachee ):
	game.global_flags[260] = 1
	game.fade_and_teleport(0,0,0,5121,252,506)
	return RUN_DEFAULT


def teleport_tower( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_tower, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_tower( attachee ):
	game.fade_and_teleport(0,0,0,5016,478,486)
	return RUN_DEFAULT


def teleport_cuthbert( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_cuthbert, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_cuthbert( attachee ):
	game.fade_and_teleport(0,0,0,5012,484,485)
	return RUN_DEFAULT


def teleport_grove( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_grove, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_grove( attachee ):
	game.fade_and_teleport(0,0,0,5042,492,477)
	return RUN_DEFAULT


def teleport_wench( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_wench, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_wench( attachee ):
	game.fade_and_teleport(0,0,0,5007,484,486)
	return RUN_DEFAULT


def teleport_smyth( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_smyth, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_smyth( attachee ):
	game.fade_and_teleport(0,0,0,5001,574,440)
	return RUN_DEFAULT


def teleport_trader( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_trader, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_trader( attachee ):
	game.fade_and_teleport(0,0,0,5010,481,480)
	return RUN_DEFAULT


def teleport_residence( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_residence, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_residence( attachee ):
	game.fade_and_teleport(0,0,0,5085,473,495)
	return RUN_DEFAULT


def teleport_hostel( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_hostel, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_hostel( attachee ):
	game.fade_and_teleport(0,0,0,5060,483,500)
	return RUN_DEFAULT


def teleport_otis( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_otis, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_otis( attachee ):
	game.fade_and_teleport(0,0,0,5056,492,487)
	return RUN_DEFAULT


def teleport_fong( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_fong, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_fong( attachee ):
	game.fade_and_teleport(0,0,0,5088,473,492)
	return RUN_DEFAULT


def teleport_cityhall( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_cityhall, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_cityhall( attachee ):
	game.fade_and_teleport(0,0,0,5169,490,490)
	return RUN_DEFAULT


def teleport_constabulary( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_constabulary, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_constabulary( attachee ):
	game.fade_and_teleport(0,0,0,5171,489,495)
	return RUN_DEFAULT


def teleport_pelor( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_pelor, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_pelor( attachee ):
	game.fade_and_teleport(0,0,0,5137,484,485)
	return RUN_DEFAULT


def teleport_goose( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_goose, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_goose( attachee ):
	game.fade_and_teleport(0,0,0,5151,497,490)
	return RUN_DEFAULT


def teleport_archers( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_archers, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_archers( attachee ):
	game.fade_and_teleport(0,0,0,5161,475,472)
	return RUN_DEFAULT


def teleport_bazaar( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_bazaar, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_bazaar( attachee ):
	game.fade_and_teleport(0,0,0,5180,516,502)
	return RUN_DEFAULT


def teleport_emridy( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_emridy, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_emridy( attachee ):
	game.fade_and_teleport(0,0,0,5094,488,488)
	return RUN_DEFAULT


def teleport_hickory( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_hickory, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_hickory( attachee ):
	game.fade_and_teleport(0,0,0,5095,462,462)
	return RUN_DEFAULT


def teleport_welkwood( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_welkwood, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_welkwood( attachee ):
	game.fade_and_teleport(0,0,0,5093,517,324)
	return RUN_DEFAULT


def teleport_moathouse( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_moathouse, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_moathouse( attachee ):
	game.fade_and_teleport(0,0,0,5004,476,478)
	return RUN_DEFAULT


def teleport_moatdung( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_moatdung, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_moatdung( attachee ):
	game.fade_and_teleport(0,0,0,5005,424,414)
	return RUN_DEFAULT


def teleport_toee( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_toee, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_toee( attachee ):
	game.fade_and_teleport(0,0,0,5064,490,499)
	return RUN_DEFAULT


def teleport_toee1( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_toee1, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_toee1( attachee ):
	game.fade_and_teleport(0,0,0,5066,484,517)
	return RUN_DEFAULT


def teleport_toee2( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_toee2, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_toee2( attachee ):
	game.fade_and_teleport(0,0,0,5067,487,455)
	return RUN_DEFAULT


def teleport_toee3( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_toee3, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_toee3( attachee ):
	game.fade_and_teleport(0,0,0,5105,491,519)
	return RUN_DEFAULT


def teleport_toee4( attachee, triggerer ):
	game.sound( 4121, 1 )
	game.particles( "sp-Teleport", attachee )
	game.timevent_add( telly_toee4, ( attachee, ), 2500 )
	game.timevent_add( play_sparkles, ( attachee, ), 2000 )
	return RUN_DEFAULT


def telly_toee4( attachee ):
	game.fade_and_teleport(0,0,0,5080,479,590)
	return RUN_DEFAULT