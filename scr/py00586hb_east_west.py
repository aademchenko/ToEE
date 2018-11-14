from toee import *
from utilities import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	destroy_gear( attachee, triggerer )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	webbed = break_free( attachee, 3)
##################
#  MELEE TROOPS  #
################################################################################################
#  dumb guys - ettin troops, stone giant troops, hill giant troops, gnoll troops, orc rundors  #
################################################################################################
	if (attachee.name == 14985 or attachee.name == 14986 or attachee.name == 14988 or attachee.name == 14475 or attachee.name == 8610 or attachee.name == 8611 or attachee.name == 8612):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 545)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 547)
		elif (group_percent_hp(leader) <= 50):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 545)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 546)
#######################################################
#  dumb guys with rage - bugbear troops, ogre troops  #
#######################################################
	elif (attachee.name == 14476 or attachee.name == 14990):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 560)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 559)
		elif (group_percent_hp(leader) <= 50):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 560)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 561)
###################
#  RANGED TROOPS  #
############################
#  dumb guys - orc bowmen  #
############################
	elif (attachee.name == 14467):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			attachee.obj_set_int(obj_f_critter_strategy, 552)
		elif (group_percent_hp(leader) <= 50):
			attachee.obj_set_int(obj_f_critter_strategy, 553)
##############################
#  smart guys - orc archers  #
##############################
	elif (attachee.name == 14746):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			attachee.obj_set_int(obj_f_critter_strategy, 551)
		elif (group_percent_hp(leader) <= 50):
			attachee.obj_set_int(obj_f_critter_strategy, 553)
################################
#  mage seekers - orc snipers  #
################################
	elif (attachee.name == 14748):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			attachee.obj_set_int(obj_f_critter_strategy, 555)
		elif (group_percent_hp(leader) <= 50):
			attachee.obj_set_int(obj_f_critter_strategy, 553)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.map == 5095):
		if (not game.combat_is_active()):
			if (attachee != OBJ_HANDLE_NULL and critter_is_unconscious(attachee) != 1 and not attachee.d20_query(Q_Prone) and attachee.leader_get() == OBJ_HANDLE_NULL):
				if (attachee.name == 8610):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (talk_40(attachee, obj)):
							attachee.npc_flag_unset(ONF_WAYPOINTS_DAY)
							attachee.npc_flag_unset(ONF_WAYPOINTS_NIGHT)
							attachee.standpoint_set( STANDPOINT_NIGHT, 432 )
							attachee.standpoint_set( STANDPOINT_DAY, 432 )
							attachee.runoff( location_from_axis( 442, 402 ) )
							game.timevent_add( orc_rund_1_off, ( attachee, triggerer ), 8000 )
				elif (attachee.name == 8611):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (talk_40(attachee, obj)):
							attachee.npc_flag_unset(ONF_WAYPOINTS_DAY)
							attachee.npc_flag_unset(ONF_WAYPOINTS_NIGHT)
							attachee.standpoint_set( STANDPOINT_NIGHT, 433 )
							attachee.standpoint_set( STANDPOINT_DAY, 433 )
							attachee.runoff( location_from_axis( 444, 384 ) )
							game.timevent_add( orc_rund_2_off, ( attachee, triggerer ), 8000 )
	return RUN_DEFAULT


def destroy_gear( attachee, triggerer ):
	dexterity_gloves_2 = attachee.item_find(6199)
	dexterity_gloves_2.destroy()
	longbow_1 = attachee.item_find(4191)
	longbow_1.destroy()
	flaming_longbow_1 = attachee.item_find(4348)
	flaming_longbow_1.destroy()
	dexterity_gloves_4 = attachee.item_find(6200)
	dexterity_gloves_4.destroy()
	longbow_2 = attachee.item_find(4299)
	longbow_2.destroy()
	frost_longbow_2 = attachee.item_find(4349)
	frost_longbow_2.destroy()
	dexterity_gloves_6 = attachee.item_find(6201)
	dexterity_gloves_6.destroy()
	unholy_longbow_2 = attachee.item_find(4482)
	unholy_longbow_2.destroy()
	unholy_longbow_2_electric = attachee.item_find(4350)
	unholy_longbow_2_electric.destroy()
	resist_cloak_2_orange = attachee.item_find(6692)
	resist_cloak_2_orange.destroy()
	resist_cloak_2_fur = attachee.item_find(6682)
	resist_cloak_2_fur.destroy()
	resist_cloak_2_red = attachee.item_find(6667)
	resist_cloak_2_red.destroy()
	unholy_heavy_mace = attachee.item_find(4449)
	unholy_heavy_mace.destroy()
	return


def talk_40(speaker,listener):
	if (speaker.can_see(listener)):
		if (speaker.distance_to(listener) <= 40):
			return 1
	return 0


def orc_rund_1_off( attachee, triggerer ):
	attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def orc_rund_2_off( attachee, triggerer ):
	attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT