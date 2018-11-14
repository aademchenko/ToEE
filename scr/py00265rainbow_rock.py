from toee import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	if (( game.quests[27].state == qs_mentioned ) or ( game.quests[27].state == qs_accepted )):
		game.quests[27].state = qs_completed
	game.global_vars[708] = 0
	#game.particles( "sp-summon monster I", game.leader)
	monsterA = game.obj_create( 14601, location_from_axis (487L, 505L) )
	monsterA.turn_towards(triggerer)
	monsterA.attack(triggerer)
	monsterA.concealed_set(1)
	monsterC = game.obj_create( 14602, location_from_axis (487L, 506L) )
	monsterC.turn_towards(triggerer)
	monsterC.concealed_set(1)
	monsterD = game.obj_create( 14602, location_from_axis (487L, 504L) )
	monsterD.turn_towards(triggerer)
	monsterD.concealed_set(1)
	monsterE = game.obj_create( 14602, location_from_axis (488L, 505L) )
	monsterE.turn_towards(triggerer)
	monsterE.concealed_set(1)
	game.new_sid = 0
	return RUN_DEFAULT

def create_rainbow_undead():
	if (( game.quests[27].state == qs_mentioned ) or ( game.quests[27].state == qs_accepted )):
		game.quests[27].state = qs_completed
	game.global_vars[708] = 0
	#game.particles( "sp-summon monster I", game.leader)
	monsterA = game.obj_create( 14601, location_from_axis (487L, 505L) )
	#monsterA.turn_towards(triggerer)
	monsterC = game.obj_create( 14602, location_from_axis (487L, 506L) )
	monsterD = game.obj_create( 14602, location_from_axis (487L, 504L) )
	monsterE = game.obj_create( 14602, location_from_axis (488L, 505L) )
	game.new_sid = 0
	return RUN_DEFAULT


def san_remove_item( attachee, triggerer ):
	if (( game.quests[27].state == qs_mentioned ) or ( game.quests[27].state == qs_accepted )):
		game.quests[27].state = qs_completed
	return RUN_DEFAULT
