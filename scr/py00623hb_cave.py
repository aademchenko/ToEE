from toee import *
from utilities import *
from py00439script_daemon import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	webbed = break_free( attachee, 3)
##################
#  MELEE TROOPS  #
############################################################
#  dumb guys - gnoll troops, kallop, boonthag, naig lliht  #
############################################################
	if (attachee.name == 8634 or attachee.name == 8815 or attachee.name == 8816 or attachee.name == 8813):
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
#######################################################################
#  dumb guys with rage - bugbear troops, orc fighters, hungous, ergo  #
#######################################################################
	elif (attachee.name == 8632 or attachee.name == 8633 or attachee.name == 8635 or attachee.name == 8803 or attachee.name == 8814):
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
####################################################################
#  smart guys  - might be a bum strategy, too much running around  #
####################################################################
#	elif (attachee.name == xxxx):
#		leader = attachee.leader_get()
#		if (group_percent_hp(leader) >= 51):
#			for obj in game.party[0].group_list():
#				if obj.d20_query(Q_Prone):
#					attachee.obj_set_int(obj_f_critter_strategy, 545)
#				else:
#					attachee.obj_set_int(obj_f_critter_strategy, 550)
#		elif (group_percent_hp(leader) <= 50):
#			for obj in game.party[0].group_list():
#				if obj.d20_query(Q_Prone):
#					attachee.obj_set_int(obj_f_critter_strategy, 545)
#				else:
#					attachee.obj_set_int(obj_f_critter_strategy, 546)
#############################################################################
#  smart guys with rage - might be a bum strategy, too much running around  #
#############################################################################
#	elif (attachee.name == xxxx):
#		leader = attachee.leader_get()
#		if (group_percent_hp(leader) >= 51):
#			for obj in game.party[0].group_list():
#				if obj.d20_query(Q_Prone):
#					attachee.obj_set_int(obj_f_critter_strategy, 560)
#				else:
#					attachee.obj_set_int(obj_f_critter_strategy, 558)
#		elif (group_percent_hp(leader) <= 50):
#			for obj in game.party[0].group_list():
#				if obj.d20_query(Q_Prone):
#					attachee.obj_set_int(obj_f_critter_strategy, 560)
#				else:
#					attachee.obj_set_int(obj_f_critter_strategy, 561)
###########################
#  mage seekers - krunch  #
###########################
	elif (attachee.name == 8802):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 545)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 548)
		elif (group_percent_hp(leader) <= 50):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 545)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 546)
######################################
#  archery seekers with rage - ruff  #
######################################
	elif (attachee.name == 8817):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 560)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 563)
		elif (group_percent_hp(leader) <= 50):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 560)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 561)
###################
#  RANGED TROOPS  #
################################
#  mage seekers - orc snipers  #
################################
	elif (attachee.name == 8630 or attachee.name == 8631):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			attachee.obj_set_int(obj_f_critter_strategy, 555)
		elif (group_percent_hp(leader) <= 50):
			attachee.obj_set_int(obj_f_critter_strategy, 553)
#####################################
#  spell responders - orc marksmen  #
#####################################
	elif (attachee.name == 8628 or attachee.name == 8629):
		for obj in game.party[0].group_list():
			if (obj.stat_level_get(stat_level_wizard) >= 1 or obj.stat_level_get(stat_level_sorcerer) >= 1 or obj.stat_level_get(stat_level_druid) >= 1 or obj.stat_level_get(stat_level_bard) >= 1):
				leader = attachee.leader_get()
				if (group_percent_hp(leader) >= 34):
					attachee.obj_set_int(obj_f_critter_strategy, 557)
				elif (group_percent_hp(leader) <= 33):
					attachee.obj_set_int(obj_f_critter_strategy, 553)
			else:
				leader = attachee.leader_get()
				if (group_percent_hp(leader) >= 34):
					attachee.obj_set_int(obj_f_critter_strategy, 554)
				elif (group_percent_hp(leader) <= 33):
					attachee.obj_set_int(obj_f_critter_strategy, 553)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (attachee.name == 8636):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (see_30(attachee, obj)):
					if (not npc_get(attachee,1)):
						game.particles( 'Mon-Balor-Smokebody60', attachee )
						game.particles( 'ef-fireburning', attachee )
						game.sound( 4185, 1 )
						damage_dice = dice_new( '4d20' )
						attachee.damage( OBJ_HANDLE_NULL, 0, damage_dice )
						npc_set(attachee,1)
						game.global_flags[571] = 1
		elif (attachee.name == 8624 or attachee.name == 8626 or attachee.name == 8628 or attachee.name == 8629 or attachee.name == 8630 or attachee.name == 8631 or attachee.name == 8814 or attachee.name == 8813):
			if (game.global_flags[571] == 1):
				attachee.unconceal()
				game.new_sid = 0
		elif (attachee.name == 8802):
			if (game.global_flags[571] == 1):
				attachee.unconceal()
				attachee.standpoint_set( STANDPOINT_NIGHT, 739 )
				attachee.standpoint_set( STANDPOINT_DAY, 739 )
				game.timevent_add( wake_hungous, (), 10000 )
				game.new_sid = 0
		elif (attachee.name == 8625):
			if (game.global_flags[571] == 1):
				attachee.unconceal()
				attachee.standpoint_set( STANDPOINT_NIGHT, 740 )
				attachee.standpoint_set( STANDPOINT_DAY, 740 )
				game.new_sid = 0
		elif (attachee.name == 8817):
			if (game.global_flags[571] == 1):
				attachee.unconceal()
				attachee.standpoint_set( STANDPOINT_NIGHT, 741 )
				attachee.standpoint_set( STANDPOINT_DAY, 741 )
				game.new_sid = 0
		elif (attachee.name == 8815):
			if (game.global_flags[571] == 1):
				attachee.unconceal()
				attachee.standpoint_set( STANDPOINT_NIGHT, 438 )
				attachee.standpoint_set( STANDPOINT_DAY, 438 )
				game.new_sid = 0
		elif (attachee.name == 8634):
			if (game.global_flags[571] == 1):
				attachee.unconceal()
				attachee.standpoint_set( STANDPOINT_NIGHT, 736 )
				attachee.standpoint_set( STANDPOINT_DAY, 736 )
				game.new_sid = 0
		elif (attachee.name == 8632):
			if (game.global_flags[571] == 1):
				attachee.unconceal()
				attachee.standpoint_set( STANDPOINT_NIGHT, 737 )
				attachee.standpoint_set( STANDPOINT_DAY, 737 )
				game.new_sid = 0
		elif (attachee.name == 8633):
			if (game.global_flags[571] == 1):
				attachee.unconceal()
				attachee.standpoint_set( STANDPOINT_NIGHT, 437 )
				attachee.standpoint_set( STANDPOINT_DAY, 437 )
				game.new_sid = 0
		elif (attachee.name == 8635):
			if (game.global_flags[571] == 1):
				attachee.unconceal()
				attachee.standpoint_set( STANDPOINT_NIGHT, 436 )
				attachee.standpoint_set( STANDPOINT_DAY, 436 )
				game.new_sid = 0
		elif (attachee.name == 8816):
			if (game.global_flags[571] == 1):
				attachee.unconceal()
				attachee.standpoint_set( STANDPOINT_NIGHT, 435 )
				attachee.standpoint_set( STANDPOINT_DAY, 435 )
				game.new_sid = 0
	return RUN_DEFAULT


def see_30(speaker, listener):
	if (speaker.distance_to(listener) <= 30):
		return 1
	return 0


def wake_hungous():
	game.global_vars[570] = 1
	return