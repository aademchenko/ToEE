from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog(attachee,1)
	return SKIP_DEFAULT

def zap( attachee, triggerer ):
	damage_dice = dice_new( '5d4' )
	game.particles( 'sp-Shocking Grasp', triggerer )
	if triggerer.reflex_save_and_damage( OBJ_HANDLE_NULL, 20, D20_Save_Reduction_Half, D20STD_F_NONE, damage_dice, D20DT_ELECTRICITY, D20DAP_UNSPECIFIED, 0 , D20DAP_NORMAL ):
#		saving throw successful
		triggerer.float_mesfile_line( 'mes\\spell.mes', 30001 )
	else:
#		saving throw unsuccessful
		triggerer.float_mesfile_line( 'mes\\spell.mes', 30002 )

	return RUN_DEFAULT