from utilities import *
from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog(attachee,100)
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if (attachee.name == 8735):
		game.global_flags[506] = 1
		if (game.quests[96].state == qs_accepted or game.quests[96].state == qs_mentioned):
			game.quests[96].state = qs_completed
		game.global_vars[972] = game.global_vars[972] + 1
	else:
		game.global_vars[972] = game.global_vars[972] + 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[506] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee != OBJ_HANDLE_NULL and critter_is_unconscious(attachee) != 1 and not attachee.d20_query(Q_Prone)):
		if (not game.combat_is_active()):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_better_to_talk(attachee, obj)):
					game.timevent_add( start_talking, ( attachee, triggerer ), 2000 )
					game.new_sid = 0
	return RUN_DEFAULT


#def tools_transfer( attachee, triggerer ): Dont think works
#	itemA = attachee.item_find(12640)
#	if (itemA != OBJ_HANDLE_NULL):
#		itemA.destroy()
#		create_item_in_inventory( 12640, triggerer )
#	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 40):
			return 1
	return 0


def start_talking( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 100 )
	return RUN_DEFAULT


def switch_to_lieutenant( attachee, triggerer, line ):
	npc = find_npc_near(attachee,8893)
	if (npc != OBJ_HANDLE_NULL):
		npc.turn_towards(game.party[0])
		triggerer.begin_dialog(npc, line)
	return SKIP_DEFAULT


def trap( attachee, triggerer ):
	game.particles( 'Mon-EarthElem-Unconceal', triggerer )
	game.particles( 'Mon-EarthElem-body120', triggerer )
	game.particles( 'Orb-Summon-Earth Elemental', triggerer )
	game.particles( 'sp-Calm Animals', triggerer )
	game.particles( 'sp-Quench', triggerer )
	game.sound( 4042, 1 )
	for obj in game.party[0].group_list():
		damage_dice = dice_new( '4d8' )
		obj.float_mesfile_line( 'mes\\float.mes', 3 )
		game.particles( "hit-BLUDGEONING-medium", obj )
		if (obj.reflex_save_and_damage( OBJ_HANDLE_NULL, 20, D20_Save_Reduction_Half, D20STD_F_NONE, damage_dice, D20DT_BLUDGEONING, D20DAP_UNSPECIFIED, 0 , D20DAP_NORMAL )):
			triggerer.float_mesfile_line( 'mes\\spell.mes', 30001 )
		else:
			triggerer.float_mesfile_line( 'mes\\spell.mes', 30002 )
	return RUN_DEFAULT


def runoff( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT