from toee import *
from utilities import *
from Co8 import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (is_better_to_talk(attachee, game.party[0])):
			game.party[0].begin_dialog(attachee,1)
			game.new_sid = 0
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
#	for pc in game.party:
#		attachee.ai_shitlist_remove( pc )
#		attachee.reaction_set( pc, 50 )
	attachee.runoff(attachee.location-3)
	Timed_Destroy(npc, 5000)
	return RUN_DEFAULT


def destroy_map( attachee, triggerer ):
	itemA = attachee.item_find(11098)
	if (itemA != OBJ_HANDLE_NULL):
		itemA.destroy()
	return RUN_DEFAULT

	
def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 40):
		return 1
	return 0