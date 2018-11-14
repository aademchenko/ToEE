from toee import *
from utilities import *
from combat_standard_routines import *


def san_enter_combat( attachee, triggerer ):
	if (attachee.name == 8911):
		if (game.global_flags[552] == 0):
			game.global_flags[551] = 1
	elif (attachee.name == 8894):
		if (game.global_flags[551] == 0):
			game.global_flags[552] = 1
	return RUN_DEFAULT


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
#  dumb guys - orc rundors, gnoll troops, ettin troops, stone giant troops, hill giant troops  #
################################################################################################
	if (attachee.name == 8896 or attachee.name == 8897 or attachee.name == 8898 or attachee.name == 8904 or attachee.name == 8905 or attachee.name == 8906 or attachee.name == 8907 or attachee.name == 8908 or attachee.name == 8619 or attachee.name == 8620 or attachee.name == 8621):
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
#####################################################################
#  dumb guys with rage - bugbear troops, orc fighters, ogre troops  #
#####################################################################
	elif (attachee.name == 8911 or attachee.name == 8614 or attachee.name == 8615 or attachee.name == 8618):
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
###############################################
#  smart guys - kallop, boonthag, naig lliht  #
###############################################
	elif (attachee.name == 8815 or attachee.name == 8816 or attachee.name == 8813):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 545)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 550)
		elif (group_percent_hp(leader) <= 50):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 545)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 546)
#######################################################
#  smart guys with rage - hungous, orc trainer, ergo  #
#######################################################
	elif (attachee.name == 8803 or attachee.name == 8922 or attachee.name == 8814 or attachee.name == 8617):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 560)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 558)
		elif (group_percent_hp(leader) <= 50):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 560)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 561)
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
##########################################################
#  mage seekers with rage - orc murderer, orc dominator  #
##########################################################
	elif (attachee.name == 8895):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 560)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 562)
		elif (group_percent_hp(leader) <= 50):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 560)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 561)
##################################
#  archery seekers - nobody atm  #
##################################
#	elif (attachee.name == xxxxx or attachee.name == xxxxx):
#		leader = attachee.leader_get()
#		if (group_percent_hp(leader) >= 51):
#			for obj in game.party[0].group_list():
#				if obj.d20_query(Q_Prone):
#					attachee.obj_set_int(obj_f_critter_strategy, 545)
#				else:
#					attachee.obj_set_int(obj_f_critter_strategy, 549)
#		elif (group_percent_hp(leader) <= 50):
#			for obj in game.party[0].group_list():
#				if obj.d20_query(Q_Prone):
#					attachee.obj_set_int(obj_f_critter_strategy, 545)
#				else:
#					attachee.obj_set_int(obj_f_critter_strategy, 546)
####################################################
#  archery seekers with rage - orc sergeant, ruff  #
####################################################
	elif (attachee.name == 8817 or attachee.name == 8894):
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
###########################
#  flankers - nobody atm  #
###########################
#	elif (attachee.name == xxxxx):
#		leader = attachee.leader_get()
#		if (group_percent_hp(leader) >= 51):
#			for obj in game.party[0].group_list():
#				if obj.d20_query(Q_Prone):
#					attachee.obj_set_int(obj_f_critter_strategy, 545)
#				else:
#					attachee.obj_set_int(obj_f_critter_strategy, 556)
#		elif (group_percent_hp(leader) <= 50):
#			for obj in game.party[0].group_list():
#				if obj.d20_query(Q_Prone):
#					attachee.obj_set_int(obj_f_critter_strategy, 545)
#				else:
#					attachee.obj_set_int(obj_f_critter_strategy, 553)
#######################################
#  flankers with rage - orc assassin  #
#######################################
	elif (attachee.name == 8616):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 560)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 564)
		elif (group_percent_hp(leader) <= 50):
			for obj in game.party[0].group_list():
				if obj.d20_query(Q_Prone):
					attachee.obj_set_int(obj_f_critter_strategy, 560)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 561)
