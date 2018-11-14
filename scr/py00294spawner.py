from toee import *
from utilities import *
from council import council_time
from py00439script_daemon import record_time_stamp, get_v, set_v, npc_set, npc_unset, npc_get, tsc, tpsts, within_rect_by_corners
from combat_standard_routines import *


#Script contains:
# -Hommlet: DH spawns, Council spawns (maps 5001 - Hommlet exterior, 5048 - Town Hall, 5049 - Stonemason)
# -Moathouse: Moathouse respawns
# -delayed DH spawn in Town Hall until after council meeting

def san_first_heartbeat( attachee, triggerer ):
	if ( (game.global_vars[972] == 2) and (attachee.map == 5004) ):
		Moathouse_Respawn(attachee, triggerer)
		return RUN_DEFAULT
	if ( (attachee.map == 5001 or attachee.map == 5048 or attachee.map == 5049) and get_v(435) != 0):
		Council_Script(attachee, triggerer)
	return RUN_DEFAULT

def san_heartbeat( attachee, triggerer ):
	c_time = council_time()
	if ( attachee.map == 5048 and get_v(435) != 0 and c_time == 1):
	# Townhall
		if get_v(435) == 1:
			set_v(435,3)
			Council_Script(attachee, triggerer)
	if (attachee.map == 5048):
	# Townhall
		if (get_v(436) == 3 and get_v(435) < 4):
		#you've found the trap, initiate dialogue with rufus to GTFO
			for npc in game.obj_list_vicinity(attachee.location,OLC_NPC):
				if (npc.name == 8071):
					game.leader.begin_dialog(npc,2000)
	return RUN_DEFAULT


def Moathouse_Respawn(attachee, triggerer):
	game.obj_create( 2050, location_from_axis (487L, 480L) )
	game.obj_create( 2051, location_from_axis (512L, 478L) )
	statue = game.obj_create( 2048, location_from_axis (494L, 484L) )	##statue
	statue.rotation = 5
	attachee.destroy()
	return


def Council_Script(attachee, triggerer):
	if (attachee.map == 5048 and game.global_flags[432] == 0):
		if (get_v(435) == 3):
		#full council assembly spawn
			burne = game.obj_create( 14004, location_from_axis (477, 470) )
			burne.move( location_from_axis (477, 470),0.0,15.0)
			burne.rotation = 2.3
			burne.obj_set_int(obj_f_critter_description_unknown,20000)
			destroy_weapons(burne,4058,0,0)
			rufus = game.obj_create( 14006, location_from_axis (474, 472) )
			rufus.move(location_from_axis (474, 472),15.0,-10.0 )
			rufus.rotation = 2.5
			rufus.obj_set_int(obj_f_critter_description_unknown,8071)
			jaroo = game.obj_create( 14005, location_from_axis (474, 476) )
			jaroo.rotation = 5.5
			destroy_weapons(jaroo,4047,4111,0)
			jaroo.obj_set_int(obj_f_critter_description_unknown,20001)
			renton = game.obj_create( 14012, location_from_axis (477, 475) )
			renton.move(location_from_axis (477, 475),0.0,-8.0 )
			renton.rotation = 5.4
			terjon = game.obj_create( 14007, location_from_axis (480, 474) )
			terjon.move(location_from_axis (480, 474),-25.0,0.0 )
			terjon.rotation = 5.8
			destroy_weapons(terjon,4124,6054,0)
			badger1 = game.obj_create( 14371, location_from_axis (482, 474) )
			badger1.move(location_from_axis (482, 474),0.0,0.0 )
			badger1.rotation = 2.1
			nevets = game.obj_create(14102,location_from_axis(475,477))
			nevets.move(location_from_axis(475,477),-8.0,0.0)
			nevets.rotation = 5.2
			miller = game.obj_create(14031,location_from_axis(477,477))
			miller.move(location_from_axis(477,477),3.0,0.0)
			miller.rotation = 5.3
			gundi = game.obj_create(14016,location_from_axis(479,477))
			gundi.move(location_from_axis(479,477),0.0,0.0)
			gundi.rotation = 5.8

			game.global_flags[432] = 1
			game.leader.begin_dialog(burne, 7000)
		elif (get_v(435) == 2):
		#only badgers spawn, if you suspected R&G
			badger1 = game.obj_create( 14371, location_from_axis (476, 477) )
			badger1.rotation = 2.5
			badger2 = game.obj_create( 14371, location_from_axis (479, 477) )
			badger2.rotation = 2.6
			badger3 = game.obj_create( 14371, location_from_axis (474, 476) )
			badger3.rotation = 2.5
			game.global_flags[432] = 1
	elif (attachee.map == 5048 and get_v(435) >= 4):
		#this should delete everyone after it's all over
		for npc in game.obj_list_vicinity(attachee.location,OLC_NPC):
			if (to_be_deleted(npc) == 1 and npc.leader_get() == OBJ_HANDLE_NULL):
				npc.destroy()
	return

def to_be_deleted(npc):
	#8008 - Gundigoot
	#8054 - Burne
	#14031 - Miller
	#14102 - Nevets
	#14371 - badger
	#20001 - Jaroo
	#20003 - Terjon
	#20007 - Renton
	if (npc.name == 8008 or npc.name == 8048 or npc.name == 8049 or npc.name == 8054 or npc.name == 8071 or npc.name == 14031 or npc.name == 14102 or npc.name == 14806 or npc.name == 14371 or npc.name == 20001 or npc.name == 20003 or npc.name == 20007):
		return 1
	return 0

def destroy_weapons(npc, item1, item2, item3):
	if (item1 != 0):
		moshe = npc.item_find(item1)
		if (moshe != OBJ_HANDLE_NULL):
			moshe.destroy()
	if (item2 != 0):
		moshe = npc.item_find(item2)
		if (moshe != OBJ_HANDLE_NULL):
			moshe.destroy()
	if (item3 != 0):
		moshe = npc.item_find(item3)
		if (moshe != OBJ_HANDLE_NULL):
			moshe.destroy()
	return
