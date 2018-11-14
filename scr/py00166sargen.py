from toee import *
from utilities import *
import _include
from co8Util.TimedEvent import *
from combat_standard_routines import *
from py00439script_daemon import get_f, set_f, get_v, set_v, tpsts, record_time_stamp


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 100 )
	elif (not attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 1 )
	else:
		triggerer.begin_dialog( attachee, 90 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
		game.global_vars[731] = 0
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[731] == 0 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
		attachee.cast_spell(spell_mage_armor, attachee)
		attachee.spells_pending_to_memorized()
		game.global_vars[731] = 1
	if (not game.combat_is_active()):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_safe_to_talk(attachee,obj)):
				game.new_sid = 0
				obj.begin_dialog(attachee,1)
				return RUN_DEFAULT
	return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	if ((attachee.area == 1) or (attachee.area == 3) or (attachee.area == 14)):
		obj = attachee.leader_get()
		if (obj != OBJ_HANDLE_NULL):
			obj.begin_dialog(attachee, 140)
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT


def schedule_reward( attachee, triggerer ):
	game.timevent_add( give_reward, (), 1814400000 ) #1814400000ms is 3 weeks
	record_time_stamp('s_sargen_reward') #  bulletproofed with Global Scheduling System - see py00439script_daemon.py
	return RUN_DEFAULT


def give_reward():
	game.encounter_queue.append(3003)
	set_f('s_sargen_reward_scheduled')
	return RUN_DEFAULT