#############################
#  concealed guys - ettins  #
#############################
	elif (attachee.name == 8912 or attachee.name == 8913 or attachee.name == 8914 or attachee.name == 8915 or attachee.name == 8916):
		if (obj_percent_hp(attachee) <= 75):
			attachee.obj_set_int(obj_f_critter_strategy, 547)
		elif (obj_percent_hp(attachee) >= 76):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_close(attachee, obj)):
					attachee.obj_set_int(obj_f_critter_strategy, 547)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 565)
###################
#  RANGED TROOPS  #
############################
#  dumb guys - orc bowmen  #
############################
	elif (attachee.name == 8899 or attachee.name == 8900 or attachee.name == 8917 or attachee.name == 8918):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			attachee.obj_set_int(obj_f_critter_strategy, 552)
		elif (group_percent_hp(leader) <= 50):
			attachee.obj_set_int(obj_f_critter_strategy, 553)
##############################
#  smart guys - orc archers  #
##############################
	elif (attachee.name == 8901 or attachee.name == 8902 or attachee.name == 8919):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			attachee.obj_set_int(obj_f_critter_strategy, 551)
		elif (group_percent_hp(leader) <= 50):
			attachee.obj_set_int(obj_f_critter_strategy, 553)
################################
#  mage seekers - orc snipers  #
################################
	elif (attachee.name == 8903):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			attachee.obj_set_int(obj_f_critter_strategy, 555)
		elif (group_percent_hp(leader) <= 50):
			attachee.obj_set_int(obj_f_critter_strategy, 553)
