from toee import *
import _include
from co8Util.TimedEvent import *
from combat_standard_routines import *
from py00439script_daemon import get_f, set_f, get_v, set_v, tpsts, record_time_stamp


def san_dialog( attachee, triggerer ):
	if ( game.quests[60].state == qs_completed and game.global_flags[315] == 1 ):
		triggerer.begin_dialog(attachee,400)
	elif ( not attachee.has_met(triggerer) ):
		if game.quests[35].state == qs_completed:
			triggerer.begin_dialog(attachee,300)
		else:
			triggerer.begin_dialog(attachee,1)
	elif ( game.quests[60].state == qs_botched ):
		triggerer.begin_dialog(attachee,260)
	elif ( game.global_flags[317] == 1 ):
		triggerer.begin_dialog(attachee,330)
	elif ( game.quests[60].state <= qs_mentioned ):
		triggerer.begin_dialog(attachee,470)
	else:
		triggerer.begin_dialog(attachee,200)
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.quests[60].state = qs_botched
	return RUN_DEFAULT


def san_heartbeat(attachee, triggerer):
	if ( game.quests[60].state == qs_completed and game.global_flags[315] == 1 ):
		if (attachee.map == 5051):
			attachee.object_flag_set(OF_OFF)
		if (attachee.map == 5089):
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def buttin( attachee, triggerer, line):
	npc = find_npc_near(attachee,8015)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,150)
	return SKIP_DEFAULT


def schedule_gremlich( attachee, triggerer ):
	game.timevent_add( set_gremlich, (), 86400000 ) #86400000ms is 1 day
	record_time_stamp('s_gremlich_1')
	return RUN_DEFAULT


def set_gremlich():
	game.encounter_queue.append(3436)
	set_f('s_gremlich_1_scheduled')
	return RUN_DEFAULT


def encounter_picker( attachee, triggerer ):
	enc = game.random_range(1,6)
	if (enc == 1):
		game.timevent_add( set_sport_encounter_1, (), 259200000 ) #259200000ms is 3 days
		record_time_stamp('s_sport_1')
	elif (enc == 2):
		game.timevent_add( set_sport_encounter_2, (), 259200000 ) #259200000ms is 3 days
		record_time_stamp('s_sport_2')
	elif (enc == 3):
		game.timevent_add( set_sport_encounter_3, (), 259200000 ) #259200000ms is 3 days
		record_time_stamp('s_sport_3')
	elif (enc == 4):
		game.timevent_add( set_sport_encounter_4, (), 259200000 ) #259200000ms is 3 days
		record_time_stamp('s_sport_4')
	elif (enc == 5):
		game.timevent_add( set_sport_encounter_5, (), 259200000 ) #259200000ms is 3 days
		record_time_stamp('s_sport_5')
	elif (enc == 6):
		game.timevent_add( set_sport_encounter_6, (), 259200000 ) #259200000ms is 3 days
		record_time_stamp('s_sport_6')
	return RUN_DEFAULT


def set_sport_encounter_1():
	game.encounter_queue.append(3441)
	set_f('s_sport_1_scheduled')
	game.global_vars[564] = 1
	return RUN_DEFAULT


def set_sport_encounter_2():
	game.encounter_queue.append(3442)
	set_f('s_sport_2_scheduled')
	game.global_vars[564] = 1
	return RUN_DEFAULT


def set_sport_encounter_3():
	game.encounter_queue.append(3443)
	set_f('s_sport_3_scheduled')
	game.global_vars[564] = 1
	return RUN_DEFAULT


def set_sport_encounter_4():
	game.encounter_queue.append(3444)
	set_f('s_sport_4_scheduled')
	game.global_vars[564] = 1
	return RUN_DEFAULT


def set_sport_encounter_5():
	game.encounter_queue.append(3445)
	set_f('s_sport_5_scheduled')
	game.global_vars[564] = 1
	return RUN_DEFAULT


def set_sport_encounter_6():
	game.encounter_queue.append(3446)
	set_f('s_sport_6_scheduled')
	game.global_vars[564] = 1
	return RUN_DEFAULT


def gremlich_movie_setup( attachee, triggerer ):
	set_gremlich_slides()
	return


def set_gremlich_slides():
	game.moviequeue_add(600)
	game.moviequeue_add(627)
	game.moviequeue_play()
	return RUN_DEFAULT