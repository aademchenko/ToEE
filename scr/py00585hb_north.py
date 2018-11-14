from toee import *
from utilities import *
from py00439script_daemon import within_rect_by_corners
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (attachee.name == 8999):
		if (game.global_flags[556] == 0):
			game.global_flags[555] = 1
	elif (attachee.name == 8994):
		if (game.global_flags[555] == 0):
			game.global_flags[556] = 1
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	webbed = break_free( attachee, 3)
##################
#  MELEE TROOPS  #
#####################################################
#  dumb guys with rage - orc fighters, ogre troops  #
#####################################################
	if (attachee.name == 8994 or attachee.name == 8601 or attachee.name == 8602 or attachee.name == 8603 or attachee.name == 8604 or attachee.name == 8605 or attachee.name == 8606):
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
		for obj in game.obj_list_vicinity( attachee.location, OLC_CRITTERS ):
			if (within_rect_by_corners(obj, 538, 394, 531, 408)):
#				obj.condition_add_with_args("Prone",0,0)
				coord_x = game.random_range(522,526)
				coord_y = game.random_range(405,409)
				obj.move(location_from_axis (coord_x, coord_y))
				game.particles( "Mon-Phycomid-10", obj )
				obj.float_mesfile_line( 'mes\\float.mes', 2 )
				game.sound( 4177, 1 )
				game.global_flags[557] = 1
			if (within_rect_by_corners(obj, 487, 398, 481, 412)):
#				obj.condition_add_with_args("Prone",0,0)
				coord_x = game.random_range(499,503)
				coord_y = game.random_range(405,409)
				obj.move(location_from_axis (coord_x, coord_y))
				game.particles( "Mon-Phycomid-10", obj )
				obj.float_mesfile_line( 'mes\\float.mes', 2 )
				game.sound( 4177, 1 )
				game.global_flags[557] = 1
		if (game.global_flags[557] == 1 and game.global_vars[568] == 0):
			game.global_vars[568] = 1
		elif (game.global_flags[557] == 1 and game.global_vars[568] == 1):
			game.sound( 4180, 1 )
			game.global_vars[568] = 2
		elif (game.global_flags[557] == 1 and game.global_vars[568] == 2):
			spawn_hydra()
###########################################
#  mage seekers with rage - orc murderer  #
###########################################
	elif (attachee.name == 8992):
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
		for obj in game.obj_list_vicinity( attachee.location, OLC_CRITTERS ):
			if (within_rect_by_corners(obj, 538, 394, 531, 408)):
#				obj.condition_add_with_args("Prone",0,0)
				coord_x = game.random_range(522,526)
				coord_y = game.random_range(405,409)
				obj.move(location_from_axis (coord_x, coord_y))
				game.particles( "Mon-Phycomid-10", obj )
				obj.float_mesfile_line( 'mes\\float.mes', 2 )
				game.sound( 4177, 1 )
				game.global_flags[557] = 1
			if (within_rect_by_corners(obj, 487, 398, 481, 412)):
#				obj.condition_add_with_args("Prone",0,0)
				coord_x = game.random_range(499,503)
				coord_y = game.random_range(405,409)
				obj.move(location_from_axis (coord_x, coord_y))
				game.particles( "Mon-Phycomid-10", obj )
				obj.float_mesfile_line( 'mes\\float.mes', 2 )
				game.sound( 4177, 1 )
				game.global_flags[557] = 1
		if (game.global_flags[557] == 1 and game.global_vars[568] == 0):
			game.global_vars[568] = 1
		elif (game.global_flags[557] == 1 and game.global_vars[568] == 1):
			game.sound( 4180, 1 )
			game.global_vars[568] = 2
		elif (game.global_flags[557] == 1 and game.global_vars[568] == 2):
			spawn_hydra()
##############################################
#  archery seekers with rage - orc sergeant  #
##############################################
	elif (attachee.name == 8993):
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
		for obj in game.obj_list_vicinity( attachee.location, OLC_CRITTERS ):
			if (within_rect_by_corners(obj, 538, 394, 531, 408)):
