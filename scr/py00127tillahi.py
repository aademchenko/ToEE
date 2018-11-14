from utilities import *
from toee import *
import _include
from co8Util.TimedEvent import *
from combat_standard_routines import *
from py00439script_daemon import get_f, set_f, get_v, set_v, tpsts, record_time_stamp


def san_dialog( attachee, triggerer ):
	if (game.global_flags[127] == 0):
		triggerer.begin_dialog( attachee, 1 )
	else:
		triggerer.begin_dialog( attachee, 140 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT


def set_reward( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	game.timevent_add( give_reward, (), 864000000 ) #864000000ms is 10 days
	record_time_stamp('s_tillahi_reward') #  bulletproofed with Global Scheduling System - see py00439script_daemon.py
	return RUN_DEFAULT


def give_reward():
	game.encounter_queue.append(3002)
	set_f('s_tillahi_reward_scheduled')
	return RUN_DEFAULT


def get_rep( attachee, triggerer ):
	if triggerer.reputation_has( 16 ) == 0:
		triggerer.reputation_add( 16 )
	game.global_vars[26] = game.global_vars[26] + 1
	if ( game.global_vars[26] >= 3 and triggerer.reputation_has( 17 ) == 0):
		triggerer.reputation_add( 17 )
	return RUN_DEFAULT