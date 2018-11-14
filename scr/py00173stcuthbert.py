from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.global_flags[328] == 0):
	## cuthbert has not talked
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	if (attachee.map == 5080):
		attachee.remove_from_initiative()
		attachee.object_flag_set(OF_OFF)
		game.particles( "sp-Magic Circle against Chaos-END", attachee )
		game.sound( 4043, 1 )
		return SKIP_DEFAULT
	else:
		strategy = game.random_range(453,460)
		if (strategy == 453):
			attachee.obj_set_int(obj_f_critter_strategy, 453)
		elif (strategy == 454):
			attachee.obj_set_int(obj_f_critter_strategy, 454)
		elif (strategy == 455):
			attachee.obj_set_int(obj_f_critter_strategy, 455)
		elif (strategy == 456):
			attachee.obj_set_int(obj_f_critter_strategy, 456)
		elif (strategy == 457):
			attachee.obj_set_int(obj_f_critter_strategy, 457)
		elif (strategy == 458):
			attachee.obj_set_int(obj_f_critter_strategy, 458)
		elif (strategy == 459):
			attachee.obj_set_int(obj_f_critter_strategy, 459)
		elif (strategy == 460):
			attachee.obj_set_int(obj_f_critter_strategy, 460)
	return RUN_DEFAULT


def switch_to_iuz( cuthbert, pc, line ):
	iuz = find_npc_near(cuthbert,8042)
	if (iuz != OBJ_HANDLE_NULL):
		pc.begin_dialog(iuz,line)
		iuz.turn_towards(cuthbert)
		cuthbert.turn_towards(iuz)
	else:
		turn_off_gods( cuthbert, pc )
	return SKIP_DEFAULT


def cuthbert_raise_good( cuthbert, pc ):
	# raise all PC's and PC followers
	for obj in game.party:
		if (obj.stat_level_get(stat_hp_current) <= -10):
			obj.resurrect( CRITTER_R_CUTHBERT_RESURRECT, 0 )
		else:
#			obj.obj_set_int( obj_f_hp_damage, 0 )
			dice = dice_new("1d10+1000")
			obj.heal( OBJ_HANDLE_NULL, dice )
			obj.healsubdual( OBJ_HANDLE_NULL, dice )
	game.particles( "sp-consecrate-END", cuthbert )
	game.sound( 4043, 1 )
	return SKIP_DEFAULT


def turn_off_gods( cuthbert, pc ):
	cuthbert.remove_from_initiative()
	cuthbert.object_flag_set(OF_OFF)
	game.particles( "sp-Death Knell-Target", cuthbert )
	iuz = find_npc_near(cuthbert,8042)
	if (iuz != OBJ_HANDLE_NULL):
		iuz.remove_from_initiative()
		iuz.object_flag_set(OF_OFF)
		game.particles( "sp-Death Knell-Target", iuz )
	game.sound( 4165, 1 )
	return SKIP_DEFAULT


def unshit( attachee, triggerer ):
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
		attachee.reaction_set( pc, 50 )
	return RUN_DEFAULT