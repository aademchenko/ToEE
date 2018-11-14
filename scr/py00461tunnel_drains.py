from toee import *
from utilities import *
from combat_standard_routines import *


def san_heartbeat( attachee, triggerer ):
	if (attachee.name == 8771):
		if (game.global_vars[537] != 1):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4145, 1 )
						game.global_vars[537] = 1
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8772):
		if (game.global_vars[537] != 2):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4145, 1 )
						game.global_vars[537] = 2
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8773):
		if (game.global_vars[537] != 3):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4145, 1 )
						game.global_vars[537] = 3
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8774):
		if (game.global_vars[537] != 4):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4145, 1 )
						game.global_vars[537] = 4
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8775):
		if (game.global_vars[537] != 5):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4145, 1 )
						game.global_vars[537] = 5
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8776):
		if (game.global_vars[537] != 6):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4145, 1 )
						game.global_vars[537] = 6
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8777):
		if (game.global_vars[537] != 7):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4146, 1 )
						game.global_vars[537] = 7
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8778):
		if (game.global_vars[537] != 8):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4146, 1 )
						game.global_vars[537] = 8
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8779):
		if (game.global_vars[537] != 9):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4146, 1 )
						game.global_vars[537] = 9
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8780):
		if (game.global_vars[537] != 10):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4147, 1 )
						game.global_vars[537] = 10
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8781):
		if (game.global_vars[537] != 11):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4147, 1 )
						game.global_vars[537] = 11
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8782):
		if (game.global_vars[537] != 12):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4147, 1 )
						game.global_vars[537] = 12
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8783):
		if (game.global_vars[537] != 13):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4147, 1 )
						game.global_vars[537] = 13
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8784):
		if (game.global_vars[537] != 14):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4147, 1 )
						game.global_vars[537] = 14
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8785):
		if (game.global_vars[537] != 15):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4147, 1 )
						game.global_vars[537] = 15
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8786):
		if (game.global_vars[537] != 16):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4148, 1 )
						game.global_vars[537] = 16
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8787):
		if (game.global_vars[537] != 17):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4148, 1 )
						game.global_vars[537] = 17
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8788):
		if (game.global_vars[537] != 18):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4148, 1 )
						game.global_vars[537] = 18
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8789):
		if (game.global_vars[537] != 19):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4148, 1 )
						game.global_vars[537] = 19
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	if (attachee.name == 8790):
		if (game.global_vars[537] != 20):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4148, 1 )
						game.global_vars[537] = 20
						if (game.global_flags[529] == 0):
							game.timevent_add( reset_ggv_537, ( attachee, ), 60000 )
							game.global_flags[529] = 1
	return RUN_DEFAULT


def in_proximity( sfx, listener ):
	if (sfx.distance_to(listener) <= 80):
		return 1
	return 0


def reset_ggv_537( attachee ):
	game.global_vars[537] = 0
	game.global_flags[529] = 0
	return