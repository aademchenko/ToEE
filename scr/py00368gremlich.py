from toee import *
from utilities import *
from co8 import *
import _include
from co8Util.TimedEvent import *
from combat_standard_routines import *
from py00439script_daemon import get_f, set_f, get_v, set_v, tpsts, record_time_stamp


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[929] == 1):
		attachee.object_flag_set(OF_OFF)
	elif (is_daytime() == 0):
		if (game.global_vars[927] == 4):
			attachee.object_flag_unset(OF_OFF)
			if (attachee.map == 5001):
				if (attachee.name == 14752):
					game.sound( 4126, 1 )
				elif (attachee.name == 14699):
					game.sound( 4128, 1 )
			elif (attachee.map == 5051):
				game.sound( 4127, 1 )
			elif (attachee.map == 5121):
				game.sound( 4129, 1 )
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if (game.global_vars[926] >= 3):
		if should_modify_CR( attachee ):
			modify_CR( attachee, get_av_level() )
		game.global_flags[929] = 1
		game.particles( 'hit-FIRE-medium', attachee )
		game.particles( 'ef-MinoCloud', attachee )
		attachee.object_flag_set(OF_OFF)
#		return RUN_DEFAULT
	elif (game.global_vars[926] <= 2):
		game.global_vars[926] = 0
		attachee.object_flag_set(OF_OFF)
		game.particles( 'ef-MinoCloud', attachee )
		if (attachee.name == 14752):
			grem2 = game.obj_create( 14699, attachee.location )
			game.particles( 'Trap-Fire', grem2 )
			grem2.turn_towards(game.party[0])
			game.sound( 4125, 1 )
			grem2.attack(triggerer)
		elif (attachee.name == 14699):
			grem1 = game.obj_create( 14752, attachee.location )
			game.particles( 'Trap-PoisonGas', grem1 )
			grem1.turn_towards(game.party[0])
			game.sound( 4129, 1 )
			grem1.attack(triggerer)
		return SKIP_DEFAULT
#		dice = dice_new("1d10+1000")
#		attachee.heal( OBJ_HANDLE_NULL, dice )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	game.global_vars[925] = game.global_vars[925] + 1
	if (obj_percent_hp(attachee) < 40):
		if (game.global_vars[926] <= 2):
			game.global_vars[926] = 0
			attachee.object_flag_set(OF_OFF)
			game.particles( 'ef-MinoCloud', attachee )
			if (attachee.name == 14752):
				grem2 = game.obj_create( 14699, attachee.location )
				game.particles( 'Trap-Fire', grem2 )
				grem2.turn_towards(game.party[0])
				game.sound( 4125, 1 )
				grem2.attack(triggerer)
			elif (attachee.name == 14699):
				grem1 = game.obj_create( 14752, attachee.location )
				game.particles( 'Trap-PoisonGas', grem1 )
				grem1.turn_towards(game.party[0])
				game.sound( 4129, 1 )
				grem1.attack(triggerer)
			return SKIP_DEFAULT
	elif (game.global_vars[925] == 0):
		return RUN_DEFAULT
	elif (game.global_vars[925] == 1):
		attachee.obj_set_int(obj_f_critter_strategy, 426)
		return RUN_DEFAULT
	elif (game.global_vars[925] == 2):
		attachee.obj_set_int(obj_f_critter_strategy, 427)
		return RUN_DEFAULT
	elif (game.global_vars[925] == 3):
		attachee.obj_set_int(obj_f_critter_strategy, 428)
		return RUN_DEFAULT
	elif (game.global_vars[925] == 4):
		attachee.obj_set_int(obj_f_critter_strategy, 429)
		return RUN_DEFAULT
	elif (game.global_vars[925] == 5):
		attachee.obj_set_int(obj_f_critter_strategy, 430)
		return RUN_DEFAULT
	elif (game.global_vars[925] == 6):
		attachee.obj_set_int(obj_f_critter_strategy, 431)
		return RUN_DEFAULT
	elif (game.global_vars[925] == 7):
		game.global_vars[925] = 0
		return RUN_DEFAULT


def san_exit_combat( attachee, triggerer ):
	if (attachee.map == 5001 or attachee.map == 5051 or attachee.map == 5121):
		attachee.object_flag_set(OF_OFF)
		if (game.global_flags[929] == 0):
			game.global_vars[927] = 5
			game.timevent_add( reset_gremlich, (), 432000000 ) #432000000ms is 5 days
			record_time_stamp('s_gremlich_2')
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_flags[929] == 1):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_spell_cast( attachee, triggerer, spell ):
	if ( spell.spell == spell_flare or spell.spell == spell_searing_light or spell.spell == spell_faerie_fire ):
		game.global_vars[926] = game.global_vars[926] + 1
		game.particles( 'hit-FIRE-medium', attachee )
		game.particles( 'ef-MinoCloud', attachee )
		game.sound( 4127, 1 )
	return RUN_DEFAULT


def reset_gremlich():
	game.encounter_queue.append(3440)
	set_f('s_gremlich_2_scheduled')
	return RUN_DEFAULT