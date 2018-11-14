from toee import *
from combat_standard_routines import *


def san_use( attachee, triggerer ):
	game.areas[4] = 1
	game.story_state = 4
	if attachee.name == 11002:
		# note from smigmal Redhand, as opposed to Alira's Temple map
		game.global_flags[425] = 1
	elif attachee.name == 11299: # Temple navigational map
		if not game.combat_is_active():
			talk_dude = OBJ_HANDLE_NULL
			if game.leader.type == obj_t_pc and game.leader.is_unconscious() == 0:
				talk_dude = game.leader
			else:
				for dude in game.party:
					if dude.type == obj_t_pc and dude.is_unconscious() == 0 and talk_dude == OBJ_HANDLE_NULL:
						talk_dude = dude
			if talk_dude != OBJ_HANDLE_NULL:
				talk_dude.scripts[9] = 435
				if  (talk_dude.area == 4 or talk_dude.map in [5064, 5065, 5066, 5067, 5079, 5080, 5092, 5105, 5110, 5111, 5112] ) and not (talk_dude.map in [ 5081, 5082, 5083, 5084]):
					talk_dude.begin_dialog(talk_dude, 1000 )
				else:
					talk_dude.begin_dialog(talk_dude, 1210 )
		return SKIP_DEFAULT
	return RUN_DEFAULT
