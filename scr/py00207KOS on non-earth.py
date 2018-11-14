from toee import *
from combat_standard_routines import *
from utilities import *
from Co8 import *
from py00439script_daemon import record_time_stamp, get_v, set_v, npc_set, npc_unset, npc_get, tsc, within_rect_by_corners


def san_first_heartbeat(attachee, triggerer):
	if attachee.name in [14337, 14338]:
		if attachee.scripts[15] == 0:
			attachee.scripts[15] = 2
	remove_dagger(attachee)
	game.new_sid = 0
	return RUN_DEFAULT

def san_will_kos( attachee, triggerer ):
	if get_v(454) & 1 != 0 and game.global_flags[104] == 1:
		# Earth Temple was on alert, and you killed Romag; don't expect to be safe in the Earth Temple anymore!
		return RUN_DEFAULT
	if (game.global_flags[347] == 1):
		# KOS override
		return SKIP_DEFAULT
	saw_ally_robe = 0
	saw_greater_robe = 0
	saw_enemy_robe = 0
	for obj in triggerer.group_list():
		robe = obj.item_worn_at(12)
		if (robe != OBJ_HANDLE_NULL):
			if ( robe.name == 3010 ):
				# Earth robe
				saw_ally_robe = 1
			elif ( robe.name == 3021 ):
				saw_greater_robe = 1
				break
			elif ( ( robe.name == 3020) or (robe.name == 3016 ) or (robe.name == 3017 ) ):
				saw_enemy_robe = 1
	if (saw_greater_robe):
		return SKIP_DEFAULT
	elif ((saw_ally_robe) and (not saw_enemy_robe)):
		return SKIP_DEFAULT
	else:
		return RUN_DEFAULT


def remove_dagger(npc):
	dagger = npc.item_find_by_proto(4060)
	while dagger != OBJ_HANDLE_NULL:
		dagger.destroy()
		dagger = npc.item_find_by_proto(4060)
	return
