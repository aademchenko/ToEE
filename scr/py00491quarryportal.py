from toee import *
from utilities import *
from combat_standard_routines import *


def san_use( door, triggerer ):
	if (game.global_vars[972] <= 28):
		damage_dice = dice_new( '4d8' )
		game.particles( "Mon-EarthElem-Unconceal", triggerer )
		game.particles( "Mon-EarthElem-body120", triggerer )
		game.particles( "hit-BLUDGEONING-medium", triggerer )
		triggerer.float_mesfile_line( 'mes\\float.mes', 3 )
		game.sound( 4042, 1 )
		if (triggerer.reflex_save_and_damage( OBJ_HANDLE_NULL, 20, D20_Save_Reduction_Half, D20STD_F_NONE, damage_dice, D20DT_BLUDGEONING, D20DAP_UNSPECIFIED, 0 , D20DAP_NORMAL )):
			triggerer.float_mesfile_line( 'mes\\spell.mes', 30001 )
		else:
			triggerer.float_mesfile_line( 'mes\\spell.mes', 30002 )
		return SKIP_DEFAULT
	else:
		return RUN_DEFAULT