#				obj.condition_add_with_args("Prone",0,0)
				coord_x = game.random_range(522,526)
				coord_y = game.random_range(405,409)
				obj.move(location_from_axis (coord_x, coord_y))
				game.particles( "Mon-Phycomid-10", obj )
				obj.float_mesfile_line( 'mes\\float.mes', 2 )
				game.sound( 4177, 1 )
				game.global_flags[557] = 1
			if (within_rect_by_corners(obj, 487, 398, 481, 412)):
#				obj.condition_add_with_args("Prone",0,0)
				coord_x = game.random_range(499,503)
				coord_y = game.random_range(405,409)
				obj.move(location_from_axis (coord_x, coord_y))
				game.particles( "Mon-Phycomid-10", obj )
				obj.float_mesfile_line( 'mes\\float.mes', 2 )
				game.sound( 4177, 1 )
				game.global_flags[557] = 1
		if (game.global_flags[557] == 1 and game.global_vars[568] == 0):
			game.global_vars[568] = 1
		elif (game.global_flags[557] == 1 and game.global_vars[568] == 1):
			game.sound( 4180, 1 )
			game.global_vars[568] = 2
		elif (game.global_flags[557] == 1 and game.global_vars[568] == 2):
			spawn_hydra()
#######################################
#  flankers with rage - orc assassin  #
#######################################
	elif (attachee.name == 8999):
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
		for obj in game.obj_list_vicinity( attachee.location, OLC_CRITTERS ):
			if (within_rect_by_corners(obj, 538, 394, 531, 408)):
#				obj.condition_add_with_args("Prone",0,0)
				coord_x = game.random_range(522,526)
				coord_y = game.random_range(405,409)
				obj.move(location_from_axis (coord_x, coord_y))
				game.particles( "Mon-Phycomid-10", obj )
				obj.float_mesfile_line( 'mes\\float.mes', 2 )
				game.sound( 4177, 1 )
				game.global_flags[557] = 1
			if (within_rect_by_corners(obj, 487, 398, 481, 412)):
#				obj.condition_add_with_args("Prone",0,0)
				coord_x = game.random_range(499,503)
				coord_y = game.random_range(405,409)
				obj.move(location_from_axis (coord_x, coord_y))
				game.particles( "Mon-Phycomid-10", obj )
				obj.float_mesfile_line( 'mes\\float.mes', 2 )
				game.sound( 4177, 1 )
				game.global_flags[557] = 1
		if (game.global_flags[557] == 1 and game.global_vars[568] == 0):
			game.global_vars[568] = 1
		elif (game.global_flags[557] == 1 and game.global_vars[568] == 1):
			game.sound( 4180, 1 )
			game.global_vars[568] = 2
		elif (game.global_flags[557] == 1 and game.global_vars[568] == 2):
			spawn_hydra()
###################
#  RANGED TROOPS  #
############################
################################
#  mage seekers - orc snipers  #
################################
	elif (attachee.name == 8995 or attachee.name == 8996 or attachee.name == 8607 or attachee.name == 8608):
		leader = attachee.leader_get()
		if (group_percent_hp(leader) >= 51):
			attachee.obj_set_int(obj_f_critter_strategy, 555)
		elif (group_percent_hp(leader) <= 50):
			attachee.obj_set_int(obj_f_critter_strategy, 553)
		for obj in game.obj_list_vicinity( attachee.location, OLC_CRITTERS ):
			if (within_rect_by_corners(obj, 538, 394, 531, 408)):
#				obj.condition_add_with_args("Prone",0,0)
				coord_x = game.random_range(522,526)
				coord_y = game.random_range(405,409)
				obj.move(location_from_axis (coord_x, coord_y))
				game.particles( "Mon-Phycomid-10", obj )
				obj.float_mesfile_line( 'mes\\float.mes', 2 )
				game.sound( 4177, 1 )
				game.global_flags[557] = 1
			if (within_rect_by_corners(obj, 487, 398, 481, 412)):
#				obj.condition_add_with_args("Prone",0,0)
				coord_x = game.random_range(499,503)
				coord_y = game.random_range(405,409)
				obj.move(location_from_axis (coord_x, coord_y))
				game.particles( "Mon-Phycomid-10", obj )
				obj.float_mesfile_line( 'mes\\float.mes', 2 )
				game.sound( 4177, 1 )
				game.global_flags[557] = 1
		if (game.global_flags[557] == 1 and game.global_vars[568] == 0):
			game.global_vars[568] = 1
		elif (game.global_flags[557] == 1 and game.global_vars[568] == 1):
			game.sound( 4180, 1 )
			game.global_vars[568] = 2
		elif (game.global_flags[557] == 1 and game.global_vars[568] == 2):
			spawn_hydra()
