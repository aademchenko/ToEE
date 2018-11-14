from toee import *
from utilities import *
from combat_standard_routines import *


def san_heartbeat( attachee, triggerer ):
	if (attachee.name == 8861):
		if (game.global_vars[563] != 1):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 1
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8862):
		if (game.global_vars[563] != 2):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 2
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8863):
		if (game.global_vars[563] != 3):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 3
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8864):
		if (game.global_vars[563] != 4):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 4
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8865):
		if (game.global_vars[563] != 5):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 5
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8866):
		if (game.global_vars[563] != 6):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 6
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8867):
		if (game.global_vars[563] != 7):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 7
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8868):
		if (game.global_vars[563] != 8):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 8
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8869):
		if (game.global_vars[563] != 9):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 9
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8870):
		if (game.global_vars[563] != 10):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 10
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8871):
		if (game.global_vars[563] != 11):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 11
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8872):
		if (game.global_vars[563] != 12):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 12
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8873):
		if (game.global_vars[563] != 13):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 13
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8874):
		if (game.global_vars[563] != 14):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 14
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8875):
		if (game.global_vars[563] != 15):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 15
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8876):
		if (game.global_vars[563] != 16):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 16
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8877):
		if (game.global_vars[563] != 17):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 17
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8878):
		if (game.global_vars[563] != 18):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 18
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8879):
		if (game.global_vars[563] != 19):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 19
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8880):
		if (game.global_vars[563] != 20):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 20
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8881):
		if (game.global_vars[563] != 21):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 21
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8882):
		if (game.global_vars[563] != 22):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 22
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8883):
		if (game.global_vars[563] != 23):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 23
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8884):
		if (game.global_vars[563] != 24):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 24
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8885):
		if (game.global_vars[563] != 25):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 25
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8886):
		if (game.global_vars[563] != 26):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 26
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8887):
		if (game.global_vars[563] != 27):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 27
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8888):
		if (game.global_vars[563] != 28):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 28
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8889):
		if (game.global_vars[563] != 29):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 29
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8890):
		if (game.global_vars[563] != 30):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						game.sound ( 4039, 1 )
						game.global_vars[563] = 30
						if (game.global_flags[546] == 0):
							game.timevent_add( reset_ggv_563, ( attachee, ), 30000 )
							game.global_flags[546] = 1
	if (attachee.name == 8891):
		if (game.global_flags[547] == 0):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity_180(attachee, obj)):
						game.sound ( 4040, 1 )
						game.global_flags[547] = 1
						game.timevent_add( reset_ggf_547, ( attachee, ), 7000 )
	if (attachee.name == 8892):
		if (game.global_flags[548] == 0):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity_60(attachee, obj)):
						game.sound ( 4020, 1 )
						game.global_flags[548] = 1
						game.timevent_add( reset_ggf_548, ( attachee, ), 7300 )
	return RUN_DEFAULT


def in_proximity( sfx, listener ):
	if (sfx.distance_to(listener) <= 40):
		return 1
	return 0


def in_proximity_60( sfx, listener ):
	if (sfx.distance_to(listener) <= 60):
		return 1
	return 0


def in_proximity_180( sfx, listener ):
	if (sfx.distance_to(listener) <= 120):
		return 1
	return 0


def reset_ggv_563( attachee ):
	game.global_vars[563] = 0
	game.global_flags[546] = 0
	return


def reset_ggf_547( attachee ):
	game.global_flags[547] = 0
	return


def reset_ggf_548( attachee ):
	game.global_flags[548] = 0
	return