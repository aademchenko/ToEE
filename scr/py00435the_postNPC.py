from toee import *
from utilities import *
from Co8 import *
from py00439script_daemon import *


def san_dialog( attachee, triggerer ):
	if (attachee.map == 5001):
		triggerer.begin_dialog( attachee, 1 )
	if (attachee.map == 5051):
		triggerer.begin_dialog( attachee, 200 )
	if (attachee.map == 5121):
		triggerer.begin_dialog( attachee, 400 )
	if attachee.map == 5064:
		triggerer.begin_dialog( attachee, 1000 )
	return SKIP_DEFAULT


def san_first_heartbeat(attachee,triggerer):
	return SKIP_DEFAULT


#def zombie_tele(chaim,moshe,yosef):
#	game.global_vars[830] = chaim
#	game.global_vars[831] = moshe
#	game.global_vars[832] = yosef
#	game.fade_and_teleport(0,0,0,5019,454,467)
#	return SKIP_DEFAULT


def tele2( dialer, town, x, y ):
	game.fade_and_teleport(300,0,0,town,x,y)
	game.timevent_add( bananaphone, ( dialer, x, y ), 100)
	return SKIP_DEFAULT


def bananaphone( dialer, x,y ):
	operator = game.obj_create( 14800, location_from_axis (x+1, y+1) )
	dialer.begin_dialog(operator, 3000)
	#game.particles( "sp-summon monster I", operator )
	return RUN_DEFAULT


def san_heartbeat(attachee,triggerer):
	if (attachee.map == 5051):
		if (game.global_vars[927] == 4 and game.global_flags[929] == 0 and is_daytime() == 0):
			attachee.object_flag_set(OF_OFF)
		else:
			attachee.object_flag_unset(OF_OFF)
	return SKIP_DEFAULT


#def flagtest():
#	game.global_vars[500]=0; #first flag set above 231
#	game.global_vars[501]=0; #first flag set above 380
#	game.global_vars[502]=0; #first flag set above 1001
#
#	flagno=231;
#	while (game.global_flags[flagno] == 0):
#		flagno = flagno + 1;
#	game.global_vars[500]=flagno;
#
#	flagno=380;
#	while (game.global_flags[flagno] == 0):
#		flagno = flagno + 1;
#	game.global_vars[501]=flagno;
#
#	flagno=1001;
#	while (game.global_flags[flagno] == 0):
#		flagno = flagno + 1;
#	game.global_vars[502]=flagno;
#
#	#check the vars in console!
#
#	return SKIP_DEFAULT


def san_start_combat( attachee, triggerer ):
	leader = game.party[0]
	StopCombat(attachee, 0)
	leader.begin_dialog( attachee, 4000 )
	return RUN_DEFAULT
	
	
