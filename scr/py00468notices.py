from toee import *
from utilities import *
import _include
from co8Util.TimedEvent import *
from combat_standard_routines import *
from py00439script_daemon import get_f, set_f, get_v, set_v, tpsts, record_time_stamp


def san_use( attachee, triggerer ):
	if (attachee.name == 11063):
		game.quests[110].state = qs_mentioned
		game.new_sid = 0
	elif (attachee.name == 11064):
		game.quests[90].state = qs_mentioned
		game.new_sid = 0
	elif (attachee.name == 11065):
		game.quests[111].state = qs_mentioned
		game.new_sid = 0
	elif (attachee.name == 11066):
		game.quests[112].state = qs_mentioned
		game.new_sid = 0
	elif (attachee.name == 11067):
		game.quests[108].state = qs_mentioned
		game.global_vars[939] = 1
		game.new_sid = 0
	elif (attachee.name == 11068):
		if (game.quests[97].state != qs_botched):
			game.quests[97].state = qs_botched
		if (game.party[0].reputation_has(53) == 0):
			game.party[0].reputation_add( 53 )
		game.global_vars[510] = 2
		game.global_flags[504] = 1
		game.new_sid = 0
	elif (attachee.name == 11069):
		triggerer.money_adj(-10000)
		attachee.destroy()
	elif (attachee.name == 11070):
		game.quests[106].state = qs_mentioned
		game.new_sid = 0
	elif (attachee.name == 11071):
		game.quests[95].state = qs_completed
		game.new_sid = 0
	elif (attachee.name == 11072):
		game.quests[105].state = qs_mentioned
		set_bethany()
		game.new_sid = 0
	elif (attachee.name == 11073):
		game.quests[105].state = qs_mentioned
		set_bethany()
		game.new_sid = 0
	return RUN_DEFAULT


def set_bethany():
	game.encounter_queue.append(3447)
	set_f('s_bethany_scheduled')
	return RUN_DEFAULT