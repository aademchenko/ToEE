from toee import *

def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[509] == 0):
		game.obj_create( 1054, location_from_axis (559L, 438L) )
		game.global_vars[509] = game.global_vars[500] + 1
	return RUN_DEFAULT

def san_trap( trap, triggerer ):
	# numP = 210 / (game.party_npc_size() + game.party_pc_size())
	# for obj in game.obj_list_vicinity( triggerer.location, OLC_CRITTERS ):
		# obj.stat_base_set(stat_experience, (obj.stat_level_get(stat_experience) - numP))
	if (triggerer.map == 5094):
#		monsterA = game.obj_create( 14424, location_from_axis (487L, 505L) )	## test
#		monsterA = game.obj_create( 14600, location_from_axis (487L, 505L) )	## test
		game.global_vars[708] = 0
		monsterA = game.obj_create( 14601, location_from_axis (487L, 505L) )	## test
#		create_item_in_inventory ( 6072, monsterA )
		create_item_in_inventory ( 4068, monsterA )
#		create_item_in_inventory ( 4004, monsterA )
		monsterA.concealed_set(1)
		monsterC = game.obj_create( 14602, location_from_axis (487L, 506L) )
		create_item_in_inventory ( 4194, monsterC )
		monsterC.concealed_set(1)
		monsterD = game.obj_create( 14602, location_from_axis (487L, 504L) )
		create_item_in_inventory ( 4194, monsterD )
		monsterD.concealed_set(1)
		monsterE = game.obj_create( 14602, location_from_axis (488L, 505L) )
		create_item_in_inventory ( 4194, monsterE )
		monsterE.concealed_set(1)


#		monsterA = game.obj_create( 14081, location_from_axis (487L, 505L) )	## test
#		monsterA.turn_towards(triggerer) 							## test
#		monsterA.attack(triggerer) 								## test
#		monsterA.concealed_set(1) 								## test
#		monsterB = game.obj_create( 14128, location_from_axis (487L, 499L) )
#		monsterB = game.obj_create( 14425, location_from_axis (487L, 499L) )  	## test
		monsterB.turn_towards(triggerer)
		monsterB.attack(triggerer)
		monsterB.concealed_set(1)
		monsterC = game.obj_create( 14107, location_from_axis (482L, 496L) )
		monsterC.turn_towards(triggerer)
		monsterC.attack(triggerer)
		monsterC.concealed_set(1)
		monsterD = game.obj_create( 14083, location_from_axis (478L, 501L) )
		monsterD.turn_towards(triggerer)
		monsterD.attack(triggerer)
		monsterD.concealed_set(1)
		monsterE = game.obj_create( 14107, location_from_axis (481L, 506L) )
		monsterE.turn_towards(triggerer)
		monsterE.attack(triggerer)
		monsterE.concealed_set(1)
	game.new_sid = 0
		
	return SKIP_DEFAULT
