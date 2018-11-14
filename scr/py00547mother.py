from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if ( attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 200 )
	else:
		triggerer.begin_dialog( attachee, 100 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.quests[95].state == qs_mentioned and game.global_vars[764] >= 8):
		attachee.object_flag_unset( OF_OFF )
		game.new_sid = 0
	return RUN_DEFAULT


def behave(attachee, triggerer):
	attachee.npc_flag_unset(ONF_WAYPOINTS_DAY)
	attachee.npc_flag_unset(ONF_WAYPOINTS_NIGHT)
	for obj in game.obj_list_vicinity(attachee.location,OLC_NPC):
		if obj.name == 14686:
			obj.npc_flag_unset(ONF_WAYPOINTS_DAY)
			obj.npc_flag_unset(ONF_WAYPOINTS_NIGHT)
	return


def bling( attachee, triggerer ):
	game.sound( 4048, 1 )
	pc1 = game.party[0]
	game.particles( "sp-Neutralize Poison", pc1 )
	pc2 = game.party[1]
	game.particles( "sp-Neutralize Poison", pc2 )
	pc3 = game.party[2]
	game.particles( "sp-Neutralize Poison", pc3 )
	pc4 = game.party[3]
	game.particles( "sp-Neutralize Poison", pc4 )
	pc5 = game.party[4]
	game.particles( "sp-Neutralize Poison", pc5 )
	pc6 = game.party[5]
	game.particles( "sp-Neutralize Poison", pc6 )
	pc7 = game.party[6]
	game.particles( "sp-Neutralize Poison", pc7 )
	pc8 = game.party[7]
	game.particles( "sp-Neutralize Poison", pc8 )
	return 1