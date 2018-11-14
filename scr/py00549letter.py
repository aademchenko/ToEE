from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.global_flags[818] == 1):
		triggerer.begin_dialog( attachee, 30 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_use( attachee, triggerer ):
	loc = triggerer.location
	npc = game.obj_create( 14678, loc )
	if (attachee.map == 5001 or attachee.map == 5002 or attachee.map == 5051 or attachee.map == 5062 or attachee.map == 5094 or attachee.map == 5068 or attachee.map == 5093 or attachee.map == 5091 or attachee.map == 5069 or attachee.map == 5112 or attachee.map == 5113 or attachee.map == 5121 or attachee.map == 5132 or attachee.map == 5108 or attachee.map == 5095 or attachee.map == 5070 or attachee.map == 5071 or attachee.map == 5072 or attachee.map == 5073 or attachee.map == 5074 or attachee.map == 5075 or attachee.map == 5076 or attachee.map == 5077 or attachee.map == 5078):
		triggerer.begin_dialog( npc, 1 )
	else:
		triggerer.begin_dialog( npc, 30 )
	return SKIP_DEFAULT