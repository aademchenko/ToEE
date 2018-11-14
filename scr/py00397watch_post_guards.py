from utilities import *
from toee import *
from combat_standard_routines import *


def san_heartbeat( attachee, triggerer ):
	if ( (attachee.map != 5171) and (game.party[0].reputation_has(34) == 1 or game.party[0].reputation_has(35) == 1 or game.party[0].reputation_has(42) == 1 or game.party[0].reputation_has(44) == 1 or game.party[0].reputation_has(45) == 1 or game.party[0].reputation_has(43) == 1 or game.party[0].reputation_has(46) == 1 or (game.global_vars[993] == 5 and game.global_flags[870] == 0)) ):
		if ( (game.global_vars[969] == 0) and (game.global_flags[955] == 0) ):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (is_better_to_talk(attachee,obj)):
						attachee.turn_towards(obj)
						obj.begin_dialog( attachee, 30 )
	elif ((attachee.map == 5149) and (game.global_vars[944] == 1 or game.global_vars[944] == 2) and (game.global_flags[861] == 0)):
		attachee.runoff(attachee.location-3)
		game.global_flags[861] = 1
#		game.new_sid = 0
	return RUN_DEFAULT