##################################
#  archery seekers - nobody atm  #
##################################
#	elif (attachee.name == xxxxx):
#		leader = attachee.leader_get()
#		if (group_percent_hp(leader) >= 51):
#			attachee.obj_set_int(obj_f_critter_strategy, 554)
#		elif (group_percent_hp(leader) <= 50):
#			attachee.obj_set_int(obj_f_critter_strategy, 553)
#####################################
#  spell responders - orc marksmen  #
#####################################
#	elif (attachee.name == 14749):
#		for obj in game.party[0].group_list():
#			if (obj.stat_level_get(stat_level_wizard) >= 1 or obj.stat_level_get(stat_level_sorcerer) >= 1 or obj.stat_level_get(stat_level_druid) >= 1 or obj.stat_level_get(stat_level_bard) >= 1):
#				leader = attachee.leader_get()
#				if (group_percent_hp(leader) >= 34):
#					attachee.obj_set_int(obj_f_critter_strategy, 557)
#				elif (group_percent_hp(leader) <= 33):
#					attachee.obj_set_int(obj_f_critter_strategy, 553)
#			else:
#				leader = attachee.leader_get()
#				if (group_percent_hp(leader) >= 34):
#					attachee.obj_set_int(obj_f_critter_strategy, 554)
#				elif (group_percent_hp(leader) <= 33):
#					attachee.obj_set_int(obj_f_critter_strategy, 553)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.name == 8894):
		if (game.global_flags[551] == 1):
			attachee.npc_flag_unset(ONF_WAYPOINTS_DAY)
			attachee.npc_flag_unset(ONF_WAYPOINTS_NIGHT)
			attachee.standpoint_set( STANDPOINT_NIGHT, 601 )
			attachee.standpoint_set( STANDPOINT_DAY, 601 )
			game.new_sid = 0
	elif (attachee.name == 8895):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 602 )
			attachee.standpoint_set( STANDPOINT_DAY, 602 )
			game.new_sid = 0
	elif (attachee.name == 8896):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 603 )
			attachee.standpoint_set( STANDPOINT_DAY, 603 )
			game.new_sid = 0
	elif (attachee.name == 8897):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 604 )
			attachee.standpoint_set( STANDPOINT_DAY, 604 )
			game.new_sid = 0
	elif (attachee.name == 8898):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 605 )
			attachee.standpoint_set( STANDPOINT_DAY, 605 )
			game.new_sid = 0
	elif (attachee.name == 8899):
		if (game.global_flags[551] == 1):
			attachee.unconceal()
			attachee.standpoint_set( STANDPOINT_NIGHT, 606 )
			attachee.standpoint_set( STANDPOINT_DAY, 606 )
			game.new_sid = 0
	elif (attachee.name == 8900):
		if (game.global_flags[551] == 1):
			attachee.unconceal()
			attachee.standpoint_set( STANDPOINT_NIGHT, 607 )
			attachee.standpoint_set( STANDPOINT_DAY, 607 )
			game.new_sid = 0
	elif (attachee.name == 8901):
		if (game.global_flags[551] == 1):
			attachee.unconceal()
			attachee.standpoint_set( STANDPOINT_NIGHT, 608 )
			attachee.standpoint_set( STANDPOINT_DAY, 608 )
			game.new_sid = 0
	elif (attachee.name == 8902):
		if (game.global_flags[551] == 1):
			attachee.unconceal()
			attachee.standpoint_set( STANDPOINT_NIGHT, 609 )
			attachee.standpoint_set( STANDPOINT_DAY, 609 )
			game.new_sid = 0
	elif (attachee.name == 8903):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 610 )
			attachee.standpoint_set( STANDPOINT_DAY, 610 )
			game.new_sid = 0
	elif (attachee.name == 8904):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 611 )
			attachee.standpoint_set( STANDPOINT_DAY, 611 )
			game.new_sid = 0
	elif (attachee.name == 8905):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 612 )
			attachee.standpoint_set( STANDPOINT_DAY, 612 )
			game.new_sid = 0
	elif (attachee.name == 8906):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 613 )
			attachee.standpoint_set( STANDPOINT_DAY, 613 )
			game.new_sid = 0
	elif (attachee.name == 8907):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 614 )
			attachee.standpoint_set( STANDPOINT_DAY, 614 )
			game.new_sid = 0
	elif (attachee.name == 8908):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 615 )
			attachee.standpoint_set( STANDPOINT_DAY, 615 )
			game.new_sid = 0
	elif (attachee.name == 8909):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 616 )
			attachee.standpoint_set( STANDPOINT_DAY, 616 )
			game.new_sid = 0
	elif (attachee.name == 8910):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 617 )
			attachee.standpoint_set( STANDPOINT_DAY, 617 )
			game.new_sid = 0
	elif (attachee.name == 8911):
		if (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 618 )
			attachee.standpoint_set( STANDPOINT_DAY, 618 )
			game.new_sid = 0
	elif (attachee.name == 8912):
		if (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 619 )
			attachee.standpoint_set( STANDPOINT_DAY, 619 )
			attachee.obj_set_int(obj_f_critter_strategy, 547)
			game.new_sid = 0
	elif (attachee.name == 8913):
		if (game.global_flags[552] == 1):
			attachee.unconceal()
			attachee.standpoint_set( STANDPOINT_NIGHT, 620 )
			attachee.standpoint_set( STANDPOINT_DAY, 620 )
			attachee.obj_set_int(obj_f_critter_strategy, 547)
			game.new_sid = 0
	elif (attachee.name == 8914):
		if (game.global_flags[552] == 1):
			attachee.unconceal()
			attachee.standpoint_set( STANDPOINT_NIGHT, 621 )
			attachee.standpoint_set( STANDPOINT_DAY, 621 )
			attachee.obj_set_int(obj_f_critter_strategy, 547)
			game.new_sid = 0
	elif (attachee.name == 8915):
		if (game.global_flags[552] == 1):
			attachee.unconceal()
			attachee.standpoint_set( STANDPOINT_NIGHT, 622 )
			attachee.standpoint_set( STANDPOINT_DAY, 622 )
			attachee.obj_set_int(obj_f_critter_strategy, 547)
			game.new_sid = 0
	elif (attachee.name == 8916):
		if (game.global_flags[552] == 1):
			attachee.unconceal()
			attachee.standpoint_set( STANDPOINT_NIGHT, 623 )
			attachee.standpoint_set( STANDPOINT_DAY, 623 )
			attachee.obj_set_int(obj_f_critter_strategy, 547)
			game.new_sid = 0
	elif (attachee.name == 8917):
		if (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 624 )
			attachee.standpoint_set( STANDPOINT_DAY, 624 )
			game.new_sid = 0
	elif (attachee.name == 8918):
		if (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 625 )
			attachee.standpoint_set( STANDPOINT_DAY, 625 )
			game.new_sid = 0
	elif (attachee.name == 8919):
		if (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 626 )
			attachee.standpoint_set( STANDPOINT_DAY, 626 )
			game.new_sid = 0
	elif (attachee.name == 8920):
		if (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 627 )
			attachee.standpoint_set( STANDPOINT_DAY, 627 )
			game.new_sid = 0
	elif (attachee.name == 8921):
		if (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 628 )
			attachee.standpoint_set( STANDPOINT_DAY, 628 )
			game.new_sid = 0
	elif (attachee.name == 8922):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 630 )
			attachee.standpoint_set( STANDPOINT_DAY, 630 )
			game.new_sid = 0
		elif (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 644 )
			attachee.standpoint_set( STANDPOINT_DAY, 644 )
			game.new_sid = 0
	elif (attachee.name == 8923):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 631 )
			attachee.standpoint_set( STANDPOINT_DAY, 631 )
			game.new_sid = 0
		elif (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 645 )
			attachee.standpoint_set( STANDPOINT_DAY, 645 )
			game.new_sid = 0
	elif (attachee.name == 8924):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 632 )
			attachee.standpoint_set( STANDPOINT_DAY, 632 )
			game.new_sid = 0
		elif (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 646 )
			attachee.standpoint_set( STANDPOINT_DAY, 646 )
			game.new_sid = 0
	elif (attachee.name == 8925):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 633 )
			attachee.standpoint_set( STANDPOINT_DAY, 633 )
			game.new_sid = 0
		elif (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 647 )
			attachee.standpoint_set( STANDPOINT_DAY, 647 )
			game.new_sid = 0
	elif (attachee.name == 8926):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 634 )
			attachee.standpoint_set( STANDPOINT_DAY, 634 )
			game.new_sid = 0
		elif (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 648 )
			attachee.standpoint_set( STANDPOINT_DAY, 648 )
			game.new_sid = 0
	elif (attachee.name == 8927):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 635 )
			attachee.standpoint_set( STANDPOINT_DAY, 635 )
			game.new_sid = 0
		elif (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 649 )
			attachee.standpoint_set( STANDPOINT_DAY, 649 )
			game.new_sid = 0
	elif (attachee.name == 8928):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 636 )
			attachee.standpoint_set( STANDPOINT_DAY, 636 )
			game.new_sid = 0
		elif (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 571 )
			attachee.standpoint_set( STANDPOINT_DAY, 571 )
			game.new_sid = 0
	elif (attachee.name == 8929):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 642 )
			attachee.standpoint_set( STANDPOINT_DAY, 642 )
			game.new_sid = 0
		elif (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 572 )
			attachee.standpoint_set( STANDPOINT_DAY, 572 )
			game.new_sid = 0
	elif (attachee.name == 8930):
		if (game.global_flags[551] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 643 )
			attachee.standpoint_set( STANDPOINT_DAY, 643 )
			game.new_sid = 0
		elif (game.global_flags[552] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 573 )
			attachee.standpoint_set( STANDPOINT_DAY, 573 )
			game.new_sid = 0
	return RUN_DEFAULT


def is_close( attachee, obj ):
	if (attachee.distance_to(obj) <= 15):
		return 1
	return 0


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