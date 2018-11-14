from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if ((triggerer.stat_level_get(stat_level_druid) >= 1) or (game.party_alignment == TRUE_NEUTRAL)):
		if (not attachee.has_met(triggerer)):
			triggerer.begin_dialog( attachee, 1 )
		else:
			triggerer.begin_dialog( attachee, 70 )
	else:
		line = (game.random_range(0,2) * 10) + 80
		triggerer.begin_dialog( attachee, line )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	game.counters[0] = game.counters[0] + 1
	if (game.counters[0] >= 3):
		shapechange(attachee,triggerer,10)
	return SKIP_DEFAULT


def shapechange( attachee, triggerer, dialog_line ):
	loc = attachee.location
	attachee.destroy()
	kella = game.obj_create( 14236, loc )
	if (kella != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( kella, dialog_line )
	return SKIP_DEFAULT
