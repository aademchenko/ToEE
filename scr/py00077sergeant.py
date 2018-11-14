from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.global_flags[37] == 1 and (game.global_flags[49] == 1 or game.global_flags[48] == 0)):
		triggerer.begin_dialog( attachee, 40 )
	elif (game.global_flags[49] == 1):
		triggerer.begin_dialog( attachee, 60 )
	elif (game.global_flags[48] == 1):
		triggerer.begin_dialog( attachee, 50 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()) and ( game.global_flags[363] == 0 ) and (attachee.leader_get() == OBJ_HANDLE_NULL):
		if (is_better_to_talk(attachee,game.party[0])): 
			if (not critter_is_unconscious(game.party[0])):	
				if (not attachee.has_met(game.party[0])):	
					attachee.turn_towards(game.party[0])
					game.party[0].begin_dialog( attachee, 1 )
					game.new_sid = 0 				
				elif (game.global_flags[49] == 0 and game.global_flags[48] == 1 and game.global_flags[62] == 1):
					attachee.turn_towards(game.party[0])
					game.party[0].begin_dialog( attachee, 50 )
					game.new_sid = 0
				elif (game.global_flags[49] == 1):
					attachee.turn_towards(game.party[0])
					game.party[0].begin_dialog( attachee, 60 )
					game.new_sid = 0
				else:
					attachee.turn_towards(game.party[0])
					game.party[0].begin_dialog( attachee, 70 )
					game.new_sid = 0
		else:
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_safe_to_talk(attachee,obj)):
					if (not attachee.has_met(obj)):
						attachee.turn_towards(obj)
						obj.begin_dialog( attachee, 1 )
					elif (game.global_flags[49] == 0 and game.global_flags[48] == 1 and game.global_flags[62] == 1):
						attachee.turn_towards(obj)
						obj.begin_dialog( attachee, 50 )
					elif (game.global_flags[49] == 1):
						attachee.turn_towards(obj)
						obj.begin_dialog( attachee, 60 )
					else:
						attachee.turn_towards(obj)
						obj.begin_dialog( attachee, 70 )
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	loc = location_from_axis(526,569)
	attachee.runoff(loc)
	return RUN_DEFAULT


def move_pc( attachee, triggerer ):
	game.fade_and_teleport(0,0,0,5005,537,545)
	# triggerer.move( location_from_axis( 537, 545 ) )
	return RUN_DEFAULT


def deliver_pc( attachee, triggerer ):
	triggerer.move( location_from_axis( 491, 541 ) )
	return RUN_DEFAULT
	

def is_better_to_talk(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 20):
			return 1
	return 0


def call_leader(npc, pc): 
	leader = game.party[0]
	leader.move(pc.location - 2)
	leader.begin_dialog(npc, 1)
	return 


def real_time_regroup():
	for obj in game.obj_list_vicinity( location_from_axis(512, 549), OLC_NPC ):
		xx, yy = location_to_axis(obj.location)
		if obj.name == 14074 and xx > 496 and yy > 544: 
			# Corridor guardsmen
			if xx == 497 and yy == 549: 
				# archer
				sps(obj, 639)
				obj.obj_set_int(obj_f_speed_walk, 1085353216)
				obj.npc_flag_set(ONF_WAYPOINTS_DAY)
				obj.npc_flag_set(ONF_WAYPOINTS_NIGHT)
				game.timevent_add( twitch_stop, (obj, 3.14), 4100)
				game.timevent_add( twitch_stop, (obj, 3.14), 5600)

			elif xx == 507 and yy == 549: 
				# swordsman
				sps(obj, 638)
				obj.obj_set_int(obj_f_speed_walk, 1085353216)
				obj.npc_flag_set(ONF_WAYPOINTS_DAY)
				obj.npc_flag_set(ONF_WAYPOINTS_NIGHT)
				game.timevent_add( twitch_stop, (obj, 2.35), 4200)
				game.timevent_add( twitch_stop, (obj, 2.35), 5500)


			elif xx == 515 and yy == 548: 
				# spearbearer
				sps(obj, 637)
				obj.obj_set_int(obj_f_speed_walk, 1085353216)
				obj.npc_flag_set(ONF_WAYPOINTS_DAY)
				obj.npc_flag_set(ONF_WAYPOINTS_NIGHT)
				game.timevent_add( twitch_stop, (obj, 4), 4300)
				game.timevent_add( twitch_stop, (obj, 4), 5400)




def twitch_stop( obj, rot_new ):
	obj.npc_flag_unset(ONF_WAYPOINTS_DAY)
	obj.npc_flag_unset(ONF_WAYPOINTS_NIGHT)
	obj.rotation = rot_new

#495, 534, rot = 2.35 - melee guy
# 481, 530, rot = 3.14 - archer
# 483, 541, rot = 4 - spear


def sps(object_to_be_transferred,new_standpoint_ID):
	## standpoint set
	object_to_be_transferred.standpoint_set(STANDPOINT_DAY, new_standpoint_ID)
	object_to_be_transferred.standpoint_set(STANDPOINT_NIGHT, new_standpoint_ID)
	return