#####################################
#  spell responders - orc marksmen  #
#####################################
	elif (attachee.name == 8997 or attachee.name == 8609):
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
		for obj in game.obj_list_vicinity( attachee.location, OLC_CRITTERS ):
			if (within_rect_by_corners(obj, 538, 394, 531, 408)):
#				obj.condition_add_with_args("Prone",0,0)
				coord_x = game.random_range(522,526)
				coord_y = game.random_range(405,409)
				obj.move(location_from_axis (coord_x, coord_y))
				game.particles( "Mon-Phycomid-10", obj )
				obj.float_mesfile_line( 'mes\\float.mes', 2 )
				game.sound( 4177, 1 )
				game.global_flags[557] = 1
			if (within_rect_by_corners(obj, 487, 398, 481, 412)):
#				obj.condition_add_with_args("Prone",0,0)
				coord_x = game.random_range(499,503)
				coord_y = game.random_range(405,409)
				obj.move(location_from_axis (coord_x, coord_y))
				game.particles( "Mon-Phycomid-10", obj )
				obj.float_mesfile_line( 'mes\\float.mes', 2 )
				game.sound( 4177, 1 )
				game.global_flags[557] = 1
		if (game.global_flags[557] == 1 and game.global_vars[568] == 0):
			game.global_vars[568] = 1
		elif (game.global_flags[557] == 1 and game.global_vars[568] == 1):
			game.sound( 4180, 1 )
			game.global_vars[568] = 2
		elif (game.global_flags[557] == 1 and game.global_vars[568] == 2):
			spawn_hydra()
#####################
#  animals - hydra  #
#####################
	elif (attachee.name == 14982):
		game.global_vars[568] = game.global_vars[568] + 1
		if (game.global_vars[568] == 4):
			picker = game.random_range(14978,14981)
			animal = game.obj_create( picker, location_from_axis (511L, 423L) )
			animal.move(location_from_axis (515L, 424L))
			animal.rotation = 5.49778714378
			animal.concealed_set(1)
			animal.unconceal()
			game.particles( "Mon-YellowMold-30", animal )
			game.sound( 4181, 1 )
		elif (game.global_vars[568] == 5):
			picker = game.random_range(14978,14981)
			animal = game.obj_create( picker, location_from_axis (511L, 423L) )
			animal.move(location_from_axis (507L, 424L))
			animal.rotation = 5.49778714378
			animal.concealed_set(1)
			animal.unconceal()
			game.particles( "Mon-YellowMold-30", animal )
			game.sound( 4181, 1 )
		elif (game.global_vars[568] == 6):
			picker = game.random_range(14978,14981)
			animal = game.obj_create( picker, location_from_axis (511L, 423L) )
			animal.move(location_from_axis (519L, 424L))
			animal.rotation = 5.49778714378
			animal.concealed_set(1)
			animal.unconceal()
			game.particles( "Mon-YellowMold-30", animal )
			game.sound( 4181, 1 )
		elif (game.global_vars[568] == 7):
			picker = game.random_range(14978,14981)
			animal = game.obj_create( picker, location_from_axis (511L, 423L) )
			animal.move(location_from_axis (503L, 424L))
			animal.rotation = 5.49778714378
			animal.concealed_set(1)
			animal.unconceal()
			game.particles( "Mon-YellowMold-30", animal )
			game.sound( 4181, 1 )
		elif (game.global_vars[568] == 8):
			picker = game.random_range(14978,14981)
			animal = game.obj_create( picker, location_from_axis (511L, 423L) )
			animal.move(location_from_axis (523L, 424L))
			animal.rotation = 5.49778714378
			animal.concealed_set(1)
			animal.unconceal()
			game.particles( "Mon-YellowMold-30", animal )
			game.sound( 4181, 1 )
		elif (game.global_vars[568] == 9):
			picker = game.random_range(14978,14981)
			animal = game.obj_create( picker, location_from_axis (511L, 423L) )
			animal.move(location_from_axis (499L, 424L))
			animal.rotation = 5.49778714378
			animal.concealed_set(1)
			animal.unconceal()
			game.particles( "Mon-YellowMold-30", animal )
			game.sound( 4181, 1 )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.name == 8999):
		if (game.global_flags[555] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 406 )
			attachee.standpoint_set( STANDPOINT_DAY, 406 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 9000):
		if (game.global_flags[555] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 405 )
			attachee.standpoint_set( STANDPOINT_DAY, 405 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 8601):
		if (game.global_flags[555] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 408 )
			attachee.standpoint_set( STANDPOINT_DAY, 408 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 8602):
		if (game.global_flags[555] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 409 )
			attachee.standpoint_set( STANDPOINT_DAY, 409 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 8603):
		if (game.global_flags[555] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 410 )
			attachee.standpoint_set( STANDPOINT_DAY, 410 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 8604):
		if (game.global_flags[555] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 411 )
			attachee.standpoint_set( STANDPOINT_DAY, 411 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 8605):
		if (game.global_flags[555] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 413 )
			attachee.standpoint_set( STANDPOINT_DAY, 413 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 8606):
		if (game.global_flags[555] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 417 )
			attachee.standpoint_set( STANDPOINT_DAY, 417 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 8607):
		if (game.global_flags[555] == 1):
			attachee.unconceal()
