from toee import *
from combat_standard_routines import *
from utilities import *
from py00439script_daemon import record_time_stamp, get_v, set_v, get_f, set_f, npc_set, npc_unset, npc_get, tsc, tpsts, within_rect_by_corners


def san_dialog( attachee, triggerer ):
	if (not attachee.has_met( triggerer )):
		record_time_stamp(516)
		triggerer.begin_dialog( attachee, 1 )
	else:
		triggerer.begin_dialog( attachee, 280 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[372] == 1):
		attachee.object_flag_set(OF_OFF)
	else:
		if (attachee.leader_get() == OBJ_HANDLE_NULL) and not game.combat_is_active():
			game.global_vars[715] = 0
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[106] = 1
	record_time_stamp(458)
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	game.global_flags[346] = 0
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[106] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	xx, yy = location_to_axis(attachee.location)
	if (not game.combat_is_active()):
		if xx == 545 and yy == 497: # Kelno is in his usual place
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (not attachee.has_met(obj)):
					if (is_safe_to_talk(attachee,obj)):
						record_time_stamp(516)
						if ( (game.global_flags[104] == 1) or (game.global_flags[105] == 1) or (game.global_flags[107] == 1) ):
							obj.turn_towards(attachee)	## added by Livonya
							attachee.turn_towards(obj)	## added by Livonya
							obj.begin_dialog( attachee, 460 )
						else:
							obj.turn_towards(attachee)	## added by Livonya
							attachee.turn_towards(obj)	## added by Livonya
							obj.begin_dialog(attachee,1)
							##game.new_sid = 0			## removed by Livonya
		else: #Kelno is in the Air Altar room - Air is on alert
			for obj in game.party:
				#attachee.turn_towards(obj)
				if (not attachee.has_met(obj) and is_safe_to_talk2(attachee,obj, 25) == 1 and obj.type == obj_t_pc):
					record_time_stamp(516)
					if (get_v(453) & 4 == 0 and get_v(453) & 8 == 0 and get_v(453) & 16 == 0): # Air Escort Variables
					## How the hell did you get here? GTFO! (not escorted by anyone, probably dropped in from ceiling or snuck in)
					# For now, ordinary dialogue
						if ( (game.global_flags[104] == 1) or (game.global_flags[105] == 1) or (game.global_flags[107] == 1) ):
							obj.turn_towards(attachee)	## added by Livonya
							attachee.turn_towards(obj)	## added by Livonya
							obj.begin_dialog( attachee, 460 )
						else:
							obj.turn_towards(attachee)	## added by Livonya
							attachee.turn_towards(obj)	## added by Livonya
							obj.begin_dialog(attachee,1)
					else:
						if ( (game.global_flags[104] == 1) or (game.global_flags[105] == 1) or (game.global_flags[107] == 1) ):
							obj.turn_towards(attachee)	## added by Livonya
							attachee.turn_towards(obj)	## added by Livonya
							obj.begin_dialog( attachee, 460 )
						else:
							obj.turn_towards(attachee)	## added by Livonya
							attachee.turn_towards(obj)	## added by Livonya
							obj.begin_dialog(attachee,1)
	if (game.global_vars[715] == 0 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
		attachee.cast_spell(spell_protection_from_elements, attachee)
		attachee.spells_pending_to_memorized()
	if (game.global_vars[715] == 4 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
		attachee.cast_spell(spell_shield_of_faith, attachee)
		attachee.spells_pending_to_memorized()
	game.global_vars[715] = game.global_vars[715] + 1
	return RUN_DEFAULT


def escort_below( attachee, triggerer ):
	# game.global_flags[144] = 1
	game.global_vars[691] = 2
	game.fade_and_teleport(0,0,0,5080,478,451)
	return RUN_DEFAULT


def is_safe_to_talk2(speaker,listener, radius):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= radius):
			return 1
	return 0


def unlock_sw_doors():
	for obj in game.obj_list_vicinity(location_from_axis(508, 501), OLC_PORTAL):
		x1, y1 = location_to_axis(obj.location)
		if (x1 == 508 and y1 == 501) or (x1 == 508 and y1 == 497):
			if ( obj.portal_flags_get() & OPF_LOCKED ):
				obj.float_mesfile_line( 'mes\\spell.mes', 30004 )
				obj.portal_flag_unset( OPF_LOCKED )

			#if not ( obj.portal_flags_get() & OPF_OPEN ):
			#	obj.portal_toggle_open() - doesn't work


def should_open_sw_doors():
	for obj in game.obj_list_vicinity(location_from_axis(508, 501), OLC_PORTAL):
		x1, y1 = location_to_axis(obj.location)
		if (x1 == 508 and y1 == 501) or (x1 == 508 and y1 == 497):
			if ( obj.portal_flags_get() & OPF_LOCKED ):
				return 1
	return 0