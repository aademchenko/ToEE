from toee import *
from utilities import *
from combat_standard_routines import *


def san_heartbeat( attachee, triggerer ):
	if (attachee.name == 8823):
		if (game.global_vars[546] != 1):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 1
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8824):
		if (game.global_vars[546] != 2):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 2
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8825):
		if (game.global_vars[546] != 3):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 3
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8826):
		if (game.global_vars[546] != 4):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 4
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8827):
		if (game.global_vars[546] != 5):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 5
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8828):
		if (game.global_vars[546] != 6):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 6
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8829):
		if (game.global_vars[546] != 7):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 7
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8830):
		if (game.global_vars[546] != 8):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 8
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8831):
		if (game.global_vars[546] != 9):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 9
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8832):
		if (game.global_vars[546] != 10):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 10
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8833):
		if (game.global_vars[546] != 11):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 11
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8834):
		if (game.global_vars[546] != 12):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 12
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8835):
		if (game.global_vars[546] != 13):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 13
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8836):
		if (game.global_vars[546] != 14):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 14
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8837):
		if (game.global_vars[546] != 15):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 15
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8838):
		if (game.global_vars[546] != 16):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 16
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8839):
		if (game.global_vars[546] != 17):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 17
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8840):
		if (game.global_vars[546] != 18):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 18
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8841):
		if (game.global_vars[546] != 19):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 19
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8842):
		if (game.global_vars[546] != 20):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 20
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8843):
		if (game.global_vars[546] != 21):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 21
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8844):
		if (game.global_vars[546] != 22):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 22
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8845):
		if (game.global_vars[546] != 23):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 23
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8846):
		if (game.global_vars[546] != 24):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 24
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8847):
		if (game.global_vars[546] != 25):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 25
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8848):
		if (game.global_vars[546] != 26):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 26
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8849):
		if (game.global_vars[546] != 27):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 27
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8850):
		if (game.global_vars[546] != 28):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 28
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8851):
		if (game.global_vars[546] != 29):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 29
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	if (attachee.name == 8852):
		if (game.global_vars[546] != 30):
			if (not game.combat_is_active()):
				for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
					if (in_proximity(attachee, obj)):
						drop = game.random_range(1,40)
						game.global_vars[546] = 30
						if (drop == 1):
							game.sound ( 4153, 1 )
						elif (drop == 2):
							game.sound ( 4154, 1 )
						elif (drop == 3):
							game.sound ( 4155, 1 )
						elif (drop == 4):
							game.sound ( 4156, 1 )
						elif (drop == 5):
							game.sound ( 4157, 1 )
						elif (drop == 6):
							game.sound ( 4158, 1 )
						elif (drop == 7):
							game.sound ( 4159, 1 )
						elif (drop == 8):
							game.sound ( 4160, 1 )
						elif (drop == 9):
							game.sound ( 4161, 1 )
						elif (drop == 10):
							game.sound ( 4162, 1 )
						elif (drop >= 11):
							return RUN_DEFAULT
	return RUN_DEFAULT


def in_proximity( sfx, listener ):
	if (sfx.distance_to(listener) <= 60):
		return 1
	return 0