from utilities import *
from toee import *
from combat_standard_routines import *
from py00439script_daemon import *


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5121):
		if (game.global_vars[944] == 1):
			game.timevent_add( one_hour_delay_to_pick_up_darlia_for_robbery, (), 3600000 )		## 1 hour
			game.global_vars[944] = 4
		if (game.global_vars[944] == 2):
			game.timevent_add( one_hour_delay_to_pick_up_darlia_for_framework, (), 3600000 )	## 1 hour
			game.global_vars[944] = 4
		if (game.global_vars[944] == 3):
			if tpsts('achan_off_to_arrest', 1*60*60) == 1:
				game.global_vars[946] = 3
			if tpsts('absalom_off_to_arrest', 1*60*60) == 1:
				game.global_vars[947] = 3
			if tpsts('abiram_off_to_arrest', 1*60*60) == 1:
				game.global_vars[948] = 3
			# setting the vars may be considered redundant with use of the time stamps, but it never hurts to bulletproof things in ToEE ;-) -SA
			game.timevent_add( one_hour_delay_to_pick_up_darlia_for_wilfrick, (), 3600000 )		## 1 hour
			game.global_vars[944] = 4
	return RUN_DEFAULT


def one_hour_delay_to_pick_up_darlia_for_robbery():
	game.global_vars[945] = 1
	return RUN_DEFAULT


def one_hour_delay_to_pick_up_darlia_for_framework():
	game.global_vars[945] = 2
	return RUN_DEFAULT


def one_hour_delay_to_pick_up_darlia_for_wilfrick():
	game.global_vars[945] = 3
	if (game.global_vars[946] == 2): # Achan
		game.global_vars[946] = 3
	if (game.global_vars[947] == 2): # Absalom
		game.global_vars[947] = 3
	if (game.global_vars[948] == 2): # Abiram
		game.global_vars[948] = 3
	return RUN_DEFAULT