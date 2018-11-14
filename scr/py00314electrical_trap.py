from toee import *
from utilities import *
from Co8 import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.global_flags[820] == 1):
		return SKIP_DEFAULT
	elif (anyone( triggerer.group_list(), "has_item", 6114 )):
		triggerer.begin_dialog( attachee, 1 )
	else:
		triggerer.begin_dialog( attachee, 1000 )
	return SKIP_DEFAULT


def san_start_combat( attachee, triggerer ):
	leader = game.party[0]
	StopCombat(attachee, 0)
	leader.begin_dialog( attachee, 4000 )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	game.global_vars[707] = game.global_vars[707] + 1
	if (game.global_vars[707] >= 3 and game.global_flags[820] == 0):
		game.global_vars[707] = 0
		game.particles( 'sp-Call Lightning', attachee )
		game.sound(4019,1)
		for obj in game.obj_list_vicinity( attachee.location, OLC_CRITTERS ):
			if (obj.distance_to(attachee) <= 12 and obj.name != attachee.name and obj.name != 14605):
				game.particles( 'sp-Shocking Grasp', obj )
				game.sound(4030,1)
				if (obj.stat_level_get( stat_hp_current ) >= -9):
#					for chest in game.obj_list_vicinity(attachee.location,OLC_CONTAINER):
#						if (chest.name == 1055):
#							if (obj.has_los(chest)):	
#								obj.turn_towards(chest)
					damage_dice = dice_new( '15d4' )
					if (obj.name == 8035):
						damage_dice = dice_new('5d4')
					if obj.reflex_save_and_damage( OBJ_HANDLE_NULL, 20, D20_Save_Reduction_Half, D20STD_F_NONE, damage_dice, D20DT_ELECTRICITY, D20DAP_UNSPECIFIED, 0 , D20DAP_NORMAL ):
						obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
					else:
						obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
	return RUN_DEFAULT


def zap( attachee, triggerer ):
	damage_dice = dice_new( '5d4' )
	game.particles( 'sp-Shocking Grasp', triggerer )
	game.sound(4030,1)
	if triggerer.reflex_save_and_damage( OBJ_HANDLE_NULL, 20, D20_Save_Reduction_Half, D20STD_F_NONE, damage_dice, D20DT_ELECTRICITY, D20DAP_UNSPECIFIED, 0 , D20DAP_NORMAL ):
		triggerer.float_mesfile_line( 'mes\\spell.mes', 30001 )
	else:
		triggerer.float_mesfile_line( 'mes\\spell.mes', 30002 )
	return RUN_DEFAULT