def should_display_dialog_node( node_name ):
	cur_map = game.leader.map
	if node_name == 'Temple Entrance':
		if cur_map == 5064:
			return 0
	elif node_name == 'Temple Tower Exterior':
		if cur_map == 5113:
			return 0
		if get_f('visited_temple_tower_exterior'):
			return 1
	elif node_name == 'More Upper Proper':
		option_count = 0
		if cur_map != 5064:
			option_count += 1
		if cur_map != 5113 and get_f('visited_temple_tower_exterior'):
			option_count += 1
		if cur_map != 5065 and get_f('visited_temple_tower_interior'):
			option_count += 1
		if cur_map != 5093 and get_f('visited_temple_burnt_farmhouse'):
			option_count += 1
		if cur_map != 5092 and get_f('visited_temple_escape_tunnel'):
			option_count += 1
		if cur_map != 5112 and get_f('visited_temple_ruined_building'):
			option_count += 1
		return option_count >= 5
	elif node_name == 'Level 1':
		if cur_map == 5066:
			return 0
		if get_f('visited_level_1_north_entrance') or get_f('visited_level_1_south_entrance') or get_f('visited_level_1_south_entrance') or game.leader.reputation_has( 11 ) or get_f('visited_secret_spiral_staircase'):
			return 1
	elif node_name == 'Level 1 - North':
		if get_f('visited_level_1_north_entrance'):
			return 1
	elif node_name == 'Level 1 - South':
		if get_f('visited_level_1_south_entrance'):
			return 1
	elif node_name == 'Level 1 - Romag':
		if game.leader.reputation_has( 11 ):
			return 1
	elif node_name == 'Secret Spiral Staircase':
		if get_f('visited_secret_spiral_staircase'):
			return 1
	elif node_name == 'Level 2':
		if cur_map == 5067:
			return 0
		if get_f('visited_level_2_north_west_entrance') or get_f('visited_level_2_centre_entrance') or game.leader.reputation_has( 13 ) or game.leader.reputation_has( 12 ) or game.leader.reputation_has( 10 ):
			return 1
	elif node_name == 'Level 2 - North West':
		if get_f('visited_level_2_north_west_entrance'):
			return 1
	elif node_name == 'Level 2 - Centre':
		if get_f('visited_level_2_centre_entrance'):
			return 1
	elif node_name == 'Level 2 - Alrrem':
		if game.leader.reputation_has( 13 ):
			return 1
	elif node_name == 'Level 2 - Belsornig':
		if game.leader.reputation_has( 12 ):
			return 1
	elif node_name == 'Level 2 - Kelno':
		if game.leader.reputation_has( 10 ):
			return 1
	elif node_name == 'Level 2 More':
		option_count = 0
		if get_f('visited_level_2_north_west_entrance'):
			option_count += 1
		if get_f('visited_level_2_centre_entrance'):
			option_count += 1
		if game.leader.reputation_has( 13 ):
			option_count += 1
		if game.leader.reputation_has( 12 ):
			option_count += 1
		if game.leader.reputation_has( 10 ):
			option_count += 1
		return option_count >= 5	
	elif node_name == 'Secret Spiral Staircase':
		if get_f('visited_secret_spiral_staircase'):
			return 1
	elif node_name == 'Level 3':
		if cur_map == 5105:
			return 0
		if get_f('visited_level_3_east_entrance') or get_f('visited_level_3_west_entrance') or get_f('visited_level_3_south_west_entrance') or get_f('visited_level_3_falrinth'):
			return 1
	elif node_name == 'Level 3 - East':
		if get_f('visited_level_3_east_entrance'):
			return 1
	elif node_name == 'Level 3 - West':
		if get_f('visited_level_3_west_entrance'):
			return 1
	elif node_name == 'Level 3 - South':
		if get_f('visited_level_3_south_west_entrance'):
			return 1
	elif node_name == 'Level 3 - Falrinth':
		if get_f('visited_level_3_falrinth'):
			return 1
	elif node_name == 'Level 4':
		if cur_map == 5080:
			return 0
		if get_f('visited_level_4_main_entrance') or get_f('visited_level_4_nexus') or get_f('visited_level_4_hedrack'):
			return 1
	elif node_name == 'Level 4 - Main':
		if get_f('visited_level_4_main_entrance'):
			return 1
	elif node_name == 'Level 4 - Nexus':
		if get_f('visited_level_4_nexus'):
			return 1
	elif node_name == 'Level 4 - Hedrack':
		if get_f('visited_level_4_hedrack'):
			return 1	
	elif node_name == 'Nodes':
		if get_f('visited_air_node') or get_f('visited_earth_node') or get_f('visited_fire_node') or get_f('visited_water_node'):
			return 1
	elif node_name == 'Air Node':
		if get_f('visited_air_node'):
			return 1
	elif node_name == 'Earth Node':
		if get_f('visited_earth_node'):
			return 1
	elif node_name == 'Fire Node':
		if get_f('visited_fire_node'):
			return 1
	elif node_name == 'Water Node':
		if get_f('visited_water_node'):
			return 1	
	elif node_name == 'Zuggtmoy Level':
		if cur_map == 5079:
			return 0
		if get_f('visited_zuggtmoy_level'):
			return 1
	return 1