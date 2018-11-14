from toee import *
from utilities import *
from py00439script_daemon import record_time_stamp, get_v, set_v, npc_set, npc_unset, npc_get, tsc, within_rect_by_corners
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if attachee.name == 14181: # Water Temple Sentry
		if get_v('water_sentry_pester') < 7:
			lll = game.random_range(0, 3)
			attachee.float_line(lll + 1100, triggerer)
			set_v('water_sentry_pester', get_v('water_sentry_pester') + 1 )
		elif get_v('water_sentry_pester') == 7:
			lll = game.random_range(0, 1)
			attachee.float_line(1104 + lll, triggerer)
			set_v('water_sentry_pester', get_v('water_sentry_pester') + 1 )
		elif get_v('water_sentry_pester') == 8:
			attachee.float_line(1150, triggerer)
			set_v('water_sentry_pester', get_v('water_sentry_pester') + 1 )
		elif get_v('water_sentry_pester') > 8:
			attachee.critter_flag_set( OCF_MUTE )
	elif (not attachee.has_met(triggerer)):
		record_time_stamp(501)
		if (game.global_flags[91] == 1):
			triggerer.begin_dialog( attachee, 100 )
		else:
			triggerer.begin_dialog( attachee, 1 )
	else:
		triggerer.begin_dialog( attachee, 300 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	dummy = 1
	return RUN_DEFAULT

def san_heartbeat( attachee, triggerer ):
	if attachee.name == 14181: #Water Temple Bugbear
		if (not game.combat_is_active() and get_v(453) & 2 == 0):
			for pc in game.party:
				if pc.type == obj_t_pc and is_safe_to_talk2(attachee, pc, 20):
					# attachee.turn_towards(pc)
					# pc.begin_dialog(attachee, 1)
					# game.particles('ef-minocloud', attachee)
					attachee.critter_flag_unset( OCF_MUTE )
					attachee.scripts[9] = 445
					set_v(453, get_v(453) | 2 ) # escorting to Water flag
					if (  int( tsc(456, 475) ) + int( tsc(458, 475) ) + int( tsc(459, 475) )   ) >= 2:
						attachee.float_line(1000, pc)
					elif tsc(456, 475) == 1:
						attachee.float_line(1001, pc)
					elif tsc(458, 475) == 1:
						attachee.float_line(1002, pc)
					elif tsc(459, 475) == 1:
						attachee.float_line(1003, pc)
	return RUN_DEFAULT

def san_enter_combat( attachee, triggerer ):
	for obj in game.obj_list_vicinity(attachee.location,OLC_NPC):
		if obj.leader_get() == OBJ_HANDLE_NULL:
			obj.npc_flag_set(ONF_KOS)
			obj.npc_flag_unset(ONF_KOS_OVERRIDE)
	attachee.scripts[19] = 0
	if attachee.name == 14181:
	# Water Temple sentry
		game.global_flags[345] = 0
		for statue in game.obj_list_vicinity( attachee.location, OLC_SCENERY ):
			if (statue.name == 1618):
				sx, sy = location_to_axis(statue.location)
				if sy > 566:
					loc = statue.location
					rot = statue.rotation
					statue.destroy()
					for obj in game.obj_list_vicinity( attachee.location, OLC_NPC ):
						if obj.name == 14244:
							return RUN_DEFAULT					
					juggernaut = game.obj_create( 14244, loc )
					juggernaut.rotation = rot
					game.particles( "ef-MinoCloud", juggernaut )
	return RUN_DEFAULT


def is_safe_to_talk2(speaker,listener, radius):
	if (speaker.can_see(listener) and listener.type == obj_t_pc):
		if (speaker.distance_to(listener) <= radius):
			return 1
	return 0