#			attachee.move(location_from_axis (511L, 364L))
			attachee.standpoint_set( STANDPOINT_NIGHT, 419 )
			attachee.standpoint_set( STANDPOINT_DAY, 419 )
			attachee.npc_flag_unset(ONF_KOS)
#			attachee.rotation = 2.35619449019
			game.new_sid = 0
	elif (attachee.name == 8608):
		if (game.global_flags[555] == 1):
			attachee.unconceal()
#			attachee.move(location_from_axis (506L, 364L))
			attachee.standpoint_set( STANDPOINT_NIGHT, 420 )
			attachee.standpoint_set( STANDPOINT_DAY, 420 )
			attachee.npc_flag_unset(ONF_KOS)
#			attachee.rotation = 2.35619449019
			game.new_sid = 0
	elif (attachee.name == 8609):
		if (game.global_flags[555] == 1):
			attachee.unconceal()
#			attachee.move(location_from_axis (508L, 361L))
			attachee.standpoint_set( STANDPOINT_NIGHT, 421 )
			attachee.standpoint_set( STANDPOINT_DAY, 421 )
			attachee.npc_flag_unset(ONF_KOS)
#			attachee.rotation = 2.35619449019
			game.new_sid = 0
	elif (attachee.name == 8992):
		if (game.global_flags[556] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 297 )
			attachee.standpoint_set( STANDPOINT_DAY, 297 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 8993):
		if (game.global_flags[556] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 298 )
			attachee.standpoint_set( STANDPOINT_DAY, 298 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 8994):
		if (game.global_flags[556] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 299 )
			attachee.standpoint_set( STANDPOINT_DAY, 299 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 8995):
		if (game.global_flags[556] == 1):
			attachee.unconceal()
			attachee.standpoint_set( STANDPOINT_NIGHT, 336 )
			attachee.standpoint_set( STANDPOINT_DAY, 336 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 8996):
		if (game.global_flags[556] == 1):
			attachee.unconceal()
			attachee.standpoint_set( STANDPOINT_NIGHT, 404 )
			attachee.standpoint_set( STANDPOINT_DAY, 404 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 8997):
		if (game.global_flags[556] == 1):
			attachee.unconceal()
			attachee.standpoint_set( STANDPOINT_NIGHT, 333 )
			attachee.standpoint_set( STANDPOINT_DAY, 333 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	elif (attachee.name == 8998):
		if (game.global_flags[556] == 1):
			attachee.standpoint_set( STANDPOINT_NIGHT, 300 )
			attachee.standpoint_set( STANDPOINT_DAY, 300 )
			attachee.npc_flag_unset(ONF_KOS)
			game.new_sid = 0
	return RUN_DEFAULT


def spawn_hydra():
	hydra = game.obj_create( 14982, location_from_axis (511L, 423L) )
	hydra.move(location_from_axis (511L, 424L))
	hydra.rotation = 5.49778714378
	hydra.concealed_set(1)
	hydra.unconceal()
	game.particles( "Mon-YellowMold-30", hydra )
	game.sound( 4179, 1 )
	game.global_vars[568] = 3
	return